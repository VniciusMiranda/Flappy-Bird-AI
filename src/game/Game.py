from game.util import getCurrentDirectoryAbsPath, loadImage
from game.GameObject import GameObject
from game.Score import Score
from game.Base import Base
from game.Bird import Bird
from game.Pipe import Pipe

from operator import attrgetter
import neat
import pygame
import os

# Game is a GameObject?? yeah... philosophical question right there
# If a set is subset of itself then I think it's ok for a Game itself
# be a game object XD
class Game(GameObject):

    # turn to False if u don't want the lines tho
    DRAW_LINES = True
    FPS = 23
    # change the scale of the game
    SCALE = 1.2
    # changing this might broke some things XD
    NUM_PIPES = 2
    GRAVITY = 3
    NEAT_CONFIG_PATH = getCurrentDirectoryAbsPath() + "config-feedforward.txt"

    def __init__(self):
        """
        This class encapsulate the entire Flappy bird game
        and the AI that will play it.
        """
        super().__init__()

        # third part libraries init()
        pygame.init()
        pygame.font.init()

        self.CLOCK = pygame.time.Clock()

        # declare some game object variables
        self.pipes : list
        self.base : Base
        self.birds: list

        self.genomes : list
        self.networks : list

        self.BG_IMG = loadImage(self.IMGS_PATH, "bg.png", self.SCALE)
        self.WIN_HEIGHT = self.BG_IMG.get_height()
        self.WIN_WIDTH = self.BG_IMG.get_width()

        # creates pygame window
        self.WIN = pygame.display.set_mode((self.WIN_WIDTH, self.WIN_HEIGHT))


        # instantiate the score variable
        self.score = Score(initialValue=0, font="comicsans", size=50, win_width=self.WIN_WIDTH)

        # game loop boolean
        self.bye = False


    def render(self, win=None):
        """
        Game render method. Calls the render method of all objects.
        :param win: Window
        :return: nothing
        """
        # draws the background
        win.blit(self.BG_IMG, (0, 0))

        frontPipeId = self.getFrontPipe()

        # draws the birds
        for bird in self.birds:
            bird.render(win)
            if self.DRAW_LINES:
                try:
                    pygame.draw.line(win, (255, 0, 0),
                                     (bird.x + bird.image.get_width() / 2, bird.y + bird.image.get_height() / 2), (
                                     self.pipes[frontPipeId].x + self.pipes[frontPipeId].PIPE_TOP.get_width() / 2,
                                     self.pipes[frontPipeId].height), 5)
                    pygame.draw.line(win, (255, 0, 0),
                                     (bird.x + bird.image.get_width() / 2, bird.y + bird.image.get_height() / 2), (
                                     self.pipes[frontPipeId].x + self.pipes[frontPipeId].PIPE_BOTTOM.get_width() / 2,
                                     self.pipes[frontPipeId].bottom), 5)
                except:
                    pass

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

        frontPipeId = self.getFrontPipe()

        # update the bird
        for  bird in self.birds:
            self.genomes[self.birds.index(bird)].fitness += 0.1
            bird.update()

            output = self.networks[self.birds.index(bird)].activate((
                bird.y,
                abs(bird.y - self.pipes[frontPipeId].height),
                abs(bird.y - self.pipes[frontPipeId].bottom)))[0]

            if output > 0.5:
                bird.jump()

        # update the pipes
        for pipe in self.pipes:

            pipe.update()

            # test collision with the pipe
            for bird in self.birds:
                if pipe.collide(bird):
                    self.genomes[self.birds.index(bird)].fitness -= 1.5
                    self.networks.pop(self.birds.index(bird))
                    self.genomes.pop(self.birds.index(bird))
                    self.birds.pop(self.birds.index(bird))

            # test collision with the ground
            for bird in self.birds:
                if self.base.collide(bird):

                    self.networks.pop(self.birds.index(bird))
                    self.genomes.pop(self.birds.index(bird))
                    self.birds.pop(self.birds.index(bird))

            for bird in self.birds:
                # if the bird passed the pipe then congrats!!
                if pipe.birdPassed(bird):
                    self.score.update()
                    pipe.reset_time = 0
                    for g in self.genomes:
                        g.fitness += 5

        self.base.update()


    def run(self, genomes, config):
        self.birds = []
        self.genomes = []
        self.networks = []

        # initialize genomes and birds
        for _, g in genomes:
            self.networks.append(neat.nn.FeedForwardNetwork.create(g, config))
            self.birds.append(Bird(self.WIN_WIDTH, self.WIN_HEIGHT,self.SCALE, self.GRAVITY))
            g.fitness = 0
            self.genomes.append(g)

        self.pipes = [Pipe(self.WIN_WIDTH,self.WIN_HEIGHT, self.SCALE, factor) for factor in range(self.NUM_PIPES)]
        self.base = Base(self.WIN_HEIGHT, self.SCALE)

        while not self.bye and len(self.birds) > 0:
            self.CLOCK.tick(self.FPS)

            # updates and renders everything
            self.update()
            self.render(self.WIN)

            # listen for events
            for event in pygame.event.get():

                # if window is close the game stops
                if event.type == pygame.QUIT:
                    self.bye = True
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    # quiting with the "q" key
                    if event.key == pygame.K_q:
                        self.bye = True

            pygame.display.update()

        # resets the value of the score
        self.score.value = 0


    def getFrontPipe(self):
        maxPipe = max(self.pipes, key=attrgetter('reset_time'))
        return self.pipes.index(maxPipe)