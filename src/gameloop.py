import pygame, sys
from pygame.locals import (
    K_SPACE,
    K_LEFT,
    K_RIGHT,
    K_UP,
    K_DOWN,
    KEYDOWN,
    K_ESCAPE,
    QUIT,
)

def draw_starting_screen(screen):
    screen.fill((0,0,0))
    font = pygame.font.SysFont('arial black', 16)
    start_text = font.render("START GAME BY PRESSING SPACE", False, (200, 150, 100))
    highscore_text = font.render("HIGHSCORES", False, (107,183,210,1))

    screen.blit(start_text, (100,200))
    screen.blit(highscore_text, (200,0))
    pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    running = False
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

def gameloop(level, screen, clock):
    level.all_sprites.draw(screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_LEFT:
                    level.move_pacman(x=-50)
                if event.key == K_RIGHT:
                    level.move_pacman(x=50)
                if event.key == K_UP:
                    level.move_pacman(y=-50)
                if event.key == K_DOWN:
                    level.move_pacman(y=50)
            if event.type == QUIT:
                running = False
        pygame.display.update()
        level.all_sprites.draw(screen)
        clock.tick(60)