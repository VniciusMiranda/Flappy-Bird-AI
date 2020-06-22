from Bird import Bird
from config import *



if __name__ == "__main__":
    run = True
    clock = pygame.time.Clock()
    bird = Bird(WIN_WIDTH/2, WIN_HEIGHT/2)

    while run:
        clock.tick(30)

        WIN.blit(BG_IMG, (0, 0))
        bird.render(WIN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


        pygame.display.update()

    pygame.quit()
