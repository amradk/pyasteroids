import pygame
from gameobject import GameObject
from random import randrange

class Background():
    def __init__(self, screen, settings, group):
        self.max_stars = 250
        self.star_speed = 2
        self.stars = []
        self.group = group
        self.screen = screen

        # galaxy sprite
        self.galaxy_last_release = pygame.time.get_ticks()
        self.galaxy_released = True
        self.galaxy_period = 10000
        self.galaxy_speedx = 0
        self.galaxy_speedy = 3
        self.galaxy = GameObject(group, self.galaxy_speedx, self.galaxy_speedy, randrange(100, 539), -100)
        self.galaxy.set_image("assets/objects/galaxy.png")

    def init_bkg(self):
        """ Create the starfield """
        for i in range(self.max_stars):
            # A star is represented as a list with this format: [X,Y]
            star = [randrange(0, self.screen.get_width() - 1),
                    randrange(0, self.screen.get_height() - 1)]
            self.stars.append(star)

    def update_stars(self):
        """ Move and draw the stars in the given screen """
        for star in self.stars:
            star[1] += self.star_speed
            # If the star hit the bottom border then we reposition
            # it in the top of the screen with a random X coordinate.
            if star[1] >= self.screen.get_height():
                star[1] = 0
                star[0] = randrange(0, 639)

    def update_galaxy(self):
        now = pygame.time.get_ticks()
        if self.galaxy_released:
            if now - self.galaxy_last_release > self.galaxy_period:
                self.galaxy.set_y(-100)
                self.galaxy.set_x(randrange(0, 639))
                self.galaxy.set_speed_y(randrange(1, 3))
                self.group.add(self.galaxy)
                self.galaxy_released = False
                self.galaxy_last_release = now
        else:
            if self.galaxy.get_y() >= self.screen.get_height():
                self.galaxy_last_release = now
                self.galaxy_released = True
                self.galaxy.kill()

    def update(self):
        self.update_stars()
        self.update_galaxy()

    def draw(self):
        for star in self.stars:
            self.screen.set_at(star, (255, 255, 255))