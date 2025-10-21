from pygame import *


def initialize_ui():
    my_font = font.SysFont('menlo', 30)
    return my_font


def ui_controller(my_font, screen, playing, lost, game_over):
    if not playing:
        if lost:
            content = "Game Over!"
        elif not game_over:
            content = "Press space to start playing..."

        text = my_font.render(content, True, (255, 255, 255))
        text_rect = text.get_rect(center=(700 / 2, 781 / 2))

        screen.blit(text, text_rect)


def show_power_ui(screen, powers):
    draw.circle(screen, (255, 255, 255), (70, 290), 35, 2)
    key_image = transform.scale(image.load("../assets/e_key.png"), (30, 30))
    screen.blit(key_image, (20, 290 - 15))

    if powers["has_power"]:
        screen.blit(transform.scale(powers["shell"], (40, 42)), (70 - 20, 290 - 21))
