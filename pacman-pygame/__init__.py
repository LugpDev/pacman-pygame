from pygame import *
import sys
from pacman import (
    create_pacman,
    handle_pacman_input,
    update_pacman,
    draw_pacman,
)

init()
screen = display.set_mode((800, 600))
clock = time.Clock()

pacman = create_pacman(100, 100, 1)

while True:
    screen.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN:
            pacman = handle_pacman_input(pacman, e.key)

    pacman = update_pacman(pacman)
    draw_pacman(pacman, screen)

    display.flip()
    clock.tick(60)