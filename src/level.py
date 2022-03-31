import pygame
from sprites.pacman import Pacman
from sprites.wall import Wall
from sprites.floor import Floor

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.pacman = None
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self._initialize_sprites(level_map)

    def _initialize_sprites(self, level_map):
        level_height = len(level_map)
        level_width = len(level_map[0])

        for y in range(level_height):
            for x in range(level_width):
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if level_map[y][x] == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                elif level_map[y][x] == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif level_map[y][x] == 2:
                    pass
                elif level_map[y][x] == 3:
                    self.pacman = Pacman(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))
        self.all_sprites.add(
            self.floors,
            self.walls,
            self.pacman
        )

    def move_pacman(self, dx = 0, dy = 0):
        self.pacman.rect.move_ip(dx, dy)

