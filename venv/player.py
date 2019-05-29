import pygame
from bullet import Bullet
from gameobject import GameObject
from gameeffect import GameEffect


class Player(GameObject):

    def __init__(self, pl_group, ef_group, screen, settings, speedx, speedy, start_x, start_y, animation_speed = 60):
        GameObject.__init__(self, pl_group, speedx, speedy, start_x, start_y, animation_speed)
        """Инициализирует корабль и задает его начальную позицию."""
        # Загрузка изображения корабля и получение прямоугольника.
        self.image_neutral = pygame.image.load(settings.player_ship).convert_alpha()
        self.image_left = pygame.image.load(settings.player_ship_left).convert_alpha()
        self.image_right = pygame.image.load(settings.player_ship_right).convert_alpha()

        self.hp = 100
        self.shield_hp = 100
        self.damage = 30

        self.effect_group = ef_group
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = self.image_neutral
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = start_x
        self.rect.bottom = start_y

        # ДК, для анимации выстрела
        self.last_shot = pygame.time.get_ticks()
        self.blast = GameEffect(self.group, 0, 0, start_x, self.rect.top, 60);
        self.blast.set_images(["assets/objects/shoots/laserGreenShot.png"])
        self.blast.set_y(self.rect.top - self.blast.get_height() + 10)
        # удаляем из груп чтобы избежать отрисовки раньше времени
        self.effect_group.remove(self.blast)

        # Щит
        self.shield = GameEffect(self.effect_group, 0, 0, start_x, self.rect.top, 150)
        self.shield.set_images([settings.player_shield])
        self.last_damage = pygame.time.get_ticks()

        # Воccтановления щита, если 5 сек. без повреждений то восстанавливаем
        # 2 еденицы энергии каждые 5 сек
        self.last_damage = 0
        self.shield_last_restore = pygame.time.get_ticks()
        self.shield_recahrge_period = 10000
        self.shield_energy_restore = 5
        self.shield_restore_delay = 1000

        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
        self.speed = settings.player_speed
        self.center = float(self.rect.centerx)

    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed
            self.set_image_righ()
        if self.moving_left and self.rect.left > 0:
            self.center -= self.speed
            self.set_image_left()
        # Обновление атрибута rect на основании self.center
        self.rect.centerx = self.center
        self.shield_restore()

    def shield_restore(self):
        if self.shield_hp < 100:
            now = pygame.time.get_ticks()
            if now - self.last_damage > self.shield_recahrge_period:
                if now - self.shield_last_restore > self.shield_restore_delay:
                    self.shield_hp += self.shield_energy_restore
                    self.shield_last_restore = now

    def set_image_neutral(self):
        if self.image != self.image_neutral:
            self.image = self.image_neutral

    def set_image_left(self):
        if self.image != self.image_left:
            self.image = self.image_left

    def set_image_righ(self):
        if self.image != self.image_right:
            self.image = self.image_right

    def shoot(self):
        self.blast.update_time()
        self.blast.set_x(self.rect.centerx)
        self.effect_group.add(self.blast)
        #if now - self.last_shot > self.shoot_delay:
        #    self.group.remove(self.blast)
        #    self.last_shot = now
        bullet = Bullet(self.group, 0, -5, self.rect.centerx, self.rect.top - 10)

        return bullet

    def get_shield(self):
        return self.shield_hp

    def get_hp(self):
        return self.hp

    def get_damage(self, damage = 0):
        if self.shield_hp > 0:
            self.shield.set_x(self.rect.centerx)
            self.shield.update_time()
            self.shield.set_x(self.rect.centerx)
            self.group.add(self.shield)
            self.shield_hp -= damage
            self.last_damage = pygame.time.get_ticks()
            if self.shield_hp < 0:
                self.shield_hp = 0
        else:
            self.hp -= damage

    def set_hp(self, hp):
        self.hp = hp

    def set_shield(self, shield):
        self.shield_hp = shield
