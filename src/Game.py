from GameObject import GameObject
from util import loadImage
from Score import Score
from Base import Base
from Bird import Bird
from Pipe import Pipe

import pygame

# Game is a GameObject?? yeah... philosophical question right there
# If a set is subset of itself then I think it's ok for a Game itself
# be a game object XD
class Game(GameObject):

    FPS = 23
    SCALE = 2
    NUM_PIPES = 2
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
        self.pipes = [Pipe(self.WIN_WIDTH, self.SCALE, i) for i in range(self.NUM_PIPES)]
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
        pass




    def update(self):
        """

        :return:
        """
        pass


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
                    bye = True
                    break

                # just for testing :)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.bird.jump()

            pygame.display.update()


