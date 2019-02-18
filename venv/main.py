import pygame
import sys
from gamestate import GameState
from statemanager import StateMananger
from titlestate import TitleState
from settings import Settings

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption(settings.caption)
    clock = pygame.time.Clock()

    state_manager = StateMananger(screen)

    #state = GameState(screen)
    #state.init_asteroids()
    state = TitleState(screen)

    # Запуск основного цикла игры.
    while True:
        # Lock the framerate at 50 FPS
        #clock.tick(30)
        clock.tick(60)

        state_manager.scene.handle_events(pygame.event.get())
        state_manager.scene.update()
        state_manager.scene.render(screen)
        #state.handle_events(pygame.event.get())
        #state.update()
        state_manager.draw()
        #pygame.display.flip()
        # Отслеживание событий клавиатуры и мыши.

run_game()
