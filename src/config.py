from util import loadImage

import os
import pygame


"""
In this file all the configuration of the constant values is made.
"""
pygame.init()


# path variables
RESOURCES_PATH = "../resources"
IMGS_PATH = RESOURCES_PATH + "/imgs/"

IMAGES = os.listdir(IMGS_PATH)

FPS = 23
CLOCK = pygame.time.Clock()

SCALE = 1.3

# resource loading
BIRD_IMGS = [loadImage(IMGS_PATH, image, SCALE) for image in IMAGES if "bird" in image]
PIPE_IMG = loadImage(IMGS_PATH, "pipe.png", SCALE)
BG_IMG = loadImage(IMGS_PATH, "bg.png", SCALE)
BASE_IMG = loadImage(IMGS_PATH, "base.png",SCALE)

# window size
WIN_WIDTH = BG_IMG.get_width()
WIN_HEIGHT = BG_IMG.get_height()

GRAVITY = 3

# creates pygame window
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

