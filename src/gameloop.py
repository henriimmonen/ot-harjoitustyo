import sys
import pygame


class Gameloop:
    def __init__(self, level, screen, clock, size):
        self.screen = screen
        self.level = level
        self.size = size
        self.clock = clock
        self.font = pygame.font.SysFont('arial black', 16)
        self.score = pygame.Rect(40, 0, 100, 30)

    def draw_starting_screen(self):
        self.initialize_starting_screen()

        while True:
            if self.handle_starting_events() is False:
                break

    def gameloop(self):
        self.initialize_gameloop()

        while True:
            if self.handle_gameloop_events() is False:
                break

    def initialize_starting_screen(self):
        self.screen.fill((0, 0, 0))

        start_text = self.font.render(
            "START GAME BY PRESSING SPACE", False, (200, 150, 100))
        highscore_text = self.font.render(
            "HIGHSCORES", False, (107, 183, 210, 1))
        self.screen.blit(start_text, (100, 200))
        self.screen.blit(highscore_text, (190, 0))
        pygame.display.update()

    def initialize_gameloop(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), self.score)
        self.level.all_sprites.draw(self.screen)
        pygame.display.update()

    def handle_starting_events(self): # pylint: disable=inconsistent-return-statements
                                      # could not figure out a way to avoid this
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

    def handle_gameloop_events(self): # pylint: disable=inconsistent-return-statements
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_LEFT:
                    self.level.pacman.direction = (-self.size, 0)
                if event.key == pygame.K_RIGHT:
                    self.level.pacman.direction = (self.size, 0)
                if event.key == pygame.K_UP:
                    self.level.pacman.direction = (0, -self.size)
                if event.key == pygame.K_DOWN:
                    self.level.pacman.direction = (0, self.size)
            if event.type == pygame.QUIT:
                return False
        self.update_round()
        if self.check_collision():
            return False

    def update_score(self):
        score_text = self.font.render(f"SCORE: {self.level.score}", True, (107, 183, 210, 1))
        self.screen.fill((0, 0, 0), self.score)
        self.screen.blit(score_text, self.score)

    def update_round(self):
        self.move_ghosts()
        self.level.move_pacman(self.level.pacman.direction)

        self.update_score()
        pygame.display.update()
        self.level.all_sprites.draw(self.screen)
        self.clock.tick(10)

    def move_ghosts(self):
        for ghost in self.level.ghosts:
            self.level.move_ghost(ghost)

    def check_collision(self):
        collision = self.level.pacman_meets_ghost()
        if collision and self.level.lives >= 0:
            pygame.time.delay(1500)
            self.start_over()
        elif collision and self.level.lives == -1:
            return True

    def start_over(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), self.score)
        self.level.position_pacman_and_ghosts_to_start()
        self.level.all_sprites.draw(self.screen)
        pygame.display.update()
