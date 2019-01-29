import pygame
from random import randrange

class Background():
    def __init__(self, screen, settings):
        self.max_stars = 250
        self.star_speed = 2
        self.stars = []

    def init_bkg(self, screen):
        """ Create the starfield """
        for i in range(self.max_stars):
            # A star is represented as a list with this format: [X,Y]
            star = [randrange(0, screen.get_width() - 1),
                    randrange(0, screen.get_height() - 1)]
            self.stars.append(star)

    def move_and_draw_bkg(self, screen):
        """ Move and draw the stars in the given screen """
        for star in self.stars:
            star[1] += self.star_speed
            # If the star hit the bottom border then we reposition
            # it in the top of the screen with a random X coordinate.
            if star[1] >= screen.get_height():
                star[1] = 0
                star[0] = randrange(0, 639)
            screen.set_at(star, (255, 255, 255))