def initialize_obstacles(screen_width, screen_height):
    # (x1, y1, x2, y1+y2)
    return [
        # Borders
        (0, 0, screen_width, 13), # Top
        (0, 0, 13, 250), # Top Left
        (screen_width - 13, 0, screen_width, 250), # Top Right
        (0, 240, 140, 100), # Top Middle Left
        (screen_width - 140, 240, screen_width, 100), # Top Middle Right
        (0, 390, 140, 100), # Bottom Middle Left
        (screen_width - 140, 390, screen_width, 100), # Bottom Middle Right
        (0, screen_height-300, 13, 300), # Bottom Left
        (screen_width - 13, screen_height-300, screen_width, screen_height), # Bottom Right
        (0, screen_height - 13, screen_width, screen_height),  # Bottom
    ]
