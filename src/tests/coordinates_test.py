import unittest
import pygame
from level import Level

test_level = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 2, 0, 0, 0, 0, 0, 0, 2, 1],
              [1, 0, 1, 3, 1, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
              [1, 0, 1, 4, 4, 4, 4, 1, 0, 1],
              [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
              [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
              [1, 2, 0, 0, 0, 0, 0, 0, 2, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
size = 30


class TestLevel(unittest.TestCase):

    def setUp(self):
        self.level = Level(test_level, size)
        self.pacman = self.level.pacman
        self.pellets = self.level.pellets
        self.power_pellets = self.level.power_pellets

    def coordinates_match(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_pacmans_coordinates_when_starting(self):
        self.coordinates_match(self.pacman, size * 3, size * 2)
    
    def test_ghost1_coordinates_when_starting(self):
        self.coordinates_match(self.level.ghost1, size * 3, size * 4)

    def test_moving_down(self):
        self.level.move_pacman((0,size))
        self.coordinates_match(self.pacman, size * 3, size * 3)

    def test_moving_up(self):
        self.level.move_pacman((0,-size))
        self.coordinates_match(self.pacman, size * 3, size * 1)

    def test_not_going_through_walls(self):
        self.level.move_pacman((-size,0))
        self.coordinates_match(self.pacman, size * 3, size * 2)

    def test_pellets_disappear_when_eaten(self):
        all_pellets = len(self.pellets)
        self.level.move_pacman((0,size))
        pellets_after_moving = len(self.pellets)
        self.assertLess(pellets_after_moving, all_pellets)

    def test_pellets_remain_same_if_nothing_to_eat(self):
        self.level.move_pacman((0,size))
        all_pellets = len(self.pellets)
        self.level.move_pacman((0,-size))
        pellets_after_moving = len(self.pellets)
        self.assertEqual(pellets_after_moving, all_pellets)
    
    def test_powerpellets_disappear_when_eaten(self):
        all_power_pellets = len(self.power_pellets)
        self.level.move_pacman((0,-size))
        self.level.move_pacman((-size, 0))
        self.level.move_pacman((-size, 0))
        power_pellets_after_moving = len(self.power_pellets)
        self.assertLess(power_pellets_after_moving, all_power_pellets)

    def test_lives_remaining_is_reduced_when_colliding_with_ghost(self):
        self.level.move_pacman((0,size))
        self.level.move_pacman((0,size))
        self.assertTrue(self.level.pacman_meets_ghost())

    def test_not_colliding_with_ghost_returns_false(self):
        self.level.move_pacman((0, size))
        self.assertFalse(self.level.pacman_meets_ghost())