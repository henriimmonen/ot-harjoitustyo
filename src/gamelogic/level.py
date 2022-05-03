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
    """Luokka, joka vastaa pelilogiikasta.

    Attributes: level_map: pelattava kenttä ruudukkona.
                cell_size: luotavan pohjan solujen koko pikseleinä.
    """
    def __init__(self, level_map, cell_size):
        self.cell_size = cell_size
        self.level = level_map
        self.walls = pygame.sprite.Group()
        self.floors = pygame.sprite.Group()
        self.pellets = pygame.sprite.Group()
        self.power_pellets = pygame.sprite.Group()
        self.ghosts = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.pacman = None
        self.score = 0
        self.lives = 3
        self.cleared = 0
        self.timer = None
        self.initialize_sprites()

    def initialize_sprites(self): # pylint: disable=too-many-statements
                                  # statements are required to initialize
        """Luodaan spritet käyttäen annettua ruudukkoa.

        Args:
            level_map: pelattava kenttä ruudukkona.
        """
        level_height = len(self.level)
        level_width = len(self.level[0])

        for height in range(level_height):
            for width in range(level_width):
                normalized_y = height * self.cell_size
                normalized_x = width * self.cell_size

                if self.level[height][width] == 0:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.pellets.add(Pellet(normalized_x, normalized_y))

                elif self.level[height][width] == 1:
                    self.walls.add(Wall(normalized_x, normalized_y))

                elif self.level[height][width] == 2:
                    self.floors.add(Floor(normalized_x, normalized_y))
                    self.power_pellets.add(
                        PowerPellet(normalized_x, normalized_y))

                elif self.level[height][width] == 3:
                    self.pacman = Pacman(normalized_x, normalized_y)
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif self.level[height][width] == 4:
                    self.ghosts.add(Ghost(1, normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif self.level[height][width] == 5:
                    self.ghosts.add(Ghost(2, normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif self.level[height][width] == 6:
                    self.ghosts.add(Ghost(3, normalized_x, normalized_y))
                    self.floors.add(Floor(normalized_x, normalized_y))

                elif self.level[height][width] == 7:
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
        """Testaa törmääkö sprite liikkuessaan seinään.

        Args:
            sprite: mikä tahansa sprite-luokan olio.

        Returns:
            Boolean arvon törmääkö annettu sprite seinään.
        """
        sprite.rect.move_ip(
            sprite.direction[0]//sprite.speed, sprite.direction[1]//sprite.speed)
        crashing = pygame.sprite.spritecollide(sprite, self.walls, False)
        can_move = not crashing
        sprite.rect.move_ip(-sprite.direction[0] //
                            sprite.speed, -sprite.direction[1]//sprite.speed)
        return can_move

    def pacman_eats(self):
        """Tarkistaa pygamen metodilla törmäävätkö
        pacman-sprite ja pellet- tai powerpellet-sprite ja lisää pisteitä tämän mukaan.
        """
        if pygame.sprite.spritecollide(self.pacman, self.pellets, True):
            self.score += 10
        elif pygame.sprite.spritecollide(self.pacman, self.power_pellets, True):
            self.score += 20
            self.ghosts_are_vulnerable()

    def ghosts_are_vulnerable(self):
        """Asettaa Ghost-luokan spritet vulnerable-tilaan ja vaihtaa kuvan.
        """
        self.timer = pygame.time.get_ticks()
        for ghost in self.ghosts:
            ghost.vulnerable = True
            ghost.set_image()

    def pacman_meets_ghost(self):
        """Metodi tarkistaa törmäävätkö pacman-sprite ja joku haamuista.
        Jos haamu on vulnerable-tilassa, se kuolee ja uusi luodaan
        lähtöpaikkaan self.revive_ghost-metodilla. True palautetaan
        ainoastaan, kun pacman-sprite menettää elämän.

        Returns:
            Boolean arvo törmäävätkö pacman- ja ghost-sprite.
        """
        list_of_colliding = pygame.sprite.spritecollide(
            self.pacman, self.ghosts, False)
        for ghost in list_of_colliding:
            if ghost.vulnerable is True:
                self.score += 100
                ghost.kill()
                self.revive_ghost(ghost)
                return False
        if pygame.sprite.spritecollide(self.pacman, self.ghosts, False):
            self.lives -= 1
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
        self.speed_up_ghost(new_ghost)
        self.ghosts.add(new_ghost)
        self.all_sprites.add(self.ghosts)

    def speed_up_ghost(self, ghost):
        """Jos kenttiä on läpäisty yksi tai enemmän, haamun liikkumista nopeutetaan.

        Args:
            ghost: Ghost-luokan sprite.
        """
        if self.cleared >= 1:
            ghost.speed = max(ghost.speed-(self.cleared*3), 3)

    def move_pacman(self, direction):
        """Pacman-luokan spriten liikuttaminen.

        Args:
            direction: Tuple suunnasta, johon spriten tulisi liikkua.
        """
        self.check_timer()
        self.pacman.new_direction = direction
        if self.centered(self.pacman):
            self.pacman.direction = self.pacman.new_direction

        if self.moving_is_possible(self.pacman):
            self.pacman.set_image()
            self.pacman.rect.move_ip(
                self.pacman.direction[0]//self.pacman.speed,
                self.pacman.direction[1]//self.pacman.speed)
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
        if sprite.vulnerable is True:
            target = [sprite.vulnerable_target[0], sprite.vulnerable_target[1]]
        else:
            target = [self.pacman.rect.x//self.cell_size,
                      self.pacman.rect.y//self.cell_size]

        path = self.bfs([sprite.rect.x//self.cell_size,
                        sprite.rect.y//self.cell_size], target)
        if len(path) >= 2:
            return path[1]
        return path[0]

    def neighbour_is_inside_matrix(self, neighbour, current_cell):
        """Tarkistetaan kuuluuko annettu solu kentän sisälle.

        Args:
            neighbour: Naapurisolu.
            current_cell: Tämän hetkinen solu.

        Returns:
            Boolean arvo True, jos naapurisolu on ruudukon sisällä, muuten False.
        """
        if neighbour[0]+current_cell[0] >= 0 and neighbour[0]+current_cell[0] < len(self.level[0]):
            if neighbour[1]+current_cell[1] >= 0 and neighbour[1]+current_cell[1] < len(self.level):
                return True
        return False

    def bfs(self, starting_cell, target_cell):
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

        self.pacman = Pacman(8*self.cell_size, 11*self.cell_size)
        self.all_sprites.add(self.pacman)

    def all_pellets_eaten(self):
        """Tarkistetaan onko kaikki Pellet- ja Powerpellet-luokkien spritet on syöty.

        Returns:
            Boolean arvo True jos kaikki pelletit on syöty, muuten False.
        """
        if len(self.pellets) == 0 and len(self.power_pellets) == 0:
            return True
        return False
