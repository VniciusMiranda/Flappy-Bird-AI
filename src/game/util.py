import pygame
import os


class CouldNotLoadImageException(Exception):
    def __init__(self, message):
        super(CouldNotLoadImageException, self).__init__(message)

def getCurrentDirectoryAbsPath():
    return os.path.abspath(__file__).replace(os.path.basename(__file__), "")

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
    
    scaleTuple = (round(image.get_width()*scale), round(image.get_height()*scale))
    return pygame.transform.scale(image, scaleTuple)

    
