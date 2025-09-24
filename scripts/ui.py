from pygame import *

def initialize_ui():
    my_font = font.SysFont('menlo', 30)
    return my_font

def ui_controller(my_font, screen, playing):
    if not playing:
        texto = my_font.render("Press space to start playing...", True, (255, 255, 255))
        screen.blit(texto, (100, 350))

