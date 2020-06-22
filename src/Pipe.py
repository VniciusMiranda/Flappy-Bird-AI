from config import *
import random


class Pipe:
    GAP = WIN_WIDTH/2
    VELOCITY = 5

    def __init__(self, x):
        """
        Pipe only have x value because the height will be random
        :param x: double
        """
        self.x = x
        self.height = 0

        self.top = 0
        self.bottom = 0
        # flips the original image
        self.PIPE_TOP = pygame.transform.flip(PIPE_IMG, False, True)
        self.PIPE_BOTTOM = PIPE_IMG

        self.passed = False
        self.setHeight()

    def setHeight(self):
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP


    def move(self):
        self.x -= self.VELOCITY

    def draw(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))
