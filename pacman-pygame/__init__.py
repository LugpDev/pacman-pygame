from pygame import *
import sys

from pacman.create_pacman import *
from pacman.draw_pacman import *
from pacman.handle_pacman_input import *
from pacman.update_pacman import *

from phantoms import create_phantoms, update_phantom, check_pacman_collision

from scripts.obstacles import initialize_obstacles
from scripts.powers import initialize_powers, power_collision, use_power, update_shell
from scripts.ui import initialize_ui, ui_controller, show_power_ui

init()
SCREEN_WIDTH, SCREEN_HEIGHT = 700, 781
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = time.Clock()
ui_font = initialize_ui()
obstacles = initialize_obstacles(SCREEN_WIDTH, SCREEN_HEIGHT)
powers = initialize_powers(SCREEN_WIDTH, SCREEN_HEIGHT)
pacman = create_pacman(335, 580, 2, SCREEN_WIDTH, SCREEN_HEIGHT, obstacles)
phantoms = create_phantoms(speed=1)

background_music = mixer.Sound("../assets/audio/background_music.mp3")
ghost_siren = mixer.Sound("../assets/audio/ghost_siren.mp3")
lose_sound = mixer.Sound("../assets/audio/lose.mp3")
background_music.set_volume(0.5)
ghost_siren.set_volume(0.5)
lose_sound.set_volume(0.5)
ghost_channel = mixer.Channel(1)
lose_channel = mixer.Channel(2)

playing = False
lost = False
lose_played = False

background_music.play()

while True:
    screen.fill((0, 0, 0))
    for e in event.get():
        if e.type == QUIT:
            sys.exit()
        elif e.type == KEYDOWN:
            if playing:
                pacman = handle_pacman_input(pacman, e.key)

                if e.key == K_e:
                    use_power(powers, pacman)

            elif not lost and e.key == K_SPACE:
                playing = True

    map = transform.scale(image.load("../assets/map.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(map, (0, 0))

    for power in powers["items"]:
        screen.blit(powers["image"], (power["x"], power["y"]))
        power_collision(powers, pacman["x"], pacman["y"])

    for phantom in phantoms:
        screen.blit(phantom["sprite"], (phantom["x"], phantom["y"]))
        update_phantom(phantom, (pacman["x"], pacman["y"]), obstacles, playing)
        collided = check_pacman_collision(phantom, pacman)

        if collided:
            playing = False
            lost = True

    pacman = update_pacman(pacman, playing)
    draw_pacman(pacman, screen, playing)

    phantoms = update_shell(powers, phantoms, obstacles, screen)

    ui_controller(ui_font, screen, playing, lost)
    show_power_ui(screen, powers)

    if playing:
        if not ghost_channel.get_busy():
            ghost_channel.play(ghost_siren, loops=-1)
            ghost_channel.set_volume(0.5)
    else:
        ghost_channel.stop()

        if lost and not lose_played:
            lose_played = True
            lose_channel.play(lose_sound)

    display.flip()
    clock.tick(60)
