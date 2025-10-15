from pygame import *

from scripts.check_collision import check_collision

SIZE = 30
SPEED = 5


def initialize_powers(screen_width, screen_height):
    sprite = transform.scale(image.load('../assets/lucky-block.jpg'), (SIZE, SIZE))
    shell = image.load('../assets/shell.png')

    return {
        "image": sprite,
        "shell": shell,
        "has_power": False,
        "shell_data": {
            "active": False,
            "x": -1,
            "y": -1,
            "angle": -1,
        },
        "items": [
            {
                "x": 25,
                "y": 25,
            },
            {
                "x": screen_width - 25 - SIZE,
                "y": 25,
            },
            {
                "x": 25,
                "y": screen_height - 25 - SIZE,
            },
            {
                "x": screen_width - 25 - SIZE,
                "y": screen_height - 25 - SIZE,
            }
        ]
    }


def power_collision(powers, pacman_x, pacman_y):
    for power in powers["items"]:
        x = power["x"]
        y = power["y"]

        if pacman_x in range(x - SIZE, x + SIZE) and pacman_y in range(y - SIZE, y + SIZE):
            powers["items"].remove(power)
            powers["has_power"] = True


def use_power(powers, pacman):
    if powers["has_power"] and not powers["shell_data"]["active"]:
        powers["shell_data"]["active"] = True
        powers["shell_data"]["x"] = pacman["x"]
        powers["shell_data"]["y"] = pacman["y"]
        powers["shell_data"]["angle"] = pacman["angle"]
        powers["has_power"] = False


def update_shell(powers, phantoms, obstacles, screen):
    if not powers["shell_data"]["active"]:
        return phantoms

    x = powers["shell_data"]["x"]
    y = powers["shell_data"]["y"]
    angle = powers["shell_data"]["angle"]

    collided = check_collision(obstacles, SIZE, SIZE, x, y, SPEED, angle)

    phantoms_obstacles = []
    for phantom in phantoms:
        phantoms_obstacles.append((phantom["x"], phantom["y"], phantom["width"], phantom["height"]))

    phantom_collided = check_collision(phantoms_obstacles, SIZE, SIZE, x, y, SPEED, angle)

    if collided:
        powers["shell_data"]["active"] = False
    elif phantom_collided:
        for phantom in phantoms:
            if phantom["x"] == phantom_collided[0] and phantom["y"] == phantom_collided[1]:
                phantoms.remove(phantom)
        powers["shell_data"]["active"] = False
    else:
        if angle == 0:
            powers["shell_data"]["x"] += SPEED

            if x >= 800:
                powers["shell_data"]["x"] = 0
        elif angle == 90:
            powers["shell_data"]["y"] -= SPEED
        elif angle == 180:
            powers["shell_data"]["x"] -= SPEED

            if x <= 0:
                powers["shell_data"]["x"] = 700
        else:
            powers["shell_data"]["y"] += SPEED
        screen.blit(transform.scale(powers["shell"], (SIZE, SIZE)), (x, y))

    return phantoms
