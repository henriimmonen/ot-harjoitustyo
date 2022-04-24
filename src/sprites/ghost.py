import os
import pygame

dirname = os.path.dirname(__file__)

class Ghost(pygame.sprite.Sprite):
    def __init__(self, number, coordinate_x=0, coordinate_y=0):
        super().__init__()
        if number == 1:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "ghost1.png")
            )
        elif number == 2:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "ghost2.png")
            )
        elif number == 3:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "ghost3.png")
            )
        else: 
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "ghost4.png")
            )

        self.rect = self.image.get_rect()
        self.rect.x = coordinate_x
        self.rect.y = coordinate_y
        self.direction = [0,0]