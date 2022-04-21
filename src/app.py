import pygame
from level import Level
from gameloop import Gameloop

class App:
    def __init__(self):
        self.level = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                      [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1],
                      [1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1],
                      [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                      [1, 1, 1, 0, 1, 4, 4, 4, 4, 1, 0, 1, 1, 1],
                      [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
                      [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
                      [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1],
                      [1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
                      [1, 0, 1, 0, 0, 3, 0, 0, 0, 0, 1, 0, 0, 1],
                      [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
                      [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1],
                      [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        self.size = 30
        self.clock = pygame.time.Clock()
        self.display_height = len(self.level) * self.size
        self.display_width = len(self.level[0]) * self.size
        self.screen = pygame.display.set_mode(
            (self.display_width, self.display_height))
        pygame.display.set_caption("Pacman")
        self.level_class = Level(self.level, self.size)

    def run(self):
        pygame.init()
        gameloop = Gameloop(self.level_class, self.screen, self.clock, self.size)

        gameloop.draw_starting_screen()
        gameloop.gameloop()

if __name__ == "__main__":
    app = App()
    app.run()
