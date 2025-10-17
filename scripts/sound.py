from pygame import *


def initialize_sound():
    ghost_siren = mixer.Sound("../assets/audio/ghost_siren.mp3")
    ghost_siren.set_volume(0.1)
    ghost_channel = mixer.Channel(1)

    lose_sound = mixer.Sound("../assets/audio/lose.mp3")
    lose_sound.set_volume(0.3)
    lose_channel = mixer.Channel(2)

    powerup_sound = mixer.Sound("../assets/audio/powerup.mp3")
    powerup_channel = mixer.Channel(3)

    hit_sound = mixer.Sound("../assets/audio/hit.mp3")
    hit_channel = mixer.Channel(4)

    return {
        "ghost_siren": ghost_siren,
        "ghost_channel": ghost_channel,
        "lose_sound": lose_sound,
        "lose_channel": lose_channel,
        "powerup_sound": powerup_sound,
        "powerup_channel": powerup_channel,
        "hit_sound": hit_sound,
        "hit_channel": hit_channel,
    }


def play_start_music():
    start_music = mixer.Sound("../assets/audio/background_music.mp3")
    start_music.set_volume(0.3)
    start_music.play()
