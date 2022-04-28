import pygame
from layouts import level_1
from level import Level
from gameloop import Gameloop


class App:
    def __init__(self):
        self.level = level_1
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
        gameloop = Gameloop(self.level_class, self.screen,
                            self.clock, self.size)

        gameloop.draw_starting_screen()
        gameloop.gameloop()


if __name__ == "__main__":
    app = App()
    app.run()
