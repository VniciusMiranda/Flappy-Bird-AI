from config import *

class Base:
    VELOCITY = 5
    IMAGE = BASE_IMG
    WIDTH = IMAGE.get_width()

    def __init__(self, y):
        """
        Represents the base of the game, will be moving as
        well, so this class is for encapsulating the methods
        for moving and testing collision.
        Had an Hard time figuring out if this was really needed
        but I think it was the right decision :).
        :param y: double or integer
        """
        self.y = y

        self.x1 = 0
        self.x2 = self.WIDTH

    def update(self):
        """
        Updates the coordinates and states if there are any.
        :return: nothing
        """
        # moves the base
        self.x1 -= self.VELOCITY
        self.x2 -= self.VELOCITY

        # if the base is out off the screen, moves it back
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH


    def render(self, win):
        """
        Draws the Base to the screen.
        :param win: Window object of pygame
        :return: nothing
        """
        win.blit((self.IMAGE), (self.x1, self.y))
        win.blit((self.IMAGE), (self.x2, self.y))

    def collided(self, bird):
        """
        Collision testing with the bird and the base.
        :param bird: Bird
        :return: boolean
        """
        return bird.image.get_height() + bird.y > self.y
