import random

from pygame import *
import sys

from scripts.animations import load_animations
from scripts.animations import show_animation

init()
screen = display.set_mode((800, 600))

while True:
    screen.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT: sys.exit()

    images = load_animations("../assets/pacman/pacman", ".png", 3, random.randint(0, 0))
    show_animation(images, 5, screen, 100, 100)

    display.flip()