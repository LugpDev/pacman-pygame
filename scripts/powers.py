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
                "used": False,
                "coords": (25, 25)
            },
            {
                "used": False,
                "coords": (screen_width - 25 - SIZE, 25)
            },
            {
                "used": False,
                "coords": (25, screen_height - 25 - SIZE)
            },
            {
                "used": False,
                "coords": (screen_width - 25 - SIZE, screen_height - 25 - SIZE)
            }
        ]
    }


def power_collision(powers, pacman_x, pacman_y):
    for power in powers["items"]:
        x = power["coords"][0]
        y = power["coords"][1]

        if power["used"]:
            return

        if pacman_x in range(x - SIZE, x + SIZE) and pacman_y in range(y - SIZE, y + SIZE):
            power["used"] = True
            powers["has_power"] = True


def use_power(powers):
    if powers["has_power"]:
        print("using power...")
        powers["has_power"] = False