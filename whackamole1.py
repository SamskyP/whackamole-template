import pygame
import random

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        moleX = 0
        moleY = 0
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked_x, clicked_y = event.pos
                    if clicked_x // 32 == moleX and clicked_y // 32 == moleY:
                        moleX = random.randrange(0, 20)
                        moleY = random.randrange(0, 16)

            screen.fill("light green")
            for i in range(20):
                pygame.draw.line(screen, "dark green", (i * 32, 0), (i * 32, 512))
            for i in range(16):
                pygame.draw.line(screen, "dark green", (0, i * 32), (640, i * 32))
            screen.blit(mole_image, mole_image.get_rect(topleft=(moleX * 32, moleY * 32)))
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()