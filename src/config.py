from .util import *
import os

RESOURCES_PATH = "../resources"
IMGS_PATH = RESOURCES_PATH + "/imgs/"

IMAGES = os.listdir(IMGS_PATH)

WIN_WIDTH = 600
WIN_HEIGHT = 800

# resource loading
BIRD_IMGS = [loadImage(IMGS_PATH, image) for image in IMAGES if "bird" in image]
PIPE_IMG = loadImage(IMGS_PATH, "pipe.png")
BG_IMG = loadImage(IMGS_PATH, "bg.png")
BASE_IMG = loadImage(IMGS_PATH, "base.png")

GRAVITY = 3

