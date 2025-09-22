from pygame import *
import time



def load_animations(prefijo, sufijo, n):
    images = []
    for i in range(1, n + 1):
        name = prefijo + str(i) + sufijo
        images.append(image.load(name))
    return images


def show_animation(images, freq, screen, x, y):
    frame = int(time.time() * freq) % len(images)
    screen.blit(images[frame], (x, y))