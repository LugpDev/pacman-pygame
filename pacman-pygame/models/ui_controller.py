from pygame import *


class UIController:
    def __init__(self, screen):
        self.font = font.SysFont('menlo', 30)
        self.screen = screen
        self.key_image = transform.scale(image.load("../assets/e_key.png"), (30, 30))
        self.shell_image = transform.scale(image.load("../assets/shell.png"), (40, 42))

    def draw_power_ui(self, has_power):
        draw.circle(self.screen, (255, 255, 255), (70, 290), 35, 2)
        self.screen.blit(self.key_image, (20, 290 - 15))

        if has_power:
            self.screen.blit(self.shell_image, (70 - 20, 290 - 21))

    def draw_ui(self, playing, lost, game_over):
        if not playing:
            if lost:
                content = "Game Over!"
            elif game_over:
                content = "¡Ganaste! 🏆"
            else:
                content = "Press space to start playing..."

            text = self.font.render(content, True, (255, 255, 255))
            text_rect = text.get_rect(center=(700 / 2, 781 / 2))

            self.screen.blit(text, text_rect)
