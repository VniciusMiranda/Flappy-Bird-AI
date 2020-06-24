from util import loadImage

import os
import pygame


"""
In this file all the configuration of the constant values is made.
"""
pygame.init()
pygame.font.init()

# path variables



FPS = 23
CLOCK = pygame.time.Clock()

SCALE = 2

# number of pipe instances that are created
NUM_PIPES = 2

# resource loading
BIRD_IMGS = [loadImage(IMGS_PATH, image, SCALE) for image in IMAGES if "bird" in image]
PIPE_IMG = loadImage(IMGS_PATH, "pipe.png", SCALE)
BG_IMG = loadImage(IMGS_PATH, "bg.png", SCALE)

# window size
WIN_WIDTH = BG_IMG.get_width()
WIN_HEIGHT = BG_IMG.get_height()

GRAVITY = 3

# creates pygame window
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

