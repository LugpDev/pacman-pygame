import random

from pygame import *
import sys

from scripts.animations import load_animations
from scripts.animations import show_animation

init()
screen = display.set_mode((800, 600))

angle = 0
while True:
    screen.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT: sys.exit()
        if e.type == KEYDOWN:
            if e.key == K_w:
                angle = 90
            elif e.key == K_s:
                angle = -90
            elif e.key == K_a:
                angle = 180
            elif e.key == K_d:
                angle = 0

    images = load_animations("../assets/pacman/pacman", ".png", 3, angle)
    show_animation(images, 5, screen, 100, 100)

    display.flip()