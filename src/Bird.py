from .config import BIRD_IMGS, GRAVITY

import pygame

class Bird:

    # static variables and constants
    IMAGES = BIRD_IMGS
    MAX_ROTATION = 25
    ROT_VEL = 20
    ANIMATION_VEL = 5

    def __init__(self, x, y):
        """
        The corner of the screen is represented by (0, 0).
        If you go down the y direction "self.y" becomes more positive.
        For "self.x" the values behave as the convention.

        :param x: moving to the right becomes more negative, moving to the left more positive
        :param y: if moving upwards becomes more negative, moving downwards more positive
        """
        # coordinates
        self.x = x
        self.y = y

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
        self.velocity = -10.5
        self.tick_count = 0

        self.height = self.y




    def update(self):
        """
        updates the coordinates, tilt and tick_count values of the bird.
        :return: nothing
        """
        self.tick_count += 1

        d = self.quadratic_formula()
        self.y += d

        self.tilt(d)




    def render(self, win):
        """
        Display the bird on the screen.
        :param win: Window object from pygame module.
        :return:
        """
        if self.tick_count % 10 == 0:
            self.image_count += 1

        if self.image_count > len(BIRD_IMGS):
            self.image_count = 0

        rotation = self.rotate()

        win.blit(rotation["rotatedImage"], rotation["rect"])




    def tilt(self, distance):
        """
        tilts the bird depending on how much it is moving
        upwards or downwards each unit of the time.

        :param distance: double -> resulting from the free fall quadratic formula
        :return: nothing
        """
        if distance < 0:
            if self.inclination < self.MAX_ROTATION:
                self.inclination = self.MAX_ROTATION

        else:
            if self.inclination > -90:
                self.inclination -= self.ROT_VEL




    def rotate(self):
        """
        Rotates bird around the center and not the left corner.
        :return: nothing
        """
        # rotate the image with conventional pygame function
        rotate_image = pygame.transform.rotate(self.image, self.inclination)

        # redefines the rectangle of the rotated image
        new_rect = rotate_image.get_rect(
            center=self.image.get_rect(topLeft = (self.x, self.y)).center)

        return {"rotatedImage": rotate_image, "rect": new_rect}




    def quadratic_formula(self):
        """
        Computes how much space the bird is moving each unit
        of time.
        Original quadratic formula:
        delta_space = velocity*time - (GRAVITY/2)*time²
        :return: double
        """
        return self.velocity * self.tick_count + (GRAVITY / 2) * self.tick_count ** 2




    def getMask(self):
        return pygame.mask.from_surface(self.image)
