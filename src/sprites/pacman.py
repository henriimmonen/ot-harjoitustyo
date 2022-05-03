import os
import pygame

dirname = os.path.dirname(__file__)


class Pacman(pygame.sprite.Sprite):
    def __init__(self, coordinate_x=0, coordinate_y=0):
        """Luodaan Pacman-luokan sprite

        Args:
            coordinate_x: Aloituskoordinaatti x.
            coordinate_y: Aloituskoordinaatti y.
        """
        super().__init__()
        self.image = pygame.image.load(
            os.path.join(dirname, "..", "assets", "pacman.png")
        )
        self.rect = self.image.get_rect()
        self.rect.x = coordinate_x
        self.rect.y = coordinate_y
        self.direction = (0, 0)
        self.new_direction = (0, 0)
        self.speed = 2

    def set_image(self):
        """Päivitetään kuva vastaamaan kulkusuuntaa.
        """
        if self.direction[0] > 0 and self.direction[1] == 0:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "pacman.png")
            )

        if self.direction[0] < 0 and self.direction[1] == 0:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "pacman_left.png")
            )

        if self.direction[0] == 0 and self.direction[1] > 0:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "pacman_down.png")
            )

        if self.direction[0] == 0 and self.direction[1] < 0:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "pacman_up.png")
            )
