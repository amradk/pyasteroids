import pygame
from gameobject import GameObject

class Bullet(GameObject):
    def __init__(self, screen, speedx, speedy, start_x, start_y, animation_speed = 60 ):
        GameObject.__init__(self, screen, speedx, speedy, start_x, start_y, animation_speed)
        self.image = pygame.image.load("assets/objects/shoots/laserGreen.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.bottom = start_y
        self.rect.centerx = start_x
        self.speedy = speedy

    def update(self):
        self.rect.y += self.speedy
        # kill if it moves off the top of the screen
        if self.rect.top < 0:
            self.kill()
