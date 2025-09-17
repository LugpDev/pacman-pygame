from pygame import *
import sys

init()
screen = display.set_mode((800, 600))
myFont = font.SysFont('menlo', 60)

frames = 0
while True:
    screen.fill((255, 255, 255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
    texto = myFont.render(str(frames), True, (50, 70, 80))
    screen.blit(texto, (200, 10))
    display.flip()
    frames += 1
