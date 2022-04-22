import pygame
from sprites.pacman import Pacman
from sprites.wall import Wall
from sprites.floor import Floor
from sprites.pellet import Pellet
from sprites.powerpellet import PowerPellet
from sprites.ghost import Ghost
from collections import deque

class Level:
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.pacman = None
        self.pacman_coordinates = []
        self.ghost_coordinates = []
        self.level = level_map
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.power_pellets = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.score = 0
        self.lives = 3
        self.ghost = None
        self.initialize_sprites(level_map)

    def initialize_sprites(self, level_map):
        ghost_count = 1

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
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.power_pellets.add(PowerPellet(normalized_x, normalized_y))

                elif level_map[height][width] == 3:
                    self.pacman = Pacman(normalized_x, normalized_y)
                    self.pacman_coordinates = [width, height]
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif level_map[height][width] == 4:
                    if ghost_count == 1:
                        self.ghost = Ghost(1, normalized_x, normalized_y)
                        self.ghosts.add(self.ghost)
                        self.ghost_coordinates = [width, height]
                        self.floors.add(Floor(normalized_x, normalized_y))
                        ghost_count += 1

                    elif ghost_count == 2:
                        self.ghosts.add(Ghost(2, normalized_x, normalized_y))
                        self.floors.add(Floor(normalized_x, normalized_y))
                        ghost_count += 1

                    elif ghost_count == 3:
                        self.ghosts.add(Ghost(3, normalized_x, normalized_y))
                        self.floors.add(Floor(normalized_x, normalized_y))
                        ghost_count += 1

                    else:
                        self.ghosts.add(Ghost(4, normalized_x, normalized_y))
                        self.floors.add(Floor(normalized_x, normalized_y))

        self.all_sprites.add(
            self.floors,
            self.walls,
            self.pacman,
            self.power_pellets,
            self.pellets,
            self.ghosts
        )

    def moving_is_possible(self, sprite, direction):
        sprite.rect.move_ip(direction[0], direction[1])
        crashing = pygame.sprite.spritecollide(sprite, self.walls, False)
        can_move = not crashing
        sprite.rect.move_ip(-direction[0], -direction[1])
        return can_move

    def pacman_eats(self):
        if pygame.sprite.spritecollide(self.pacman, self.pellets, True) or pygame.sprite.spritecollide(self.pacman, self.power_pellets, True):
            self.score += 10
    
    def pacman_meets_ghost(self):
        if pygame.sprite.spritecollide(self.pacman, self.ghosts, False):
            return True
        return False

    def move_pacman(self, direction):
        if len(self.pellets) == 0:
            return "finished"

        if not self.moving_is_possible(self.pacman, direction):
            return

        self.pacman.rect.move_ip(direction[0], direction[1])
        new_coordinates = [direction[0] // self.cell_size, direction[1]//self.cell_size]
        self.pacman_coordinates = [self.pacman_coordinates[0] + new_coordinates[0], self.pacman_coordinates[1] + new_coordinates[1]]
        print(self.pacman_coordinates)
        if self.pacman_meets_ghost():
            self.lives -= 1
            return "dead"
        self.pacman_eats()

    def move_ghost(self):
        path = self.bfs([self.ghost_coordinates[0], self.ghost_coordinates[1]], [self.pacman_coordinates[0], self.pacman_coordinates[1]])
        next_cell = path[1]
        x_dir = next_cell[0] - self.ghost_coordinates[0]
        y_dir = next_cell[1] - self.ghost_coordinates[1]
        self.ghost.rect.move_ip(x_dir*self.cell_size, y_dir*self.cell_size)
        self.ghost_coordinates = [self.ghost_coordinates[0] + x_dir, self.ghost_coordinates[1] + y_dir]

    def bfs(self, start, target):
        q = deque()
        visited = []
        path = []
        q.append(start)
        while q:
            current = q.popleft()
            visited.append(current)

            if current == target:
                break
            for neighbour in [[0,1], [0,-1], [1,0], [-1,0]]:
                if neighbour[0]+current[0] >= 0 and neighbour[0]+current[0] < len(self.level[0]):
                    if neighbour[1]+current[1] >= 0 and neighbour[1]+current[1] < len(self.level):
                        next_cell = [neighbour[0]+current[0], neighbour[1]+current[1]]
                        if next_cell not in visited:
                            if self.level[next_cell[1]][next_cell[0]] != 1:
                                q.append(next_cell)
                                path.append({"Current":current, "Next":next_cell})
        shortest = [target]
        while target != start:
            for step in path:
                if step["Next"] == target:
                    target = step["Current"]
                    shortest.insert(0, step["Current"])
        return shortest