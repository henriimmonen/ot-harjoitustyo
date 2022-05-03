import sys
import pygame


class Gameloop:
    def __init__(self, level, screen, clock, size):
        self.screen = screen
        self.level = level
        self.size = size
        self.clock = clock
        self.font = pygame.font.SysFont('arial black', 16)
        self.score_box = pygame.Rect(40, 0, 100, 30)

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

    def gameover(self):
        self.initialize_gameover()

        while True:
            if self.handle_gameover_events() is False:
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
        pygame.draw.rect(self.screen, (0, 0, 0), self.score_box)
        self.update_lives()
        self.level.all_sprites.draw(self.screen)
        pygame.display.update()

    def initialize_gameover(self):
        self.screen.fill((0, 0, 0))
        gameover_text = self.font.render(
            "GAME OVER", False, (190, 150, 100))
        score_text = self.font.render(
            f"SCORE: {self.level.score}", False, (107, 183, 210))
        self.screen.blit(score_text, (200, 0))
        self.screen.blit(gameover_text, (200, 200))
        pygame.display.update()

    def handle_starting_events(self):  # pylint: disable=inconsistent-return-statements
        # could not figure out a way to avoid this
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            if event.type == pygame.QUIT:
                sys.exit()

    def handle_gameloop_events(self):  # pylint: disable=inconsistent-return-statements
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_LEFT:
                    self.level.pacman.new_direction = (-self.size, 0)
                if event.key == pygame.K_RIGHT:
                    self.level.pacman.new_direction = (self.size, 0)
                if event.key == pygame.K_UP:
                    self.level.pacman.new_direction = (0, -self.size)
                if event.key == pygame.K_DOWN:
                    self.level.pacman.new_direction = (0, self.size)
            if event.type == pygame.QUIT:
                return False

        self.update_round()

        if self.check_collision():
            return False

    def handle_gameover_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
            if event.type == pygame.QUIT:
                return False

    def update_score(self):
        score_text = self.font.render(
            f"SCORE: {self.level.score}", False, (107, 183, 210, 1))
        self.screen.fill((0, 0, 0), self.score_box)
        self.screen.blit(score_text, self.score_box)

    def update_lives(self):
        lives_text = self.font.render(
            f"LIVES: {self.level.lives}", False, (107, 183, 210, 1))
        self.screen.blit(lives_text, (400, 0))

    def update_round(self):
        self.move_ghosts()
        self.level.move_pacman(self.level.pacman.new_direction)
        self.update_score()
        pygame.display.update()

        if self.level.all_pellets_eaten():
            self.start_over_with_pellets()

        self.level.all_sprites.draw(self.screen)
        self.clock.tick(10)

    def move_ghosts(self):
        for ghost in self.level.ghosts:
            self.level.move_ghost(ghost)

    def check_collision(self):
        collision = self.level.pacman_meets_ghost()
        if collision and self.level.lives >= 0:
            pygame.time.delay(1000)
            self.start_over()
        elif collision and self.level.lives < 0:
            pygame.time.delay(1000)
            self.gameover()
            return True

    def start_over(self):
        self.screen.fill((0, 0, 0))
        self.update_lives()
        self.update_score()
        self.level.position_pacman_and_ghosts_to_start()
        self.level.all_sprites.draw(self.screen)
        pygame.display.update()

    def start_over_with_pellets(self):
        pygame.time.delay(1500)
        self.level.cleared += 1
        self.level.initialize_sprites(self.level.level)
        self.level.position_pacman_and_ghosts_to_start()

