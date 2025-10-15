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
            "priority": "x",
            "width": WIDTH,
            "height": HEIGHT,
        },
        {
            "name": "red",
            "sprite": load_sprite("red"),
            "x": 370,
            "y": 270,
            "speed": speed,
            "priority": "y",
            "width": WIDTH,
            "height": HEIGHT,
        },
        {
            "name": "pink",
            "sprite": load_sprite("pink"),
            "x": 70,
            "y": 350,
            "speed": speed,
            "priority": "y",
            "width": WIDTH,
            "height": HEIGHT,
        },
        {
            "name": "blue",
            "sprite": load_sprite("blue"),
            "x": 600,
            "y": 350,
            "speed": speed,
            "priority": "x",
            "width": WIDTH,
            "height": HEIGHT,
        }
    ]


def get_phantom_collision(phantom, obstacles, angle):
    collided = check_collision(obstacles, WIDTH, HEIGHT, phantom["x"], phantom["y"], phantom["speed"], angle)
    return collided


def check_pacman_collision(phantom, pacman):
    pacman_rect = (pacman["x"], pacman["y"], 30, 30)
    angles = [0, 90, 180, 270]
    return any(
        check_collision([pacman_rect], WIDTH, HEIGHT, phantom["x"], phantom["y"], 0, angle)
        for angle in angles
    )


def update_phantom(phantom, dest, obstacles, playing):
    if not playing:
        return phantom

    dest_x, dest_y = dest[0], dest[1]

    right_collided = get_phantom_collision(phantom, obstacles, 0)
    up_collided = get_phantom_collision(phantom, obstacles, 90)
    left_collided = get_phantom_collision(phantom, obstacles, 180)
    down_collided = get_phantom_collision(phantom, obstacles, 270)

    if phantom["priority"] == "x":
        if phantom["x"] < dest_x and not right_collided:
            phantom["x"] += phantom["speed"]
        elif phantom["x"] > dest_x and not left_collided:
            phantom["x"] -= phantom["speed"]
        elif phantom["y"] < dest_y and not down_collided:
            phantom["y"] += phantom["speed"]
        elif phantom["y"] > dest_y and not up_collided:
            phantom["y"] -= phantom["speed"]
        else:
            phantom["priority"] = "y"
    else:
        if phantom["y"] > dest_y and not up_collided:
            phantom["y"] -= phantom["speed"]
        elif phantom["y"] < dest_y and not down_collided:
            phantom["y"] += phantom["speed"]
        elif phantom["x"] > dest_x and not left_collided:
            phantom["x"] -= phantom["speed"]
        elif phantom["x"] < dest_x and not right_collided:
            phantom["x"] += phantom["speed"]
        else:
            phantom["priority"] = "x"

    return phantom
