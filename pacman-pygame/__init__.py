from pygame import *
import sys

from pacman import (
    create_pacman,
    handle_pacman_input,
    update_pacman,
    draw_pacman,
)
from scripts.obstacles import initialize_obstacles
from scripts.powers import initialize_powers
from scripts.ui import initialize_ui, ui_controller

init()
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 781
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = time.Clock()
ui_font = initialize_ui()
obstacles = initialize_obstacles(SCREEN_WIDTH, SCREEN_HEIGHT)
powers = initialize_powers(SCREEN_WIDTH, SCREEN_HEIGHT)
pacman = create_pacman(335, 580, 2, SCREEN_WIDTH, SCREEN_HEIGHT, obstacles)

playing = False

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

    for power in powers["items"]:
        screen.blit(powers["image"], power["coords"])

    pacman = update_pacman(pacman, playing)
    draw_pacman(pacman, screen, playing)

    for obstacle in obstacles:
        draw.rect(screen, (255, 0,0), obstacle, 1)

    ui_controller(ui_font, screen, playing)

    display.flip()
    clock.tick(60)
