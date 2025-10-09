def check_collision(obstacles, width, height, x, y, speed, angle):
    for obstacle in obstacles:
        if angle == 0:  # Right
            collided_y = y in range(obstacle[1] - height, obstacle[3] + obstacle[1])
            collided_x = x + width + speed in range(obstacle[0], obstacle[2] + obstacle[0])
        elif angle == 90:  # Up
            collided_y = y - speed in range(obstacle[1], obstacle[3] + obstacle[1])
            collided_x = x in range(obstacle[0] - width, obstacle[2] + obstacle[0])
        elif angle == 180:  # Left
            collided_y = y in range(obstacle[1] - height, obstacle[3] + obstacle[1])
            collided_x = x - speed in range(obstacle[0], obstacle[2] + obstacle[0])
        elif angle == 270:  # Down
            collided_y = y + speed + height in range(obstacle[1], obstacle[3] + obstacle[1])
            collided_x = x in range(obstacle[0] - width, obstacle[2] + obstacle[0])
        else:
            continue

        if collided_y and collided_x:
            return True
    return False
