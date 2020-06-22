"""
Might not be really necessary because it's a small personal project,
but it is good to keep the good practices :)
"""
class CouldNotLoadImageException(Exception):

    def __init__(self, message):
        super().__init__(message)


class InvalidCoordinateException(Exception):
    def __init__(self, message):
        super().__init__(message)


class  InvalidBirdCoordinateException(InvalidCoordinateException):
    def __init__(self, message):
        super().__init__(message)

class InvalidPipeCoordinateException(InvalidCoordinateException):
    def __init__(self, message):
        super().__init__(message)