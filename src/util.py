import pygame
import os

from Exceptions import CouldNotLoadImageException


def loadImage( directoryPath : str, fileName : str):
    """
    Loads images using pygame.
    :param directoryPath: str
    :param fileName: str
    :return: pygame image object
    """
    image = pygame.image.load(
            os.path.join(directoryPath + fileName))

    if image is None:
        raise CouldNotLoadImageException(f"could not load image: {fileName}")

    return image
