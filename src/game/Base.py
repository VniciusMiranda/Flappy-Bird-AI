from game.util import loadImage
from game.GameObject import GameObject


class Base(GameObject):
    VELOCITY = 5

    def __init__(self,win_height, scale):
        """
        Represents the base of the game, will be moving as
        well, so this class is for encapsulating the methods
        for moving and testing collision.
        Had an Hard time figuring out if this was really needed
        but I think it was the right decision :).
        :param y: double or integer
        """
        super().__init__()

        self.y = win_height - win_height / 14

        self.SCALE = scale
        self.IMAGE = loadImage(self.IMGS_PATH, "base.png",self.SCALE)
        self.WIDTH = self.IMAGE.get_width()

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

    def collide(self, bird):
        """
        Collision testing with the bird and the base and the ceiling.
        :param bird: Bird
        :return: boolean
        """
        return bird.image.get_height() + bird.y > self.y or bird.y < 0
