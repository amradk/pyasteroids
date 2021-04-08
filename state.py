import pygame


class State(object):

    def __init__(self):
        self.done = False
        self.next = None
        self.quit = False
        self.previous = None

    def init(self):
        raise NotImplementedError

    def draw(self):
        raise NotImplementedError

    def update(self):
        raise NotImplementedError

    def handle_events(self, events):
        raise NotImplementedError