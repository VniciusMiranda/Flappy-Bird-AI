from config import *

from Bird import Bird
from Pipe import Pipe
from Base import Base


def update(bird, pipes, base):
    """
    Calls the update of all objects.
    :param bird: Bird
    :param pipe: Pipe
    :param base: Base
    :return: nothing
    """

    bird.update()
    for pipe in pipes:
        pipe.update()

        # test collision with the bird
        if pipe.collide(bird):
            pass

        if pipe.isOutOfScreen():
            pipe.x = 700


    base.update()

def render(win, bird :Bird, pipes, base:Base):
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

    for pipe in pipes:
        pipe.render(win)

    base.render(win)

def main():

    # define the start values
    bird = Bird(WIN_WIDTH/5, WIN_HEIGHT - WIN_HEIGHT/2)
    pipes = [Pipe(WIN_WIDTH + i*WIN_WIDTH/1.5) for i in range(3)]
    base = Base( WIN_HEIGHT - WIN_HEIGHT/15)


    bye = False


    # Game Loop
    while not bye:
        CLOCK.tick(FPS)


        update(bird,pipes, base)
        render(WIN, bird, pipes, base)

        for event in pygame.event.get():
            # see if window was closed
            if event.type == pygame.QUIT:
                bye = True


        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
