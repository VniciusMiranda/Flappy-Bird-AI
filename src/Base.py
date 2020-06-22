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

        # the
        self.x1 = 0
        self.x2 = self.WIDTH

    def update(self):
        """
        Updates the coordinates and states if there are any.
        :return: nothing
        """
        pass
