from pygame import *
from scripts.animations import load_animations, show_animation


def create_pacman(x, y, speed, screen_width, screen_height):
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
    }


def handle_pacman_input(pacman, key):
    angle = pacman["angle"]
    if key == K_RIGHT:
        angle = 0
    elif key == K_UP:
        angle = 90
    elif key == K_LEFT:
        angle = 180
    elif key == K_DOWN:
        angle = 270

    if angle != pacman["angle"]:
        pacman = pacman.copy()
        pacman["angle"] = angle
        pacman["images"] = load_animations(
            pacman["image_path"], pacman["suffix"], 3, angle
        )
    return pacman


def update_pacman(pacman):
    pacman = pacman.copy()
    angle = pacman["angle"]
    speed = pacman["speed"]

    if angle == 0:
        if pacman["x"] >= pacman["screen_width"]:
            pacman["x"] = 0
        pacman["x"] += speed
    elif angle == 90:
        if pacman["y"] <= 0:
            pacman["y"] = pacman["screen_height"]
        pacman["y"] -= speed
    elif angle == 180:
        if pacman["x"] <= 0:
            pacman["x"] = 800
        pacman["x"] -= speed
    elif angle == 270:
        if pacman["y"] >= pacman["screen_height"]:
            pacman["y"] = 0
        pacman["y"] += speed

    now = time.get_ticks()
    if now - pacman["last_update"] > 1000 // pacman["anim_fps"]:
        pacman["frame_index"] = (pacman["frame_index"] + 1) % len(pacman["images"])
        pacman["last_update"] = now
    return pacman


def draw_pacman(pacman, surface):
    show_animation(
        [pacman["images"][pacman["frame_index"]]], 1,
        surface, pacman["x"], pacman["y"]
    )
