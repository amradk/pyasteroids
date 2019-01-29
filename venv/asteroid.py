import pygame
from random import randrange
from gameobject import GameObject
from gameeffect import GameEffect


class Asteroid(GameObject):
    """Анимированные (вращение) астероиды"""
    def __init__(self, group, eff_group, speed, start_x, start_y, animation_speed = 60 ):
        GameObject.__init__(self, group, speed, start_x, start_y, animation_speed)
        self.images = []
        self.animation_step = 0
        self.animation_len = 0
        self.last_death = 0
        self.elapsed = pygame.time.get_ticks()
        self.animation_speed = animation_speed
        self.effect_group = eff_group
        self.hp = 100
        self.damage = 30
        # Взрыв
        self.explosion = GameEffect(self.effect_group, start_x, self.rect.top);
        self.explosion.set_images([
            "assets/objects/explosion/regularExplosion01.png",
            "assets/objects/explosion/regularExplosion02.png",
            "assets/objects/explosion/regularExplosion03.png",
            "assets/objects/explosion/regularExplosion04.png",
            "assets/objects/explosion/regularExplosion05.png",
            "assets/objects/explosion/regularExplosion06.png",
            "assets/objects/explosion/regularExplosion07.png",
            "assets/objects/explosion/regularExplosion08.png",
        ])
        # удаляем из груп чтобы избежать отрисовки раньше времени
        self.effect_group.remove(self.explosion)
        self.is_destroyed = False


    def set_images(self, image_list = []):
        self.images.clear()
        for i in image_list:
            image = pygame.image.load(i).convert_alpha()
            self.images.append(image)
        self.animation_len = len(self.images)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.top = self.start_y
        self.rect.centerx = self.start_x

    def update(self):
        """Обновляет анимацию."""
        now = pygame.time.get_ticks()
        if self.is_destroyed == False:
            if (now - self.elapsed) > self.animation_speed:  # animate every second
                self.animation_step = (self.animation_step + 1) % self.animation_len
                self.elapsed = now
            self.image = self.images[self.animation_step]
            self.rect.top += self.speed

    def do_damage(self):
        return self.damage

    def get_damage(self, damage = 0):
        pass

    def death(self):
        self.kill()
        self.is_destroyed = True
        self.effect_group.add(self.explosion)
        self.explosion.set_y(self.rect.top)
        self.explosion.set_x(self.rect.centerx)
        self.explosion.update_time()
        self.last_death = pygame.time.get_ticks()

    # Дабы оживлять астероиды после их уничтожения
    # нужно для переиспользования уже имеющихся
    # объектов, вместо создания новых
    def set_live_status(self, status):
        self.is_destroyed = status

    def get_last_death(self):
        return self.last_death

    def get_is_destroyed(self):
        return self.is_destroyed

    def respawn(self):
        print("Asteroid is respawned")
        self.is_destroyed = False
        # respawn
        self.rect.top = -100
        self.rect.centerx = randrange(0, 639)
        self.speed = randrange(2, 6)
        self.group.add(self)

