from config import *
from Exceptions import InvalidPipeCoordinateException
import random


class Pipe:
    GAP = WIN_WIDTH/2.5
    VELOCITY = 5

    def __init__(self, x):
        """
        Pipe only have x value because the height will be random.
        Pipe class is also  both the top pipe and the bottom pipe.
        :param x: double
        """
        if x < 0:
            raise InvalidPipeCoordinateException(f"invalid X coordinate on the __init__ method\nx: {x}")


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
        """
        Sets the height of the top pipe and the bottom pipe
        randomly.
        :return:  nothing
        """
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.GAP


    def update(self):
        self.x -= self.VELOCITY

    def render(self, win):
        win.blit(self.PIPE_TOP, (self.x, self.top))
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))

    def collide(self, bird):
        """
        Implementation of pixel perfect collision using pygame masks.
        :param bird: Bird
        :return: boolean
        """

        # gets the mask of the images
        birdMask = bird.getMask()
        topMask = pygame.mask.from_surface(self.PIPE_TOP)
        bottomMask = pygame.mask.from_surface(self.PIPE_BOTTOM)

        # gets offset
        topOffset = (round(self.x - bird.x), round(self.top - bird.y))
        bottomOffset = (round(self.x - bird.x), round(self.bottom - bird.y))

        # tests if the masks overlap
        bottomOverlapPoint = birdMask.overlap(bottomMask, bottomOffset)
        topOverlapPoint = birdMask.overlap(topMask, topOffset)

        # if there is a collision return true, otherwise false
        return True if bottomOverlapPoint or topOverlapPoint else False

    def isOutOfScreen(self):
        return self.x + self.PIPE_TOP.get_width() < 0

