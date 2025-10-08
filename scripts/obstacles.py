def initialize_obstacles(screen_width, screen_height):
    # (x1, y1, x1+x2, y1+y2)
    return [
        # Borders
        (0, 0, screen_width, 13),  # Top
        (0, 0, 13, 250),  # Top Left
        (screen_width - 13, 0, 13, 250),  # Top Right
        (0, 240, 140, 100),  # Top Middle Left
        (screen_width - 140, 240, 140, 100),  # Top Middle Right
        (0, 390, 140, 100),  # Bottom Middle Left
        (screen_width - 140, 390, 140, 100),  # Bottom Middle Right
        (0, screen_height - 300, 13, 300),  # Bottom Left
        (screen_width - 13, screen_height - 300, 13, screen_height),  # Bottom Right
        (0, screen_height - 13, screen_width, screen_height),  # Bottom

        # Obstacles       Shape

        # 1° row
        (338, 0, 25, 113),  # |
        (63, 63, 77, 50),  # [==]
        (188, 63, 99, 50),  # [==]
        (414, 63, 99, 50),  # [==]
        (560, 63, 78, 50),  # [==]

        # 2° row
        (63, 163, 77, 26),  # --
        (260, 163, 180, 26),  # --
        (560, 163, 78, 26),  # --
        (338, 189, 25, 75),  # |
        (188, 163, 27, 177),  # |
        (215, 238, 73, 26),  # --
        (486, 163, 27, 177),  # |
        (413, 238, 73, 26),  # --

        # 3° row
        (188, 390, 27, 100),  # |
        (486, 390, 27, 100),  # |
        (260, 464, 180, 26),  # --
        (338, 490, 25, 76),  # |

        # 4° row
        (63, 540, 77, 26),  # --
        (188, 540, 99, 26),  # --
        (414, 540, 99, 26),  # --
        (560, 540, 77, 26),  # --

    ]
