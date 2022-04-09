import pygame
from level import Level
from gameloop import Gameloop


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
        self.level_class = Level(self.level, self.size)
        self.screen = pygame.display.set_mode(
            (self.display_width, self.display_height))
        pygame.display.set_caption("Pacman")

    def run(self):
        pygame.init()
        g = Gameloop(self.level_class, self.screen, self.clock)

        g.draw_starting_screen()
        g.gameloop()

if __name__ == "__main__":
    app = App()
    app.run()
