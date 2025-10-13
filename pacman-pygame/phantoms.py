from pygame import *

from scripts.check_collision import check_collision

WIDTH, HEIGHT = 35, 30


def load_sprite(name):
    sprite = transform.scale(image.load(f'../assets/phantoms/{name}.png'), (WIDTH, HEIGHT))
    return sprite


def create_phantoms(speed):
    return [
        {
            "name": "orange",
            "sprite": load_sprite("orange"),
            "x": 295,
            "y": 270,
            "speed": speed,
        },
        {
            "name": "red",
            "sprite": load_sprite("red"),
            "x": 370,
            "y": 270,
            "speed": speed,
        },
        {
            "name": "pink",
            "sprite": load_sprite("pink"),
            "x": 70,
            "y": 350,
            "speed": speed,
        },
        {
            "name": "blue",
            "sprite": load_sprite("blue"),
            "x": 600,
            "y": 350,
            "speed": speed,
        }
    ]


def get_phantom_collision(phantom, obstacles, angle):
    collided = check_collision(obstacles, WIDTH, HEIGHT, phantom["x"], phantom["y"], phantom["speed"], angle)
    return collided


def update_phantom(phantom, dest, obstacles, playing):
    if not playing:
        return phantom

    dest_x, dest_y = dest[0], dest[1]

    right_collided = get_phantom_collision(phantom, obstacles, 0)
    up_collided = get_phantom_collision(phantom, obstacles, 90)
    left_collided = get_phantom_collision(phantom, obstacles, 180)
    down_collided = get_phantom_collision(phantom, obstacles, 270)

    if phantom["x"] < dest_x and not right_collided:
        phantom["x"] += phantom["speed"]
    elif phantom["x"] > dest_x and not left_collided:
        phantom["x"] -= phantom["speed"]
    elif phantom["y"] < dest_y and not down_collided:
        phantom["y"] += phantom["speed"]
    elif phantom["y"] > dest_y and not up_collided:
        phantom["y"] -= phantom["speed"]

    return phantom
