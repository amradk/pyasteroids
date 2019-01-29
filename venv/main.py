import pygame
import sys
from settings import Settings
from player import Player
from background import Background
from gameobject import GameObject
from asteroid import Asteroid
from random import randrange

asteroid_images = {
    1 : [
        "assets/objects/asteroids/a10000.png",
        "assets/objects/asteroids/a10001.png",
        "assets/objects/asteroids/a10002.png",
        "assets/objects/asteroids/a10003.png",
        "assets/objects/asteroids/a10004.png",
        "assets/objects/asteroids/a10005.png",
        "assets/objects/asteroids/a10006.png",
        "assets/objects/asteroids/a10007.png",
        "assets/objects/asteroids/a10008.png",
        "assets/objects/asteroids/a10009.png",
        "assets/objects/asteroids/a10010.png",
        "assets/objects/asteroids/a10011.png",
        "assets/objects/asteroids/a10012.png",
        "assets/objects/asteroids/a10013.png",
        "assets/objects/asteroids/a10014.png",
        "assets/objects/asteroids/a10015.png",
    ],

    2 : [
        "assets/objects/asteroids/a30000.png",
        "assets/objects/asteroids/a30001.png",
        "assets/objects/asteroids/a30002.png",
        "assets/objects/asteroids/a30003.png",
        "assets/objects/asteroids/a30004.png",
        "assets/objects/asteroids/a30005.png",
        "assets/objects/asteroids/a30006.png",
        "assets/objects/asteroids/a30007.png",
        "assets/objects/asteroids/a30008.png",
        "assets/objects/asteroids/a30009.png",
        "assets/objects/asteroids/a30010.png",
        "assets/objects/asteroids/a30011.png",
        "assets/objects/asteroids/a30012.png",
        "assets/objects/asteroids/a30013.png",
        "assets/objects/asteroids/a30014.png",
        "assets/objects/asteroids/a30015.png",
    ],

    3 : [
        "assets/objects/asteroids/a40000.png",
        "assets/objects/asteroids/a40001.png",
        "assets/objects/asteroids/a40002.png",
        "assets/objects/asteroids/a40003.png",
        "assets/objects/asteroids/a40004.png",
        "assets/objects/asteroids/a40005.png",
        "assets/objects/asteroids/a40006.png",
        "assets/objects/asteroids/a40007.png",
        "assets/objects/asteroids/a40008.png",
        "assets/objects/asteroids/a40009.png",
        "assets/objects/asteroids/a40010.png",
        "assets/objects/asteroids/a40011.png",
        "assets/objects/asteroids/a40012.png",
        "assets/objects/asteroids/a40013.png",
        "assets/objects/asteroids/a40014.png",
        "assets/objects/asteroids/a40015.png",
    ],

    4: [
        "assets/objects/asteroids/b10000.png",
        "assets/objects/asteroids/b10001.png",
        "assets/objects/asteroids/b10002.png",
        "assets/objects/asteroids/b10003.png",
        "assets/objects/asteroids/b10004.png",
        "assets/objects/asteroids/b10005.png",
        "assets/objects/asteroids/b10006.png",
        "assets/objects/asteroids/b10007.png",
        "assets/objects/asteroids/b10008.png",
        "assets/objects/asteroids/b10009.png",
        "assets/objects/asteroids/b10010.png",
        "assets/objects/asteroids/b10011.png",
        "assets/objects/asteroids/b10012.png",
        "assets/objects/asteroids/b10013.png",
        "assets/objects/asteroids/b10014.png",
        "assets/objects/asteroids/b10015.png",
    ],

    5: [
        "assets/objects/asteroids/b30000.png",
        "assets/objects/asteroids/b30001.png",
        "assets/objects/asteroids/b30002.png",
        "assets/objects/asteroids/b30003.png",
        "assets/objects/asteroids/b30004.png",
        "assets/objects/asteroids/b30005.png",
        "assets/objects/asteroids/b30006.png",
        "assets/objects/asteroids/b30007.png",
        "assets/objects/asteroids/b30008.png",
        "assets/objects/asteroids/b30009.png",
        "assets/objects/asteroids/b30010.png",
        "assets/objects/asteroids/b30011.png",
        "assets/objects/asteroids/b30012.png",
        "assets/objects/asteroids/b30013.png",
        "assets/objects/asteroids/b30014.png",
        "assets/objects/asteroids/b30015.png",
    ],

    6: [
        "assets/objects/asteroids/b40000.png",
        "assets/objects/asteroids/b40001.png",
        "assets/objects/asteroids/b40002.png",
        "assets/objects/asteroids/b40003.png",
        "assets/objects/asteroids/b40004.png",
        "assets/objects/asteroids/b40005.png",
        "assets/objects/asteroids/b40006.png",
        "assets/objects/asteroids/b40007.png",
        "assets/objects/asteroids/b40008.png",
        "assets/objects/asteroids/b40009.png",
        "assets/objects/asteroids/b40010.png",
        "assets/objects/asteroids/b40011.png",
        "assets/objects/asteroids/b40012.png",
        "assets/objects/asteroids/b40013.png",
        "assets/objects/asteroids/b40014.png",
        "assets/objects/asteroids/b40015.png",
    ],

}

