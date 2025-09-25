def initialize_obstacles(screen_width, screen_height):
    # [x1, y1, x2, y2]
    return [
        #(0, 0, 13, 250),
        (screen_width -13 , 0, screen_width, 250),
        (screen_width - 13, screen_height-300, screen_width, screen_height-50),
        (0, 0, screen_width, 13),
        (0, screen_height-13, screen_width, screen_height)
    ]
