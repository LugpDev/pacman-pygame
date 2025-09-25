PACMAN_SIZE = 30

def check_collision(pacman):
    for obstacle in pacman["obstacles"]:
        if pacman["angle"] == 0:  # Right
            collided_y = pacman["y"] in range(obstacle[1], obstacle[3])
            collided_x = pacman["x"] + PACMAN_SIZE + pacman["speed"] in range(obstacle[0], obstacle[2])
        elif pacman["angle"] == 90:  # Up
            collided_y = pacman["y"] - pacman["speed"] in range(obstacle[1], obstacle[3])
            collided_x = pacman["x"] + PACMAN_SIZE in range(obstacle[0], obstacle[2])
        elif pacman["angle"] == 180:  # Left
            collided_y = pacman["y"] in range(obstacle[1], obstacle[3])
            collided_x = pacman["x"] - pacman["speed"] in range(obstacle[0], obstacle[2])
        elif pacman["angle"] == 270:  # Down
            collided_y = pacman["y"] + pacman["speed"] + PACMAN_SIZE in range(obstacle[1], obstacle[3])
            collided_x = pacman["x"] + PACMAN_SIZE in range(obstacle[0], obstacle[2])
        else:
            continue

        if collided_y and collided_x:
            return True
    return False