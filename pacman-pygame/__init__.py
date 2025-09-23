from pygame import *
import sys

from pacman import (
    create_pacman,
    handle_pacman_input,
    update_pacman,
    draw_pacman,
)

init()
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 781
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = time.Clock()

pacman = create_pacman(100, 100, 2, SCREEN_WIDTH, SCREEN_HEIGHT)

playing = False

while True:
    screen.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                playing = not playing
            elif playing:
                pacman = handle_pacman_input(pacman, e.key)

    map = transform.scale(image.load("../assets/map.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(map, (0, 0))

    pacman = update_pacman(pacman, playing)
    draw_pacman(pacman, screen, playing)

    display.flip()
    clock.tick(60)