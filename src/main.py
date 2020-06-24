from config import *

from Bird import Bird
from Pipe import Pipe
from Base import Base
from Score import Score




def update(bird, pipes, base, score):
    """
    Calls the update of all objects.
    :param bird: Bird
    :param pipe: Pipe
    :param base: Base
    :return: nothing
    """

    # update the bird
    bird.update()

    # update the pipes
    for pipe in pipes:
        pipe.update()

        # sets the pipe.passed back to False
        # when the pipe completes a cycle
        if pipe.x > bird.x:
            pipe.passed = False


        # test collision with the pipe
        if pipe.collide(bird):
            #TODO: make the bird die or something like that
            print("collided with the pipe")

        # test collision with the ground
        if base.collide(bird):
            print("hitted the floor")

        # make the pipes cycle infinitely
        if pipe.isOutOfScreen():
            pipe.x = 700

        # if the bird passed the pipe then congrats!!
        if not pipe.passed and pipe.x < bird.x:
            pipe.passed = True
            score.value += 1

    # update the base
    base.update()




def render(win, bird :Bird, pipes, base:Base, score):
    """
    Renders all of the objects on the screen.
    :param win: Window
    :param bird: Bird
    :param pipe: Pipe
    :param base: Base
    :return:
    """
    # draws the background
    win.blit(BG_IMG, (0, 0))

    # draws the bird
    bird.render(win)

    # draws the pipes
    for pipe in pipes:
        pipe.render(win)

    # draws the score and the base
    score.render(win)
    base.render(win)




def main():

    # instantiating the objects
    bird = Bird(WIN_WIDTH/5, WIN_HEIGHT - WIN_HEIGHT/2)
    pipes = [Pipe(WIN_WIDTH + i*(WIN_WIDTH/1.5)) for i in range(NUM_PIPES)]
    base = Base(WIN_HEIGHT - WIN_HEIGHT/14)
    score = Score(initialValue=0, font="comicsans", size=50)

    # game variables
    bye = False

    # Game Loop
    while not bye:
        # defines the FPS of the game
        CLOCK.tick(FPS)

        # update and render everything
        update(bird,pipes, base, score)
        render(WIN, bird, pipes, base, score)

        # listen for events
        for event in pygame.event.get():

            # if window is close the game stops
            if event.type == pygame.QUIT:
                bye = True
                break

            # just for testing :)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bird.jump()


        pygame.display.update()

    pygame.quit()




if __name__ == "__main__":
    main()
