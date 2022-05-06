import pygame
import sqlite3
from gamelogic.level import Level
from levels.layouts import LEVEL_1, CELL_SIZE
from ui.gameloop import Gameloop


class App:
    def __init__(self):
        """Alustetaan parametrit pelin käynnistämistä varten.
        """
        self.clock = pygame.time.Clock()
        self.display_height = len(LEVEL_1) * CELL_SIZE
        self.display_width = len(LEVEL_1[0]) * CELL_SIZE
        self.screen = pygame.display.set_mode(
            (self.display_width, self.display_height))
        pygame.display.set_caption("Pacman")
        self.level_class1 = Level()

    def _establish_database(self):
        connection = sqlite3.connect('highscores.db')
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='highscores'")
        result = cursor.fetchall()
        if result == []:
            cursor.execute('''CREATE TABLE highscores (player, score)''')
            connection.commit()
        connection.close()

    def run(self):
        """Käynnistetään pygame ja luodaan Gameloop-luokan instanssi.
        """
        self._establish_database()
        pygame.init()
        gameloop = Gameloop(self.level_class1, self.screen,
                            self.clock, CELL_SIZE)
        gameloop.draw_starting_screen()
        gameloop.gameloop()


if __name__ == "__main__":
    app = App()
    app.run()
