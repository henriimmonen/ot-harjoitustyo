import os
import pygame

dirname = os.path.dirname(__file__)


class Floor(pygame.sprite.Sprite):
    """Luodaan lattiaruutua kuvaava sprite.
    """
    def __init__(self, coordinate_x=0, coordinate_y=0):
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "floor.png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = coordinate_x
        self.rect.y = coordinate_y
