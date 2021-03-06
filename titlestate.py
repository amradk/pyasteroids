import pygame
import thorpy
from state import State
from gamestate import GameState
import resources
import sys


class TitleState(State):
    def __init__(self, screen, scene_manager):
        super(State, self).__init__()
        self.scene_manager = scene_manager
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        # font settings
        self.font_size = 18
        self.font_name = pygame.font.match_font('arial')
        self.font = pygame.font.Font(self.font_name, self.font_size)
        # define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.YELLOW = (255, 255, 0)
        self.BAR_LENGTH = 100
        self.BAR_HEIGHT = 10
        # menu
        self.quit_btn = thorpy.make_button("Quit", func=thorpy.functions.quit_func)
        self.ng_btn = thorpy.make_button("New game", func = self.scene_manager.go_to, params = {'scene':'game', 'state':'init'})
        self.res_btn = thorpy.make_button("Resume", func = self.scene_manager.go_to, params = { 'scene':'game', 'state':'resume'})
        self.box = thorpy.Box.make(elements=[self.quit_btn, self.ng_btn, self.res_btn])

        self.menu = thorpy.Menu(self.box)
        for element in self.menu.get_population():
            element.surface = self.screen
        self.box.set_topleft((200, 200))
        #self.background = thorpy.Background(resources.background_image_path, elements=[self.box])

    def init(self):
        pass

    def draw(self):
        self.box.blit()

    def update(self):
        self.box.update()

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                sys.exit()
            else:
                self.menu.react(event)  # the menu automatically integrate your elements

    def switch_state(self):
        pass