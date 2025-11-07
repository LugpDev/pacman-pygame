from pygame import *


class SoundController:
    def __init__(self):
        self.start_music = mixer.Sound("../assets/audio/background_music.mp3")
        self.start_music.set_volume(0.3)

        self.siren_sound = mixer.Sound("../assets/audio/ghost_siren.mp3")
        self.siren_sound.set_volume(0.1)
        self.siren_channel = mixer.Channel(1)

        self.lose_sound = mixer.Sound("../assets/audio/lose.mp3")
        self.lose_sound.set_volume(0.3)
        self.lose_channel = mixer.Channel(2)

        self.powerup_sound = mixer.Sound("../assets/audio/powerup.mp3")
        self.powerup_channel = mixer.Channel(3)

        self.hit_sound = mixer.Sound("../assets/audio/hit.mp3")
        self.hit_channel = mixer.Channel(4)

    def play_start_music(self):
        self.start_music.play()