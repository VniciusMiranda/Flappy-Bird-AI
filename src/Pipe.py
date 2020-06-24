from Exceptions import InvalidPipeCoordinateException
from GameObject import GameObject
from util import loadImage
import pygame
import random


class Pipe(GameObject):
    VELOCITY = 5

    def __init__(self, win_width, scale, factor=0):
        """
        Pipe only have x value because the height will be random.
        Pipe class is also  both the top pipe and the bottom pipe.
        :param x: double
        """
        super().__init__()

        self.SCALE = scale

        self.PIPE_IMG = loadImage(self.IMGS_PATH, "", self.SCALE)
        if x < 0:
            raise InvalidPipeCoordinateException(f"invalid X coordinate on the __init__ method\nx: {x}")

        self.WIN_WIDTH = win_width

        self.GAP = self.WIN_WIDTH/2.5

        # if the initial distance of the pipe needs tp be bigger than the window width
        # the variable factor is passed
        self.x = self.WIN_WIDTH + factor*(self.WIN_WIDTH / 1.5)
        self.height = 0

        self.top = 0
        self.bottom = 0
        # flips the original image
        self.PIPE_TOP = pygame.transform.flip(self.PIPE_IMG, False, True)

        self.PIPE_BOTTOM = self.PIPE_IMG

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
        """

        :return: nothing
        """
        self.x -= self.VELOCITY




    def render(self, win):
        """

        :param win: Window
        :return: nothing
        """
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

