from game.Game import Game
import neat

def run_neat(configPath, game):
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                                neat.DefaultSpeciesSet, neat.DefaultStagnation,
                                configPath)

    population = neat.Population(config)

    population.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    population.add_reporter(stats)

    winner = population.run( game.run, 100)

if __name__ == "__main__":
    game = Game()
    run_neat(game.NEAT_CONFIG_PATH, game)

