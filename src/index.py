import pygame
from level import Level
import gameloop as g

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
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]
        self.size = 50
        self.clock = pygame.time.Clock()
        self.height = len(self.level)
        self.width = len(self.level[0])

    def run(self):
        display_height = self.height * self.size
        display_width = self.width * self.size
        screen = pygame.display.set_mode((display_width, display_height))
        pygame.display.set_caption("Pacman")
        level = Level(self.level, self.size)

        pygame.init()

        g.draw_starting_screen(screen)
        g.gameloop(level, screen, self.clock)

if __name__ == "__main__":
    app = App()
    app.run()
