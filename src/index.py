import pygame
from level import Level
import gameloop as g


class App:
    def __init__(self):
        self.level = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
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
        self.level_height = len(self.level)
        self.level_width = len(self.level[0])
        self.display_height = self.level_height * self.size
        self.display_width = self.level_width * self.size
        self.screen = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption("Pacman")

    def run(self):
        level_object = Level(self.level, self.size)

        pygame.init()

        g.draw_starting_screen(self.screen)
        g.gameloop(level_object, self.screen, self.clock)


if __name__ == "__main__":
    app = App()
    app.run()
