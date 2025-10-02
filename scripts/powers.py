from pygame import *

SIZE = 30


def initialize_powers(screen_width, screen_height):
    sprite = transform.scale(image.load('../assets/lucky-block.jpg'), (SIZE, SIZE))
    shell = image.load('../assets/shell.png')

    return {
        "image": sprite,
        "shell": shell,
        "has_power": False,
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


def use_power(powers):
    if powers["has_power"]:
        print("using power...")
        powers["has_power"] = False