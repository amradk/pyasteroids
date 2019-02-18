import pygame
from pygame import *

from state import State
import sys
from settings import Settings
from player import Player
from background import Background
from gameobject import GameObject
from asteroid import Asteroid
from random import randrange
import resources

class GameState(State):
    def __init__(self, screen):
        super(State, self).__init__()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.max_asteroids = 10
        # font settings
        self.font_size = 18
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.score_x =320
        self.score_y = 10
        self.scores = 0
        self.respawn_time = 5000
        self.asteroid_respawn_time = 5000
        self.asteroid_images = resources.asteroid_images
        self.settings = Settings()
        # define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.BAR_LENGTH = 100
        self.BAR_HEIGHT = 10
        # Группы для спрайтов
        self.sp_player = pygame.sprite.Group()
        self.sp_effects = pygame.sprite.Group()
        self.sp_asteroids = pygame.sprite.Group()
        self.sp_bullets = pygame.sprite.Group()
        self.sp_backgroud = pygame.sprite.Group()

        self.pl = Player(self.sp_player, self.sp_effects,
                         self.screen, self.settings, 0, 0, self.screen_rect.centerx, self.screen_rect.bottom)
        self.sp_player.add(self.pl)

        self.bg = Background(self.screen, self.settings, self.sp_backgroud)
        self.bg.init_bkg()
        self.asteroids = []

    def draw_text(self, text, x, y):
        text_surface = self.font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_shield_bar(self):
        self.draw_bar(5, 20, self.pl.get_shield(), self.GREEN)

    def draw_health_bar(self):
        self.draw_bar(5, 40, self.pl.get_hp(), self.RED)

    def init_asteroids(self):
        for i in range(self.max_asteroids):
            asteroid = Asteroid(self.sp_asteroids, self.sp_effects, 0, randrange(3, 5),
                    randrange(0, self.screen.get_width() - 1), (0 - randrange(100, 200)))
            asteroid.set_images(self.asteroid_images[randrange(1, 6)])
            self.asteroids.append(asteroid)
        self.sp_asteroids.add(self.asteroids)

    # ДК: кажется это надо переписать
    def update_asteroids(self):
        # Move and draw the asteroids in the given screen
        now = pygame.time.get_ticks()
        for asteroid in self.asteroids:
            # Если координаты астероида выходят за нижнюю границу игрового поля
            # перемещаем его за верхнюю границу и назначаем новую скорость
            if asteroid.get_y() >= self.screen.get_height():
                asteroid.set_y(-100)
                asteroid.set_x(randrange(0, 639))
                asteroid.set_speed(randrange(2, 6))
            # Оживляем убитые астероиды
            if asteroid.get_is_destroyed() == True:
                if (now - asteroid.get_last_death()) > self.respawn_time:
                    asteroid.respawn()
                    asteroid.set_images(self.asteroid_images[randrange(1, 6)])

    def draw_bar(self, x, y, value, color):
        if value < 0:
            value = 0
        fill = (value / 100) * self.BAR_LENGTH
        outline_rect = pygame.Rect(x, y, self.BAR_LENGTH, self.BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, self.BAR_HEIGHT)
        pygame.draw.rect(self.screen, color, fill_rect)
        pygame.draw.rect(self.screen, self.WHITE, outline_rect, 2)


    def draw_hud(self):
        self.draw_health_bar()
        self.draw_shield_bar()
        self.draw_text(str(self.scores), self.score_x, self.score_y)

    def update(self):
        # Update sprites
        self.sp_backgroud.update()
        self.sp_player.update()
        self.sp_asteroids.update()
        self.update_asteroids()
        self.sp_effects.update()
        self.sp_bullets.update()

        # Обработка столкновений -> выстрел, астероид
        hits = pygame.sprite.groupcollide(self.sp_asteroids, self.sp_bullets, False, True)
        for hit in hits:
            hit.death()
            self.scores += 10

        # Обработка столкновений -> астероид, игрок
        hits = pygame.sprite.groupcollide(self.sp_asteroids, self.sp_player, False, False)
        for hit in hits:
            hit.death()
            self.pl.get_damage(hit.do_damage())

        # Отображение последнего прорисованного экрана.
        self.bg.update()

    def draw(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill((0, 0, 0))
        # Отображение последнего прорисованного экрана.
        self.bg.draw()
        self.sp_backgroud.draw(self.screen)
        self.sp_asteroids.draw(self.screen)
        self.sp_effects.draw(self.screen)
        self.sp_player.draw(self.screen)
        self.sp_bullets.draw(self.screen)

        self.draw_hud()
        pygame.display.flip()

    # ДК обработка событий, нажатие клавишь
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Реагирует на нажатие клавиш.
                if event.key == pygame.K_RIGHT:
                    self.pl.moving_right = True
                    self.pl.set_image_righ()
                elif event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_LEFT:
                    self.pl.moving_left = True
                    self.pl.set_image_left()
                elif event.key == pygame.K_SPACE:
                    self.sp_bullets.add(self.pl.shoot())
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.pl.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.pl.moving_left = False
                self.pl.set_image_neutral()