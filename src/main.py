from config import *

from Bird import Bird
from Pipe import Pipe
from Base import Base
from Score import Score

baseHeight = WIN_HEIGHT - WIN_HEIGHT/14




def update(bird, pipes, base, score):
    """
    Calls the update of all objects.
    :param bird: Bird
    :param pipe: Pipe
    :param base: Base
    :return: nothing
    """
    global baseHeight


    bird.update()

    # update the pipes
    for pipe in pipes:
        pipe.update()


        if pipe.x > bird.x:
            pipe.passed = False

        # test collision with the bird
        if pipe.collide(bird):
            #TODO: make the bird die or something like that
            print("collided with the pipe")

        if base.collided(bird):
            print("hitted the floor")
        if pipe.isOutOfScreen():
            pipe.x = 700

        if not pipe.passed and pipe.x < bird.x:
            pipe.passed = True
            score.value += 1


    base.update()




def render(win, bird :Bird, pipes, base:Base, score):
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

    score.render(win)
    base.render(win)




def main():
    global baseHeight
    # define the start values
    bird = Bird(WIN_WIDTH/5, WIN_HEIGHT - WIN_HEIGHT/2)
    pipes = [Pipe(WIN_WIDTH + i*WIN_WIDTH/1.5) for i in range(3)]
    base = Base(baseHeight)
    score = Score(initialValue=0, font="comicsans", size=50)

    # game variables
    bye = False


    # Game Loop
    while not bye:
        CLOCK.tick(FPS)


        update(bird,pipes, base, score)
        render(WIN, bird, pipes, base, score)

        for event in pygame.event.get():

            # if window is close the game stops
            if event.type == pygame.QUIT:
                bye = True
                break

            # just for testing
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()

        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
