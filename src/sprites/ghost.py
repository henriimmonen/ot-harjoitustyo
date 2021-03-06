import os
import pygame

dirname = os.path.dirname(__file__)


class Ghost(pygame.sprite.Sprite):
    def __init__(self, number, coordinate_x=0, coordinate_y=0):  # pylint: disable=too-many-statements
        """Luodaan Ghost-luokan sprite.

        Args:
            number: Numero, jonka perusteella haamu saa kuvan ja oman vulnerable-
            kohteen.
            coordinate_x: Aloituskoordinaatti x.
            coordinate_y: Aloituskoordinaatti y.
        """
        super().__init__()
        if number == 1:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "ghost1.png")
            )
            self.speed = 6
            self.vulnerable_target = (2, 2)
            self.starting_point = (6, 6)
        elif number == 2:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "ghost2.png")
            )
            self.speed = 6
            self.vulnerable_target = (14, 2)
            self.starting_point = (10, 6)
        elif number == 3:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "ghost3.png")
            )
            self.speed = 9
            self.vulnerable_target = (2, 14)
            self.starting_point = (6, 7)
        else:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "ghost4.png")
            )
            self.speed = 12
            self.vulnerable_target = (14, 14)
            self.starting_point = (10, 7)
        self.vulnerable = False
        self.rect = self.image.get_rect()
        self.rect.x = coordinate_x
        self.rect.y = coordinate_y
        self.direction = (0, 0)
        self.number = number

    def set_image(self):
        """Jos luokan sprite on vulnerable-tilassa, kuva on valkoinen.
        Muulloin normaali numeron mukainen kuva.
        """
        if self.vulnerable is True:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets", "ghost.png")
            )
        else:
            self.image = pygame.image.load(
                os.path.join(dirname, "..", "assets",
                             f"ghost{self.number}.png")
            )