regular_explosion = [
    "assets/objects/explosion/regularExplosion01.png",
    "assets/objects/explosion/regularExplosion02.png",
    "assets/objects/explosion/regularExplosion03.png",
    "assets/objects/explosion/regularExplosion04.png",
    "assets/objects/explosion/regularExplosion05.png",
    "assets/objects/explosion/regularExplosion06.png",
    "assets/objects/explosion/regularExplosion07.png",
    "assets/objects/explosion/regularExplosion08.png",
]

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

max_asteroids = 10

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def draw_shield_bar(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, GREEN, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)


def draw_health_bar(surf, x, y, pct):
    if pct < 0:
        pct = 0
    BAR_LENGTH = 100
    BAR_HEIGHT = 10
    fill = (pct / 100) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(surf, RED, fill_rect)
    pygame.draw.rect(surf, WHITE, outline_rect, 2)

def init_asteroids(group, eff_group, max_asteroids, asteroid_images, screen):
    asteroids = []
    for i in range(max_asteroids):
        asteroid = Asteroid(group, eff_group, randrange(3, 5), randrange(0, screen.get_width() - 1),
                              (0 - randrange(100, 200)))
        asteroid.set_images(asteroid_images[randrange(1, 6)])
        asteroids.append(asteroid)

    return asteroids

def update_asteroids(asteroids, screen, respawn_time):
    # Move and draw the asteroids in the given screen
    now = pygame.time.get_ticks()
    for asteroid in asteroids:
        # Если координаты астероида выходят за нижнюю границу игрового поля
        # перемещаем его за верхнюю границу и назначаем новую скорость
        if asteroid.get_y() >= screen.get_height():
            asteroid.set_y(-100)
            asteroid.set_x(randrange(0, 639))
            asteroid.set_speed(randrange(2, 6))
        # Оживляем убитые астероиды
        if asteroid.get_is_destroyed() == True:
            if (now - asteroid.get_last_death()) > respawn_time:
                asteroid.respawn()
                #asteroid.set_images(asteroid_images[randrange(1, 6)])


def run_game():
    scores = 0
    respawn_time = 5000
    # Инициализирует игру и создает объект экрана.
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    screen_rect = screen.get_rect()
    pygame.display.set_caption(settings.caption)
    clock = pygame.time.Clock()

    # Группы для спрайтов
    sp_player = pygame.sprite.Group()
    sp_effects = pygame.sprite.Group()
    sp_asteroids = pygame.sprite.Group()
    sp_bullets = pygame.sprite.Group()

    pl = Player(sp_player, sp_effects, screen, settings, 0, screen_rect.centerx, screen_rect.bottom )
    sp_player.add(pl)
    bg = Background(screen, settings)
    bg.init_bkg(screen)
    asteroids = init_asteroids(sp_asteroids, sp_effects, max_asteroids, asteroid_images, screen)
    sp_asteroids.add(asteroids)


    # Запуск основного цикла игры.
    while True:
        # Lock the framerate at 50 FPS
        clock.tick(30)

        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                # Реагирует на нажатие клавиш.
                if event.key == pygame.K_RIGHT:
                    pl.moving_right = True
                    pl.set_image_righ()
                elif event.key == pygame.K_LEFT:
                    pl.moving_left = True
                    pl.set_image_left()
                elif event.key == pygame.K_SPACE:
                    sp_bullets.add(pl.shoot())
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    pl.moving_right = False
                elif event.key == pygame.K_LEFT:
                    pl.moving_left = False
                pl.set_image_neutral()

        # Update sprites
        sp_player.update()
        sp_asteroids.update()
        sp_effects.update()
        sp_bullets.update()

        # Обработка столкновений -> выстрел, астероид
        hits = pygame.sprite.groupcollide(sp_asteroids, sp_bullets, False, True)
        for hit in hits:
            hit.death()
            scores += 10

        # Обработка столкновений -> астероид, игрок
        hits = pygame.sprite.groupcollide(sp_asteroids, sp_player, False, False)
        for hit in hits:
            hit.death()
            pl.get_damage(hit.do_damage())

        update_asteroids(asteroids, screen, respawn_time)

        # При каждом проходе цикла перерисовывается экран.
        screen.fill((0, 0, 0))
        # Отображение последнего прорисованного экрана.
        bg.move_and_draw_bkg(screen)
        sp_asteroids.draw(screen)
        sp_effects.draw(screen)
        sp_player.draw(screen)
        sp_bullets.draw(screen)
        draw_text(screen, str(scores), 18, 320, 10)
        draw_shield_bar(screen, 5, 5, pl.get_shield())
        draw_health_bar(screen, 5, 20, pl.get_hp())
        pygame.display.flip()

run_game()