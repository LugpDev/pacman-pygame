from pygame import *

SIZE = 30


def initialize_powers(screen_width, screen_height):
    sprite = transform.scale(image.load('../assets/lucky-block.jpg'), (SIZE, SIZE))

    return {
        "image": sprite,
        "items": [
            {
                "coords": (25, 25)
            },
            {
                "coords": (screen_width - 25 - SIZE, 25)
            },
            {
                "coords": (25, screen_height - 25 - SIZE)
            },
            {
                "coords": (screen_width - 25 - SIZE, screen_height - 25 - SIZE)
            }
        ]
    }
