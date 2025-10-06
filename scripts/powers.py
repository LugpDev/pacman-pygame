from pygame import *

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
        powers["shell_data"]["x"] = pacman["x"] - 5
        powers["shell_data"]["y"] = pacman["y"] - 10
        powers["shell_data"]["angle"] = pacman["angle"]
        powers["has_power"] = False


def update_shell(powers, screen):
    if not powers["shell_data"]["active"]:
        return

    x = powers["shell_data"]["x"]
    y = powers["shell_data"]["y"]
    angle = powers["shell_data"]["angle"]

    if angle == 0:
        powers["shell_data"]["x"] += SPEED
    elif angle == 90:
        powers["shell_data"]["y"] -= SPEED
    elif angle == 180:
        powers["shell_data"]["x"] -= SPEED
    else:
        powers["shell_data"]["y"] += SPEED

    screen.blit(transform.scale(powers["shell"], (40, 42)), (x, y))
