from collections import deque
import pygame
from sprites.pacman import Pacman
from sprites.wall import Wall
from sprites.floor import Floor
from sprites.pellet import Pellet
from sprites.powerpellet import PowerPellet
from sprites.ghost import Ghost
from levels.layouts import LEVEL_1, CELL_SIZE


class Level: # pylint: disable=too-many-instance-attributes
    """Luokka, joka vastaa pelilogiikasta.

    Attributes: level_map: pelattava kenttä ruudukkona.
                cell_size: luotavan pohjan solujen koko pikseleinä.
    """
    def __init__(self):
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.power_pellets = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.pacman = None
        self.timer = pygame.time.get_ticks()
        self.score = 0
        self.lives = 3
        self.cleared = 0
        self.initialize_sprites()

    def initialize_sprites(self): # pylint: disable=too-many-statements
                                  # statements are required to initialize
        """Luodaan spritet käyttäen annettua ruudukkoa.

        Args:
            level_map: pelattava kenttä ruudukkona.
        """
        level_height = len(LEVEL_1)
        level_width = len(LEVEL_1[0])

        for height in range(level_height):
            for width in range(level_width):
                normalized_y = height * CELL_SIZE
                normalized_x = width * CELL_SIZE

                if LEVEL_1[height][width] == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.pellets.add(Pellet(normalized_x, normalized_y))

                elif LEVEL_1[height][width] == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))

                elif LEVEL_1[height][width] == 2:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.power_pellets.add(
                        PowerPellet(normalized_x, normalized_y))

                elif LEVEL_1[height][width] == 3:
                    self.pacman = Pacman(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif LEVEL_1[height][width] == 4:
                    self.ghosts.add(Ghost(1, normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif LEVEL_1[height][width] == 5:
                    self.ghosts.add(Ghost(2, normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif LEVEL_1[height][width] == 6:
                    self.ghosts.add(Ghost(3, normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif LEVEL_1[height][width] == 7:
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

    def _moving_is_possible(self, sprite):
        sprite.rect.move_ip(
            sprite.direction[0]//sprite.speed, sprite.direction[1]//sprite.speed)
        crashing = pygame.sprite.spritecollide(sprite, self.walls, False)
        can_move = not crashing
        sprite.rect.move_ip(-sprite.direction[0] //
                            sprite.speed, -sprite.direction[1]//sprite.speed)
        return can_move

    def _pacman_eats(self):
        if pygame.sprite.spritecollide(self.pacman, self.pellets, True):
            self.score += 10
        elif pygame.sprite.spritecollide(self.pacman, self.power_pellets, True):
            self.score += 20
            self._ghosts_are_vulnerable()

    def _ghosts_are_vulnerable(self):
        self.timer = pygame.time.get_ticks()
        for ghost in self.ghosts:
            ghost.vulnerable = True
            ghost.set_image()

    def pacman_meets_ghost(self):
        """Metodi tarkistaa törmäävätkö pacman-sprite ja joku haamuista.
        Jos jokin törmää pygamen spritecollide metodin mielestä, tarkistetaan onko
        haamu vulnerable-tilassa. Jos haamu ei ole vulnerable-tilassa, palautetaan True ja
        vähennetään elämiä, mutta vasta kun koordinaatit ovat tarpeeksi lähellä
        toisiaan.

        Returns:
            Boolean arvo törmäävätkö pacman- ja ghost-sprite. False viittaa tilanteeseen,
            jossa ei menetetä elämää eli peli ei ala alkuasetelmasta.
        """
        list_of_colliding = pygame.sprite.spritecollide(
            self.pacman, self.ghosts, False)
        if len(list_of_colliding) == 0:
            return False
        for ghost in list_of_colliding:
            if self.pacman.rect.x == ghost.rect.x and abs(self.pacman.rect.y -
                ghost.rect.y) <= CELL_SIZE//2:
                if self._ghost_vulnerable(ghost):
                    return False
                self.lives -= 1
                return True
            if self.pacman.rect.y == ghost.rect.y and abs(self.pacman.rect.x -
                ghost.rect.x) <= CELL_SIZE//2:
                if self._ghost_vulnerable(ghost):
                    return False
                self.lives -= 1
                return True
        return False

    def _ghost_vulnerable(self, sprite):
        if sprite.vulnerable is True:
            self.score += 100
            sprite.kill()
            self.revive_ghost(sprite)
            return True
        return False

    def revive_ghost(self, ghost):
        """Ghost-sprite luodaan uudelleen numeron mukaiseen lähtöruutuun ja speed_up_ghost-
        metodi tarkistaa tarvitseeko ghost-spriten liikkumista nopeuttaa.

        Args:
            ghost: Ghost-luokan sprite.
        """
        starting_point = 150 + 30*ghost.number
        new_ghost = Ghost(ghost.number, starting_point, 210)
        self._speed_up_ghost(new_ghost)
        self.ghosts.add(new_ghost)
        self.all_sprites.add(self.ghosts)

    def _speed_up_ghost(self, ghost):
        if self.cleared >= 1:
            ghost.speed = max(ghost.speed-(self.cleared*3), 3)

    def move_pacman(self, direction):
        """Pacman-luokan spriten liikuttaminen.

        Args:
            direction: Tuple suunnasta, johon spriten tulisi liikkua.
        """
        self._check_timer()
        self.pacman.new_direction = direction
        if self._centered(self.pacman):
            self.pacman.direction = self.pacman.new_direction

        if self._moving_is_possible(self.pacman):
            self.pacman.set_image()
            self.pacman.rect.move_ip(
                self.pacman.direction[0]//self.pacman.speed,
                self.pacman.direction[1]//self.pacman.speed)
            self._pacman_eats()

    def move_ghost(self, sprite):
        if self._centered(sprite):
            next_cell = self._find_path(sprite)
            x_coordinate = next_cell[0] - sprite.rect.x//CELL_SIZE
            y_coordinate = next_cell[1] - sprite.rect.y//CELL_SIZE
            sprite.direction = (x_coordinate, y_coordinate)
            sprite.rect.move_ip(x_coordinate*(CELL_SIZE//sprite.speed),
                                y_coordinate*(CELL_SIZE//sprite.speed))
        else:
            sprite.rect.move_ip(sprite.direction[0] * (
                CELL_SIZE//sprite.speed), sprite.direction[1] * (CELL_SIZE//sprite.speed))

    def _check_timer(self):
        if self.timer:
            if pygame.time.get_ticks() - self.timer >= 5000:
                for ghost in self.ghosts:
                    ghost.vulnerable = False
                    ghost.set_image()

    def _centered(self, sprite):
        if sprite.rect.x % CELL_SIZE == 0 and sprite.rect.y % CELL_SIZE == 0:
            return True
        return False

    def _find_path(self, sprite):
        if sprite.vulnerable is True:
            target = [sprite.vulnerable_target[0], sprite.vulnerable_target[1]]
        else:
            target = [self.pacman.rect.x//CELL_SIZE,
                      self.pacman.rect.y//CELL_SIZE]

        path = self._bfs([sprite.rect.x//CELL_SIZE,
                        sprite.rect.y//CELL_SIZE], target)
        if len(path) >= 2:
            return path[1]
        return path[0]

    def _neighbour_is_inside_matrix(self, neighbour, current_cell):
        if neighbour[0]+current_cell[0] >= 0 and neighbour[0]+current_cell[0] < len(LEVEL_1[0]):
            if neighbour[1]+current_cell[1] >= 0 and neighbour[1]+current_cell[1] < len(LEVEL_1):
                return True
        return False

    def _bfs(self, starting_cell, target_cell):
        queue = deque()
        visited = []
        path = []
        queue.append(starting_cell)
        while queue:  # pylint: disable=too-many-nested-blocks
                      # nested blocks can not be avoided in this algorithm
            current_cell = queue.popleft()
            visited.append(current_cell)

            if current_cell == target_cell:
                break

            for neighbour in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                if self._neighbour_is_inside_matrix(neighbour, current_cell):
                    next_cell = [neighbour[0]+current_cell[0],
                                 neighbour[1]+current_cell[1]]
                    if next_cell not in visited and LEVEL_1[next_cell[1]][next_cell[0]] != 1:
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
        """Tuhotaan kaikki Ghost-luokan spritet ja Pacman-luokan sprite ja luodaan ne uudelleen
        lähtötilanteeseen.
        """
        for ghost in self.ghosts:
            ghost.kill()

        self.all_sprites.remove(self.ghosts)

        self.pacman.kill()
        self.all_sprites.remove(self.pacman)

        for number in range(1, 5):
            self.revive_ghost(Ghost(number, 0, 0))

        self.pacman = Pacman(8*CELL_SIZE, 11*CELL_SIZE)
        self.all_sprites.add(self.pacman)

    def all_pellets_eaten(self):
        """Tarkistetaan onko kaikki Pellet- ja Powerpellet-luokkien spritet on syöty.

        Returns:
            Boolean arvo True jos kaikki pelletit on syöty, muuten False.
        """
        if len(self.pellets) == 0 and len(self.power_pellets) == 0:
            return True
        return False
