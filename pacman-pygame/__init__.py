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

pacman = create_pacman(335, 580, 2, SCREEN_WIDTH, SCREEN_HEIGHT)

playing = False

myFont = font.SysFont('menlo', 30)

while True:
    screen.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN:
            if playing:
                pacman = handle_pacman_input(pacman, e.key)
            elif e.key == K_SPACE:
                playing = True

    map = transform.scale(image.load("../assets/map.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(map, (0, 0))

    pacman = update_pacman(pacman, playing)
    draw_pacman(pacman, screen, playing)

    if not playing:
        texto = myFont.render("Press space to start playing...", True, (255, 255, 255))
        screen.blit(texto, (100, 350))

    display.flip()
    clock.tick(60)
