from pygame import *

from scripts.check_collision import *

SIZE = 30
MOVES = {
    0: ("x", 1),
    90: ("y", -1),
    180: ("x", -1),
    270: ("y", 1),
}


def update_pacman(pacman, playing):
    angle = pacman["angle"]
    speed = pacman["speed"] if playing else 0

    axis, direction = MOVES.get(angle, (None, None))
    if axis is not None:
        # Teletransporte horizontal
        if angle == 0 and pacman["x"] >= pacman["screen_width"]:
            pacman["x"] = 0
        elif angle == 180 and pacman["x"] <= 0:
            pacman["x"] = pacman["screen_width"]
        # Movimiento normal con control de colisión
        elif not check_collision(
                pacman["obstacles"], SIZE, SIZE,
                pacman["x"], pacman["y"], pacman["speed"], angle
        ):
            pacman[axis] += direction * speed

    now = time.get_ticks()
    if now - pacman["last_update"] > 1000 // pacman["anim_fps"]:
        pacman["frame_index"] = (pacman["frame_index"] + 1) % len(pacman["images"])
        pacman["last_update"] = now
    return pacman
