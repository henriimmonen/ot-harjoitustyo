import pygame
from sprites.pacman import Pacman
from sprites.wall import Wall
from sprites.floor import Floor
from sprites.pellet import Pellet


class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.pacman = None
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.initialize_sprites(level_map)
        self.score = 0

    def initialize_sprites(self, level_map):
        level_height = len(level_map)
        level_width = len(level_map[0])

        for y in range(level_height):
            for x in range(level_width):
                normalized_x = x * self.cell_size
                normalized_y = y * self.cell_size

                if level_map[y][x] == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.pellets.add(Pellet(normalized_x, normalized_y))
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
            self.pacman,
            self.pellets
        )

    def moving_is_possible(self, x=0, y=0):
        self.pacman.rect.move_ip(x, y)
        crashing = pygame.sprite.spritecollide(self.pacman, self.walls, False)
        can_move = not crashing
        self.pacman.rect.move_ip(-x, -y)
        return can_move

    def pacman_eats(self):
        if pygame.sprite.spritecollide(self.pacman, self.pellets, True):
            self.score += 10

    def move_pacman(self, x=0, y=0):
        if not self.moving_is_possible(x, y):
            return
        self.pacman.rect.move_ip(x, y)
        self.pacman_eats()

