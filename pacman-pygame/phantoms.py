from pygame import *

WIDTH, HEIGHT = 35, 30


def load_sprite(name):
    sprite = transform.scale(image.load(f'../assets/phantoms/{name}.png'), (WIDTH, HEIGHT))
    return sprite


def create_phantoms(speed):
    return [
        {
            "name": "orange",
            "sprite": load_sprite("orange"),
            "x": 300,
            "y": 300,
            "speed": speed,
        },
        {
            "name": "red",
            "sprite": load_sprite("red"),
            "x": 350,
            "y": 350,
            "speed": speed,
        },
        {
            "name": "pink",
            "sprite": load_sprite("pink"),
            "x": 300,
            "y": 370,
            "speed": speed,
        },
        {
            "name": "blue",
            "sprite": load_sprite("blue"),
            "x": 350,
            "y": 390,
            "speed": speed,
        }
    ]


def update_phantom(phantom, dest, obstacles, playing):
    if not playing:
        return phantom

    dest_x, dest_y = dest[0], dest[1]

    if phantom["x"] < dest_x:
        phantom["x"] += phantom["speed"]
    elif phantom["x"] > dest_x:
        phantom["x"] -= phantom["speed"]
    elif phantom["y"] < dest_y:
        phantom["y"] += phantom["speed"]
    elif phantom["y"] > dest_y:
        phantom["y"] -= phantom["speed"]

    return phantom
