from game.GameObject import GameObject
from game.util import loadImage
from game.Score import Score
from game.Base import Base
from game.Bird import Bird
from game.Pipe import Pipe

import pygame

# Game is a GameObject?? yeah... philosophical question right there
# If a set is subset of itself then I think it's ok for a Game itself
# be a game object XD
class Game(GameObject):

    FPS = 23
    SCALE = 1.2
    NUM_PIPES = 4
    GRAVITY = 3

    def __init__(self):
        """
        This class encapsulate the entire Flappy bird game.
        """
        super().__init__()

        # third part libraries init()
        pygame.init()
        pygame.font.init()

        self.CLOCK = pygame.time.Clock()

        self.BG_IMG = loadImage(self.IMGS_PATH, "bg.png", self.SCALE)
        self.WIN_HEIGHT = self.BG_IMG.get_height()
        self.WIN_WIDTH = self.BG_IMG.get_width()

        # creates pygame window
        self.WIN = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))

        # instantiate all the game objects
        self.bird = Bird(self.WIN_WIDTH, self.WIN_HEIGHT, self.SCALE, self.GRAVITY)
        self.pipes = [Pipe(self.WIN_WIDTH, self.SCALE, factor) for factor in range(self.NUM_PIPES)]
        self.base = Base(self.WIN_HEIGHT - self.WIN_HEIGHT/14, self.SCALE)

        # instantiate the score variable
        self.score = Score(initialValue=0, font="comicsans", size=50, win_width=self.WIN_WIDTH)

        # game loop boolean
        self.bye = False

        self.run()
        pygame.quit()


    def render(self, win=None):
        """
        Game render method. Calls the render method of all objects.
        :param win: Window
        :return: nothing
        """
        # draws the background
        win.blit(self.BG_IMG, (0, 0))

        # draws the bird
        self.bird.render(win)

        # draws the pipes
        for pipe in self.pipes:
            pipe.render(win)

        # draws the score and the base
        self.score.render(win)
        self.base.render(win)




    def update(self):
        """
        Game update method. It updates the state and coordinates of
        every object of the game.
        :return: nothing
        """

        # update the bird
        self.bird.update()

        # update the pipes
        for pipe in self.pipes:

            pipe.update()


            # test collision with the pipe
            if pipe.collide(self.bird):
                # TODO: make the bird die or something like that
                pass


            # test collision with the ground
            if self.base.collide(self.bird):
                # TODO: make the bird die or something like that
                pass


            # if the bird passed the pipe then congrats!!
            if pipe.birdPassed(self.bird):
                self.score.update()


        # update the base
        self.base.update()


    def run(self):

        while not self.bye:
            self.CLOCK.tick(self.FPS)

            # updates and renders everything
            self.update()
            self.render(self.WIN)

            # listen for events
            for event in pygame.event.get():

                # if window is close the game stops
                if event.type == pygame.QUIT:
                    self.bye = True
                    break


                # just for testing :)
                if event.type == pygame.KEYDOWN:

                    # jump with the space bar
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

                    # quiting with the "q" key
                    if event.key == pygame.K_q:
                        self.bye = True

            pygame.display.update()


