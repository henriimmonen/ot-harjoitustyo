import unittest
import pygame
from level import Level

test_level = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 2, 0, 0, 0, 0, 0, 0, 2, 1],
              [1, 5, 1, 3, 1, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
              [1, 0, 1, 4, 0, 6, 7, 1, 0, 1],
              [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
              [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
              [1, 2, 0, 0, 0, 0, 0, 0, 2, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

test_pellet_level = [[1, 1, 1, 1],
                     [1, 0, 0, 1],
                     [1, 0, 3, 1],
                     [1, 1, 1, 1]]
size = 30


class TestLevel(unittest.TestCase):

    def setUp(self):
        self.level = Level(test_level, size)
        self.pellet_level = Level(test_pellet_level, size)
        self.pacman = self.level.pacman
        self.pellets = self.level.pellets
        self.power_pellets = self.level.power_pellets

        for ghost in self.level.ghosts:
            if ghost.number == 1:
                self.ghost1 = ghost
            if ghost.number == 3:
                self.ghost3 = ghost
            if ghost.number == 4:
                self.ghost4 = ghost

    def coordinates_match(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_pacmans_coordinates_when_starting(self):
        self.coordinates_match(self.pacman, size * 3, size * 2)

    def test_ghost1_coordinates_when_starting(self):
        self.coordinates_match(self.ghost1, size * 3, size * 4)

    def test_moving_down(self):
        self.level.move_pacman((0, size))
        self.level.move_pacman((0, size))
        self.coordinates_match(self.pacman, size * 3, size * 3)

    def test_moving_up(self):
        self.level.move_pacman((0, -size))
        self.level.move_pacman((0, -size))
        self.coordinates_match(self.pacman, size * 3, size * 1)

    def test_not_going_through_walls(self):
        self.level.move_pacman((-size, 0))
        self.coordinates_match(self.pacman, size * 3, size * 2)

    def test_pellets_disappear_when_eaten(self):
        all_pellets = len(self.pellets)
        self.level.move_pacman((0, size))
        pellets_after_moving = len(self.pellets)
        self.assertLess(pellets_after_moving, all_pellets)

    def test_pellets_remain_same_if_nothing_to_eat(self):
        self.level.move_pacman((0, size))
        all_pellets = len(self.pellets)
        self.level.move_pacman((0, -size))
        pellets_after_moving = len(self.pellets)
        self.assertEqual(pellets_after_moving, all_pellets)

    def test_powerpellets_disappear_when_eaten(self):
        all_power_pellets = len(self.power_pellets)
        self.level.move_pacman((0, -size))
        self.level.move_pacman((0, -size))
        for x in range(1,5):
            self.level.move_pacman((-size, 0))
        power_pellets_after_moving = len(self.power_pellets)
        self.assertLess(power_pellets_after_moving, all_power_pellets)

    def test_colliding_with_ghost_returns_true(self):
        for x in range(1,5):
            self.level.move_pacman((0, size))
        self.assertTrue(self.level.pacman_meets_ghost())

    def test_not_colliding_with_ghost_returns_false(self):
        self.level.move_pacman((0, size))
        self.assertFalse(self.level.pacman_meets_ghost())

    def test_ghost_starts_centered(self):
        self.assertEqual(self.level.centered(self.ghost1), True)

    def test_ghost_is_not_centered_after_first_move(self):
        self.level.move_ghost(self.ghost1)
        self.assertEqual(self.level.centered(self.ghost1), False)

    def test_bfs_finds_correct_path(self):
        path = self.level.find_path(self.ghost1)
        self.assertEqual(path, [3, 3])

    def test_bfs_returns_path0_if_next_to_pacman(self):
        self.level.move_ghost(self.ghost1)
        path = self.level.find_path(self.ghost1)
        self.assertEqual(path, [3, 2])
