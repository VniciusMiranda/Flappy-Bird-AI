



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








if __name__ == "__main__":
    pass