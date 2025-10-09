from pygame import *
from scripts.animations import load_animations


def handle_pacman_input(pacman, pressed_key):
    angle = pacman["angle"]
    if pressed_key == K_RIGHT:
        angle = 0
    elif pressed_key == K_UP:
        angle = 90
    elif pressed_key == K_LEFT:
        angle = 180
    elif pressed_key == K_DOWN:
        angle = 270

    if angle != pacman["angle"]:
        pacman = pacman.copy()
        pacman["angle"] = angle
        pacman["images"] = load_animations(
            pacman["image_path"], pacman["suffix"], 3, angle
        )
    return pacman
