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
        self.score = 0
        self.initialize_sprites(level_map)

    def initialize_sprites(self, level_map):
        level_height = len(level_map)
        level_width = len(level_map[0])

        for height in range(level_height):
            for width in range(level_width):
                normalized_y = height * self.cell_size
                normalized_x = width * self.cell_size

                if level_map[height][width] == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.pellets.add(Pellet(normalized_x, normalized_y))
                elif level_map[height][width] == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))
                elif level_map[height][width] == 2:
                    pass
                elif level_map[height][width] == 3:
                    self.pacman = Pacman(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.pacman,
            self.pellets
        )

    def moving_is_possible(self, d_x=0, d_y=0):
        self.pacman.rect.move_ip(d_x, d_y)
        crashing = pygame.sprite.spritecollide(self.pacman, self.walls, False)
        can_move = not crashing
        self.pacman.rect.move_ip(-d_x, -d_y)
        return can_move

    def pacman_eats(self):
        if pygame.sprite.spritecollide(self.pacman, self.pellets, True):
            self.score += 10

    def move_pacman(self, direction):
        if not self.moving_is_possible(direction[0], direction[1]):
            return

        self.pacman.rect.move_ip(direction[0], direction[1])
        self.pacman_eats()
