import pygame
from titlestate import TitleState

class StateMananger(object):
    def __init__(self, screen):
        self.screen = screen
        self.go_to(TitleState(screen))

    def go_to(self, scene):
        self.scene = scene
        self.scene.manager = self