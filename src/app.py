import pygame
from levels.layouts import level_1
from gamelogic.level import Level
from ui.gameloop import Gameloop


class App:
    def __init__(self):
        self.size = 30
        self.clock = pygame.time.Clock()
        self.display_height = len(level_1) * self.size
        self.display_width = len(level_1[0]) * self.size
        self.screen = pygame.display.set_mode(
            (self.display_width, self.display_height))
        pygame.display.set_caption("Pacman")
        self.level_class1 = Level(level_1, self.size)

    def run(self):
        pygame.init()
        gameloop = Gameloop(self.level_class1, self.screen,
                            self.clock, self.size)

        gameloop.draw_starting_screen()
        gameloop.gameloop()


if __name__ == "__main__":
    app = App()
    app.run()
