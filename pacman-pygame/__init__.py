from pygame import *
import sys

from pacman import (
    create_pacman,
    handle_pacman_input,
    update_pacman,
    draw_pacman,
)

init()
screen_width, screen_height = 700, 781
screen = display.set_mode((screen_width, screen_height))
clock = time.Clock()

pacman = create_pacman(100, 100, 2, screen_width, screen_height)

while True:
    screen.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN:
            pacman = handle_pacman_input(pacman, e.key)

    map = transform.scale(image.load("../assets/map.png"), (screen_width, screen_height))
    screen.blit(map, (0, 0))

    pacman = update_pacman(pacman)
    draw_pacman(pacman, screen)

    display.flip()
    clock.tick(60)