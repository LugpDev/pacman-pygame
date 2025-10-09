from pygame import *

WIDTH, HEIGHT = 35, 30

def load_sprite(name):
    sprite = transform.scale(image.load(f'../assets/phantoms/{name}.png'), (WIDTH, HEIGHT))
    return sprite

def create_phantoms():
    return [
        {
        "name": "orange",
        "sprite": load_sprite("orange"),
        "x": 300,
        "y": 300,
        },
        {
            "name": "red",
            "sprite": load_sprite("red"),
            "x": 350,
            "y": 350,
        },
        {
            "name": "pink",
            "sprite": load_sprite("pink"),
            "x": 300,
            "y": 370,
        },
        {
            "name": "blue",
            "sprite": load_sprite("blue"),
            "x": 350,
            "y": 390,
        }
    ]