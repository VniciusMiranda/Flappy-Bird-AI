from config import *

from Bird import Bird
from Pipe import Pipe
from Base import Base

def drawWindow(win, bird, pipe, base):
    win.blit(BG_IMG, (0, 0))
    bird.render(win)

def update(bird, pipe, base):
    """
    Calls the update of all objects.
    :param bird: Bird
    :param pipe: Pipe
    :param base: Base
    :return: nothing
    """
    bird.update()
    pipe.update()
    base.update()

def render(win, bird :Bird, pipe:Pipe, base:Base):
    """
    Renders all on the screen.
    :param win: Window from pygame
    :param bird: Bird
    :param pipe: Pipe
    :param base: Base
    :return:
    """
    win.blit(BG_IMG, (0, 0))
    bird.render(win)
    pipe.render(win)
    base.render(win)


def main():

    bird = Bird(WIN_WIDTH/2, WIN_HEIGHT/2)
    pipe = Pipe(WIN_WIDTH)
    base = Base( WIN_HEIGHT - WIN_HEIGHT/5)

    bye = False
    while not bye:
        CLOCK.tick(FPS)


        update(bird,pipe, base)
        render(WIN, bird, pipe, base)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bye = True


        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
