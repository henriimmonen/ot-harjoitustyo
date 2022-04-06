import pygame, sys
from level import Level
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


class App:
    def __init__(self):
        self.level = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 3, 1, 1, 0, 1, 0, 1],
                      [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                      [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                      [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
                      [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
                      [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.size = 50
        self.clock = pygame.time.Clock()
        self.height = len(self.level)
        self.width = len(self.level[0])

    def draw_starting_screen(self, screen):
        screen.fill((0,0,0))
        font = pygame.font.SysFont('arial black', 16)
        start_text = font.render("START GAME", False, (200, 150, 100))
        highscore_text = font.render("HIGHSCORES", False, (107,183,210,1))

        screen.blit(start_text, (200,200))
        screen.blit(highscore_text, (200,0))
        pygame.display.update()

        ok = True
        while ok:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        ok = False
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                if event.type == QUIT:
                        pygame.quit()
                        sys.exit()


    def run(self):
        display_height = self.height * self.size
        display_width = self.width * self.size
        screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Pacman")
        level = Level(self.level, self.size)

        pygame.init()

        self.draw_starting_screen(screen)
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
            self.clock.tick(60)

if __name__ == "__main__":
    app = App()
    app.run()
