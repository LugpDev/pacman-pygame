from pygame import *
import sys

from pacman.create_pacman import *
from pacman.draw_pacman import *
from pacman.handle_pacman_input import *
from pacman.update_pacman import *

from phantoms import create_phantoms, update_phantom, check_pacman_collision

from scripts.obstacles import initialize_obstacles
from scripts.powers import initialize_powers, power_collision, use_power, update_shell
from scripts.sound import initialize_sound, play_start_music
from models.ui_controller import UIController

init()

sound_controller = initialize_sound()
ghost_channel = sound_controller["ghost_channel"]
ghost_siren = sound_controller["ghost_siren"]
lose_channel = sound_controller["lose_channel"]
lose_sound = sound_controller["lose_sound"]
powerup_channel = sound_controller["powerup_channel"]
powerup_sound = sound_controller["powerup_sound"]
hit_channel = sound_controller["hit_channel"]
hit_sound = sound_controller["hit_sound"]

SCREEN_WIDTH, SCREEN_HEIGHT = 700, 781
screen = display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = time.Clock()
ui_controller = UIController(screen)
obstacles = initialize_obstacles(SCREEN_WIDTH, SCREEN_HEIGHT)
powers = initialize_powers(SCREEN_WIDTH, SCREEN_HEIGHT, powerup_channel, powerup_sound, hit_channel, hit_sound)
pacman = create_pacman(335, 580, 2, SCREEN_WIDTH, SCREEN_HEIGHT, obstacles)
phantoms = create_phantoms(speed=1)

playing = False
lost = False
lose_played = False

play_start_music()

# pellets
PELLET_RADIUS = 3

pellets = []

# horizontales (filas)
# cada tupla es (inicio_x, fin_x, y)

i1, f1 = 40.5, 42
i2, f2 = 79.5, 81
i3, f3 = 118.5, 120
i4, f4 = 157.5, 160
i5, f5 = 196.5, 198
i6, f6 = 235.5, 240
i7, f7 = 274.5, 276
i8, f8 = 313.5, 315
i9, f9 = 352.5, 355
i10, f10 = 391.5, 395
i11, f11 = 430.5, 432
i12, f12 = 469.5, 475
i13, f13 = 508.5, 510
i14, f14 = 547.5, 550
i15, f15 = 586.5, 590
i16, f16 = 625.5, 628
i17, f17 = 664.5, 670

# alturas
h1 = 39.5
h2 = 86.9
h3 = 136
h4 = 175
h5 = 215
h6 = 255
h7 = 292
h8 = 330
h9 = 365
h10 = 405
h11 = 440
h12 = 475
h13 = 515
h14 = 550
h15 = 590
h16 = 628
h17 = 670
h18 = 705
h19 = 740

horizontal = [
    (i1, f8, h1),  # fila 1
    (i10, f17, h1),  # fila 1

    (i1, f1, h2),  # punto 1
    (i4, f4, h2),  # punto 4
    (i8, f8, h2),  # punto 8
    (i10, f10, h2),  # punto 10
    (i14, f14, h2),  # punto 14
    (i17, f17, h2),  # punto 17

    (i1, f17, h3),  # fila 3

    (i1, f1, h4),  # punto 1
    (i4, f4, h4),  # punto 4
    (i6, f6, h4),  # punto 6
    (i12, f12, h4),  # punto 12
    (i14, f14, h4),  # punto 14
    (i17, f17, h4),  # punto 17

    (i1, f4, h5),  # 1-4
    (i6, f8, h5),  # 6-8
    (i10, f12, h5),  # 10-12
    (i14, f17, h5),  # 14-17

    (i4, f4, h6),  # punto 4
    (i8, f8, h6),  # punto 8
    (i10, f10, h6),  # punto 10
    (i14, f14, h6),  # punto 14

    (i4, f4, h7),  # punto 4
    (i6, f8, h7),  # 6-8
    (i10, f12, h7),  # 10-12
    (i14, f14, h7),  # 14

    (i4, f4, h8),  # punto 4
    (i6, f6, h8),  # punto 6
    (i12, f12, h8),  # punto 12
    (i14, f14, h8),  # punto 14

    (i1, f6, h9),  # 9 mitad
    (i12, f17, h9),  # 9 mitad

    (i6, f6, h10),  # punto 6
    (i12, f12, h10),  # punto 12
    (i4, f4, h10),  # punto 4
    (i14, f14, h10),  # punto 14

    (i6, f12, h11),  # punto 6-12
    (i4, f4, h11),  # punto 4
    (i14, f14, h11),  # punto 14

    (i4, f4, h12),  # punto 4
    (i14, f14, h12),  # punto 14
    (i6, f6, h12),  # punto 6
    (i12, f12, h12),  # punto 12

    (i10, f17, h13),  # punto 10-17
    (i1, f8, h13),  # punto 1-8

    (i4, f4, h14),  # punto 4
    (i14, f14, h14),  # punto 14
    (i8, f8, h14),  # punto 8
    (i10, f10, h14),  # punto 10
    (i1, f1, h14),  # punto 1
    (i17, f17, h14),  # punto 17

    (i4, f14, h15),  # punto 4-14
    (i1, f2, h15),  # punto 4-14
    (i16, f17, h15),  # punto 4-14

    (i4, f4, h16),  # punto 4
    (i2, f2, h16),  # punto 14
    (i6, f6, h16),  # punto 6
    (i14, f14, h16),  # punto 14
    (i12, f12, h16),  # punto 12
    (i16, f16, h16),  # punto 16

    (i1, f4, h17),  # 1-4
    (i6, f8, h17),  # 6-8
    (i10, f12, h17),  # 10-12
    (i14, f17, h17),  # 14-17

    (i1, f1, h18),  # punto 1
    (i8, f8, h18),  # punto 8
    (i10, f10, h18),  # punto 10
    (i17, f17, h18),  # punto 17

    (i1, f17, h19),  # última

]

for start_x, end_x, y in horizontal:
    x = start_x
    while x < end_x:
        pellets.append({"x": x, "y": y})
        x += 39

score = 0
game_over = False

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

    for p in pellets:
        draw.circle(screen, (255, 255, 0), (p["x"], p["y"]), PELLET_RADIUS)

    if playing and not game_over:
        new_pellets = []
        for p in pellets:
            pac_x = pacman["x"] + 10
            pac_y = pacman["y"] + 10

            dx = pac_x - p["x"]
            dy = pac_y - p["y"]
            distance = (dx * dx + dy * dy) ** 0.5

            if distance < 20:
                score += 1
            else:
                new_pellets.append(p)
        pellets = new_pellets

        if len(pellets) == 0:
            game_over = True
            playing = False


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
    ui_controller.draw_score(score)
    ui_controller.draw_message_ui(playing, lost, game_over)
    ui_controller.draw_power_ui(powers["has_power"])

    if playing:
        if not ghost_channel.get_busy():
            ghost_channel.play(ghost_siren, loops=-1)
    else:
        ghost_channel.stop()
        if lost and not lose_played:
            lose_played = True
            lose_channel.play(lose_sound)

    display.flip()
    clock.tick(60)
