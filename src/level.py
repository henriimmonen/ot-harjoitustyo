from collections import deque
import pygame
from sprites.pacman import Pacman
from sprites.wall import Wall
from sprites.floor import Floor
from sprites.pellet import Pellet
from sprites.powerpellet import PowerPellet
from sprites.ghost import Ghost


class Level: # pylint: disable=too-many-instance-attributes
             # all instance attributes are necessary for this class
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.level = level_map
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.power_pellets = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.score = 0
        self.lives = 3
        self.timer = None
        self.initialize_sprites(level_map)

    def initialize_sprites(self, level_map): # pylint: disable=too-many-statements
                                             # statements are required to initialize
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
                    self.power_pellets.add(
                        PowerPellet(normalized_x, normalized_y))

                elif level_map[height][width] == 3:
                    self.pacman = Pacman(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif level_map[height][width] == 4:
                    self.ghosts.add(Ghost(1, normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif level_map[height][width] == 5:
                    self.ghosts.add(Ghost(2, normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif level_map[height][width] == 6:
                    self.ghosts.add(Ghost(3, normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif level_map[height][width] == 7:
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

    def moving_is_possible(self, sprite):
        sprite.rect.move_ip(sprite.direction[0]//sprite.speed, sprite.direction[1]//sprite.speed)
        crashing = pygame.sprite.spritecollide(sprite, self.walls, False)
        can_move = not crashing
        sprite.rect.move_ip(-sprite.direction[0]//sprite.speed, -sprite.direction[1]//sprite.speed)
        return can_move

    def pacman_eats(self):
        if pygame.sprite.spritecollide(self.pacman, self.pellets, True):
            self.score += 10
        elif pygame.sprite.spritecollide(self.pacman, self.power_pellets, True):
            self.score += 20
            self.ghosts_are_vulnerable()

    def ghosts_are_vulnerable(self):
        self.timer = pygame.time.get_ticks()
        for ghost in self.ghosts:
            ghost.vulnerable = True
            ghost.set_image()

    def pacman_meets_ghost(self):
        list_of_colliding = pygame.sprite.spritecollide(self.pacman, self.ghosts, False)
        for ghost in list_of_colliding:
            if ghost.vulnerable == True:
                self.score += 100
                ghost.kill()
                self.revive_ghost(ghost)
                return False
        if pygame.sprite.spritecollide(self.pacman, self.ghosts, False):
            self.lives -= 1
            return True
        return False

    def revive_ghost(self, ghost):
        starting_point = 150 + 30*ghost.number
        self.ghosts.add(Ghost(ghost.number, starting_point, 210))
        self.all_sprites.add(self.ghosts)

    def move_pacman(self, direction):
        self.check_timer()
        self.pacman.new_direction = direction
        if self.centered(self.pacman):
            self.pacman.direction = self.pacman.new_direction

        if self.moving_is_possible(self.pacman):
            self.pacman.set_image()
            self.pacman.rect.move_ip(
                self.pacman.direction[0]//self.pacman.speed, self.pacman.direction[1]//self.pacman.speed)
            self.pacman_eats()

    def move_ghost(self, sprite):
        if self.centered(sprite):
            next_cell = self.find_path(sprite)
            x_coordinate = next_cell[0] - sprite.rect.x//self.cell_size
            y_coordinate = next_cell[1] - sprite.rect.y//self.cell_size
            sprite.direction = (x_coordinate, y_coordinate)
            sprite.rect.move_ip(x_coordinate*(self.cell_size//sprite.speed),
                                y_coordinate*(self.cell_size//sprite.speed))
        else:
            sprite.rect.move_ip(sprite.direction[0] * (
                self.cell_size//sprite.speed), sprite.direction[1] * (self.cell_size//sprite.speed))

    def check_timer(self):
        if self.timer:
            if pygame.time.get_ticks() - self.timer >= 5000:
                for ghost in self.ghosts:
                    ghost.vulnerable = False
                    ghost.set_image()

    def centered(self, sprite):
        if sprite.rect.x % self.cell_size == 0 and sprite.rect.y % self.cell_size == 0:
            return True
        return False

    def find_path(self, sprite):
        if sprite.vulnerable == True:
            target = [sprite.vulnerable_target[0], sprite.vulnerable_target[1]]
        else:
            target = [self.pacman.rect.x//self.cell_size, self.pacman.rect.y//self.cell_size]

        path = self.bfs([sprite.rect.x//self.cell_size, sprite.rect.y//self.cell_size]
            , target)
        if len(path) >= 2:
            return path[1]
        return path[0]

    def neighbour_is_inside_matrix(self, neighbour, current_cell):
        if neighbour[0]+current_cell[0] >= 0 and neighbour[0]+current_cell[0] < len(self.level[0]):
            if neighbour[1]+current_cell[1] >= 0 and neighbour[1]+current_cell[1] < len(self.level):
                return True
        return False

    def bfs(self, starting_cell, target_cell):
        queue = deque()
        visited = []
        path = []
        queue.append(starting_cell)
        while queue: # pylint: disable=too-many-nested-blocks
                     # nested blocks can not be avoided in this algorithm
            current_cell = queue.popleft()
            visited.append(current_cell)

            if current_cell == target_cell:
                break

            for neighbour in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if self.neighbour_is_inside_matrix(neighbour, current_cell):
                    next_cell = [neighbour[0]+current_cell[0],
                        neighbour[1]+current_cell[1]]
                    if next_cell not in visited and self.level[next_cell[1]][next_cell[0]] != 1:
                        queue.append(next_cell)
                        path.append([current_cell, next_cell])
        direction = [target_cell]
        while target_cell != starting_cell:
            for step in path:
                if step[1] == target_cell:
                    target_cell = step[0]
                    direction.insert(0, step[0])
        return direction

    def position_pacman_and_ghosts_to_start(self):
        for ghost in self.ghosts:
            ghost.kill()

        self.all_sprites.remove(self.ghosts)

        self.pacman.kill()
        self.all_sprites.remove(self.pacman)

        for x in range(1, 5):
            self.revive_ghost(Ghost(x, 0, 0))

        self.pacman = Pacman(8*self.cell_size, 11*self.cell_size)
        self.all_sprites.add(self.pacman)


