from game.util import loadImage
from game.GameObject import GameObject
import pygame


class Bird(GameObject):

    # static variables and constants
    MAX_ROTATION = 25
    ROT_VEL = 20
    JUMP_VELOCITY_FACTOR = 6.5

    def __init__(self, win_width, win_height, scale, gravity):
        """
        The corner of the screen is represented by (0, 0).
        If you go down the y direction "self.y" becomes more positive.
        For "self.x" the values behave as the convention.

        :param x: moving to the right becomes more negative, moving to the left more positive
        :param y: if moving upwards becomes more negative, moving downwards more positive
        """
        super().__init__()

        self.GRAVITY = gravity
        self.WIN_WIDTH = win_width
        self.WIN_HEIGHT = win_height
        self.SCALE = scale

        self.IMAGES = [loadImage(self.IMGS_PATH, image, self.SCALE) for image in self.RESOURCE_IMAGES if "bird" in image]

        # initial coordinates are define in function of the size of the window
        self.x = self.WIN_WIDTH / 5
        self.y = self.WIN_HEIGHT - self.WIN_HEIGHT / 2

        self.inclination = 0 # how much the bird must tilt

        self.tick_count = 0 # time reference to use for the physics of the bird
        self.height = self.y
        self.velocity = 0
        self.image_count = 0

        # first image AKA default image
        self.image = self.IMAGES[0]





    def jump(self):
        """
        Sets the velocity of the bird to a initial negative
        value so it starts going upwards and keep track of
        from which height the bird has jumped.
        :return: nothing
        """
        self.velocity = -self.JUMP_VELOCITY_FACTOR*self.SCALE
        self.tick_count = 0

        self.height = self.y




    def update(self):
        """
        updates the coordinates, tilt and tick_count values of the bird.
        :return: nothing
        """

        self.tick_count += 1

        d = self.quadratic_formula(self.tick_count, self.GRAVITY)

        # don't let the bird accelerate forever
        if d >= 16:
            d  = 16

        # if is still going up, go a little further
        # it makes the movement of the bird better
        if d < 0:
             d -= 2

        self.y += d
        self.tilt(d)



    def render(self, win):
        """
        Display the bird on the screen.
        :param win: Window object from pygame.
        :return:
        """
        self.image_count += 1

        if self.image_count > len(self.IMAGES) - 1:
            self.image_count = 0

        self.image = self.IMAGES[self.image_count]

        self.rotate(win)




    def tilt(self, distance):
        """
        tilts the bird depending on how much it is moving
        upwards or downwards each unit of the time.

        :param distance: double -> resulting from the free fall quadratic formula
        :return: nothing
        """

        # while the bird is going up(distance < 0), keep the rotation to the max level
        if distance < 0:
            if self.inclination < self.MAX_ROTATION:
                self.inclination = self.MAX_ROTATION

        # if the bird is going down rotate the bird to point it towards the ground
        else:
            if self.inclination > -90:
                self.inclination -= self.ROT_VEL




    def rotate(self, win):
        """
        Rotates bird around the center and not the left corner.
        :return: nothing
        """
        # rotate the image with conventional pygame function
        rotate_image = pygame.transform.rotate(self.image, self.inclination)

        # redefines the rectangle of the rotated image
        new_rect = rotate_image.get_rect(
            center=self.image.get_rect(topleft = (self.x, self.y)).center)

        win.blit(rotate_image, new_rect.topleft)




    def quadratic_formula(self, time, gravity):
        """
        Computes how much space the bird is moving each unit
        of time.
        Original quadratic formula:
        delta_space = velocity*time - (GRAVITY/2)*time²
        :return: double
        """
        return self.velocity*time + (gravity / 2) * time**2




    def getMask(self):
        """
        Get the mask object of the current image of the bird.
        :return: Mask object from pygame
        """
        return pygame.mask.from_surface(self.image)
