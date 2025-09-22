from pygame import *
import time



def load_animations(prefix, suffix, n, angle):
    images = []
    for i in range(1, n + 1):
        name = prefix + str(i) + suffix
        img = transform.rotate(image.load(name), angle)
        images.append(img)
    return images


def show_animation(images, freq, screen, x, y):
    frame = int(time.time() * freq) % len(images)
    screen.blit(images[frame], (x, y))