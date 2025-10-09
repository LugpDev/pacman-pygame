from pygame import *
from scripts.animations import load_animations


def create_pacman(x, y, speed, screen_width, screen_height, obstacles):
    image_path = "../assets/pacman/pacman"
    suffix = ".png"

    return {
        "x": x,
        "y": y,
        "speed": speed,
        "angle": 0,
        "anim_fps": 5,
        "image_path": image_path,
        "suffix": suffix,
        "images": load_animations(image_path, suffix, 3, 0),
        "frame_index": 0,
        "last_update": time.get_ticks(),
        "screen_width": screen_width,
        "screen_height": screen_height,
        "obstacles": obstacles,
    }
