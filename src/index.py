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
    initial_level = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 1, 3, 1, 1, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
             [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
             [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    size = 50

    clock = pygame.time.Clock()

    height = len(initial_level)
    width = len(initial_level[0])
    display_height = height * size
    display_width = width * size
    screen = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption("Pacman")

    level = Level(initial_level, size)

    pygame.init()

    level.all_sprites.draw(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    level.move_pacman(x = -50)
                if event.key == K_RIGHT:
                    level.move_pacman(x = 50)
                if event.key == K_UP:
                    level.move_pacman(y = -50)
                if event.key == K_DOWN:
                    level.move_pacman(y = 50)
            if event.type == QUIT:
                running = False
        pygame.display.update()
        level.all_sprites.draw(screen)
        clock.tick(60)
if __name__ == "__main__":
    main()