import pygame

class Score:

    def __init__(self, initialValue, font, size, win_width):
        self.WIN_WIDTH = win_width
        self.value = initialValue
        self.font = pygame.font.SysFont(font, size)

    def render(self, win):
        """
        Draws the score to the screen.
        :param win: Window
        :return: nothing
        """
        text = self.font.render(f"score: {self.value}", 1, (255,255,255))
        win.blit(text, (self.WIN_WIDTH - 10 - text.get_width(), 10))

    def update(self):
        """
        Updates the score value
        :return: nothing
        """
        self.value += 1