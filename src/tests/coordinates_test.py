import unittest
from level import Level

test_level = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 0, 1, 3, 1, 1, 0, 1, 0, 1],
              [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
              [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
              [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
              [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
              [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
              [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
size = 50


class TestLevel(unittest.TestCase):

    def setUp(self):
        self.level = Level(test_level, size)
        self.pacman = self.level.pacman
        self.pellets = self.level.pellets

    def coordinates_match(self, sprite, x, y):
        self.assertEqual(sprite.rect.x, x)
        self.assertEqual(sprite.rect.y, y)

    def test_coordinates_when_starting(self):
        self.coordinates_match(self.pacman, size * 3, size * 2)

    def test_moving_down(self):
        self.level.move_pacman(y=50)
        self.coordinates_match(self.pacman, size * 3, size * 3)

    def test_moving_up(self):
        self.level.move_pacman(y=-50)
        self.coordinates_match(self.pacman, size * 3, size * 1)

    def test_not_going_through_walls(self):
        self.level.move_pacman(x=-50)
        self.coordinates_match(self.pacman, size * 3, size * 2)

    def test_pellets_disappear_when_eaten(self):
        all_pellets = len(self.pellets)
        self.level.move_pacman(y=50)
        one_pellet_less = len(self.pellets)
        self.assertLess(one_pellet_less, all_pellets)

    def test_pellets_remain_same_if_nothing_to_eat(self):
        self.level.move_pacman(y=50)
        all_pellets = len(self.pellets)
        self.level.move_pacman(y=-50)
        pellets_after_moving = len(self.pellets)
        self.assertEqual(pellets_after_moving, all_pellets)
