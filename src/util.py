import pygame
import os

from Exceptions import CouldNotLoadImageException


# all images will be transform to 2 times the original size when loaded
def loadImage( directoryPath : str, fileName : str):
    image = pygame.image.load(
            os.path.join(directoryPath + fileName))

    if image is None:
        raise CouldNotLoadImageException(f"could not load image: {fileName}")

    return image
