import pygame
from titlestate import TitleState
from gamestate import GameState


class StateMananger(object):
    def __init__(self, screen):
        self.screen = screen
        self.scenes = {}
        self.cur_scene = None

    def go_to(self, scene, state):

        if state == 'init':
            if scene in self.scenes:
                self.scenes[scene].init()
            else:
                if scene == 'game':
                    self.scenes[scene] = GameState(self.screen, self)
                if scene == 'title':
                    self.scenes[scene] = TitleState(self.screen, self)
                self.scenes[scene].init()

            self.cur_scene = self.scenes[scene]

        if state == 'resume':
            self.cur_scene = self.scenes[scene]