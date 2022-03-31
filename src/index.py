import pygame
from level import Level
from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    KEYDOWN,
    K_ESCAPE,
    QUIT,
)

def main():

    LEVEL_MAP = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 3, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    CELL_SIZE = 50

    clock = pygame.time.Clock()

    height = len(LEVEL_MAP)
    width = len(LEVEL_MAP[0])
    display_height = height * CELL_SIZE
    display_width = width * CELL_SIZE
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Pacman")

    level = Level(LEVEL_MAP, CELL_SIZE)

    pygame.init()

    level.all_sprites.draw(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    level.move_pacman(dx = -50)
                if event.key == K_RIGHT:
                    level.move_pacman(dx = 50)
                if event.key == K_UP:
                    level.move_pacman(dy = -50)
                if event.key == K_DOWN:
                    level.move_pacman(dy = 50)
                if event.type == QUIT:
                    running = False
        pygame.display.update()
        level.all_sprites.draw(screen)
        clock.tick(60)
if __name__ == "__main__":
    main()