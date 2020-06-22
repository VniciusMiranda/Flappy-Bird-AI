from util import loadImage

import os
import pygame

"""
In this file all the configuration of the constant values is made
and the import statements of third part modules are here.
"""
pygame.init()


# path variables
RESOURCES_PATH = "../resources"
IMGS_PATH = RESOURCES_PATH + "/imgs/"

IMAGES = os.listdir(IMGS_PATH)

# window size
WIN_WIDTH = 288
WIN_HEIGHT = 512

# resource loading
BIRD_IMGS = [loadImage(IMGS_PATH, image) for image in IMAGES if "bird" in image]
PIPE_IMG = loadImage(IMGS_PATH, "pipe.png")
BG_IMG = loadImage(IMGS_PATH, "bg.png")
BASE_IMG = loadImage(IMGS_PATH, "base.png")

GRAVITY = 3

# creates pygame window
WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

