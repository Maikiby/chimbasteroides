import pygame
from constants import *

def main():
    _ = pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_clock = pygame.time.Clock()
    dt = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        _ = screen.fill("#000000", None, 0)

        pygame.display.flip()

        dt = game_clock.tick(60) / 1000
    
if __name__ == "__main__":
    main()
