from config import *

class Score:

    def __init__(self, initialValue, font, size):
        self.value = initialValue
        self.font = pygame.font.SysFont(font, size)

    def render(self, win):
        text = self.font.render(f"score: {self.value}", 1, (255,255,255))
        win.blit(text, (WIN_WIDTH - 10 - text.get_width(), 10))