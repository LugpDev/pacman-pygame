from pygame import *
import sys

init()
screen = display.set_mode((800, 600))

frames = 0
while True:
    screen.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT: sys.exit()
    display.flip()