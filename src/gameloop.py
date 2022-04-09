import pygame
import sys
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

class Gameloop:
    def __init__(self, level, screen, clock):
        self.screen = screen
        self.level = level
        self.clock = clock
        self.font = pygame.font.SysFont('arial black', 16)
        self.score = pygame.Rect(200, 0, 100, 50)
        self.direction = (0,0)
        self.running = True
        self.starting_screen = True

    def draw_starting_screen(self):
        self.initialize_starting_screen()

        while self.starting_screen:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        self.starting_screen = False
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    def gameloop(self):
        self.initialize_gameloop()

        while self.running:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        self.running = False
                    if event.key == K_LEFT:
                        self.direction = (-50, 0)
                    if event.key == K_RIGHT:
                        self.direction = (50, 0)
                    if event.key == K_UP:
                        self.direction = (0, -50)
                    if event.key == K_DOWN:
                        self.direction = (0, 50)
                if event.type == QUIT:
                    self.running = False
            self.update_round(self.direction)

    def initialize_starting_screen(self):
        self.screen.fill((0, 0, 0))
        start_text = self.font.render(
            "START GAME BY PRESSING SPACE", False, (200, 150, 100))
        highscore_text = self.font.render("HIGHSCORES", False, (107, 183, 210, 1))
        self.screen.blit(start_text, (100, 200))
        self.screen.blit(highscore_text, (200, 0))
        pygame.display.update()

    def initialize_gameloop(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), self.score)
        self.level.all_sprites.draw(self.screen)
        pygame.display.update()

    def update_score(self):
        score_text = self.font.render("SCORE: {}".format(
            self.level.score), True, (107, 183, 210, 1))
        self.screen.fill((0, 0, 0), self.score)
        self.screen.blit(score_text, self.score)

    def update_round(self, direction):
        self.level.move_pacman(direction)
        self.update_score()
        pygame.display.update()
        self.level.all_sprites.draw(self.screen)
        self.clock.tick(7)