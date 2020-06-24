import pygame
import os


class CouldNotLoadImageException(Exception):
    def __init__(self, message):
        super(CouldNotLoadImageException, self).__init__(message)



def loadImage( directoryPath : str, fileName : str, scale=1.0):
    """
    Loads images using pygame
    :param directoryPath: str
    :param fileName: str
    :return: pygame image object
    """
    image = pygame.image.load(
            os.path.join(directoryPath + fileName))

    if image is None:
        raise CouldNotLoadImageException(f"could not load image: {fileName}")

    image = pygame.transform.scale(image,
                                   (round(image.get_width()*scale),
                                    round(image.get_height()*scale)))

    return image
