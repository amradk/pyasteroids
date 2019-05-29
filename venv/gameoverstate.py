import pygame
from pygame import *
from state import State
import sys
from gameobject import GameObject
import resources


class GameOverState(State):

    def __init__(self, screen, state_manager):
        super(State, self).__init__()
        self.state_manager = state_manager
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # font settings
        self.font_size = 18
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.Font(self.font_name, self.font_size)
        self.score_x =320
        self.score_y = 10
        self.scores = 0
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
        self.sp = pygame.sprite.Group()

    def init(self):
        self.screen.fill((0, 0, 255))
        self.scores = 0
        #ДК очищаем игры
        self.sp.empty()

    def update(self):
        # Update sprites
        self.sp.update()

    def draw(self):
        # При каждом проходе цикла перерисовывается экран.
        self.screen.fill((0, 0, 0))
        # Отображение последнего прорисованного экрана.
        self.sp.draw(self.screen)

        pygame.display.flip()

    # ДК обработка событий, нажатие клавишь
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
