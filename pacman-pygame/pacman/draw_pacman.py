from scripts.animations import show_animation


def draw_pacman(pacman, surface, playing):
    if playing:
        show_animation(
            [pacman["images"][pacman["frame_index"]]], 1,
            surface, pacman["x"], pacman["y"]
        )
    else:
        surface.blit(pacman["images"][0], (pacman["x"], pacman["y"]))
