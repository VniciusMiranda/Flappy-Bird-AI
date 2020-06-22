from Bird import Bird
from config import *




def drawWindow(win, bird):
    win.blit(BG_IMG, (0, 0))
    bird.render(win)
    pygame.display.update()


if __name__ == "__main__":
    run = True
    clock = pygame.time.Clock()
    bird = Bird(WIN_WIDTH/2, WIN_HEIGHT/2)

    while run:
        clock.tick(30)

        drawWindow(WIN, bird)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False



    pygame.quit()
