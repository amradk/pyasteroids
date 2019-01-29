import pygame
from gameobject import GameObject

class GameEffect(GameObject):
    """ Класс для еффектов (взрывы, всполохи и проч. короткоживущие объекты)"""
    def __init__(self, group, start_x, start_y, ttl = 250, animation_speed = 60 ):
        GameObject.__init__(self, group, 0, start_x, start_y, animation_speed)
        self.images = []
        # TTL - time to life, a time after will self remove from groups
        self.ttl = ttl
        self.last_appears = pygame.time.get_ticks()

        self.animation_step = 0
        self.animation_len = 0
        self.elapsed = pygame.time.get_ticks()
        self.animation_speed = animation_speed


    def set_ttl(self, ttl):
        self.ttl = ttl

    def set_images(self, image_list = []):
        for i in image_list:
            image = pygame.image.load(i).convert_alpha()
            self.images.append(image)
        self.animation_len = len(self.images)
        if self.animation_len > 1:
            self.ttl = self.animation_speed * self.animation_len
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.top = self.start_y
        self.rect.centerx = self.start_x

    def update_time(self):
        self.last_appears = pygame.time.get_ticks()

    def update(self):
        """Обновляет анимацию."""
        # Если с момента создания прошло больше чем ttl,
        # то удалить обёект из групп
        now = pygame.time.get_ticks()
        if now - self.last_appears > self.ttl:
            self.kill()
            return

        if self.animation_len > 1:
            if (now - self.elapsed) > self.animation_speed:  # animate every second
                self.animation_step = (self.animation_step + 1) % self.animation_len
                self.elapsed = now
            self.image = self.images[self.animation_step]
