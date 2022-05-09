import os
import sys
import sqlite3
import pygame
from levels.layouts import CELL_SIZE


class Gameloop:
    def __init__(self, level, screen, clock, size):
        """Luodaan muuttujat vaadittaville parametreille.

        Args:
            level: Level-luokan instanssi.
            screen: Pygamen display-olio.
            clock: Pygamen kello.
            size: Solun koko pikseleinä.
        """
        self.screen = screen
        self.level = level
        self.size = size
        self.clock = clock
        self.font = pygame.font.SysFont('arial black', 16)
        self.score_box = pygame.Rect(40, 0, 100, 30)

    def draw_starting_screen(self):
        """Piirretään aloitusruutu initialize_starting_screen-metodilla ja
        käynnistetään silmukka tapahtumien käsittelyä varten.
        """
        self.initialize_starting_screen()

        while True:
            handle_events = self.handle_starting_events()
            if handle_events is False:
                break
            if handle_events is None:
                sys.exit()

    def gameloop(self):
        """Piirretään peliruutu initialize_gameloop-metodilla ja käynnistetään
        silmukka tapahtumien käsittelyä varten.
        """
        self.initialize_gameloop()

        while True:
            handle_events = self.handle_gameloop_events()
            if handle_events is False:
                break

    def gameover(self):
        """Piirretään game over-ruutu initialize_gameover-metodilla ja käynnistetään
        silmukka tapahtumien käsittelyä varten.
        """
        self.initialize_gameover()

        while True:
            if self.handle_gameover_events() is False:
                break
            name_text = self.font.render(
                self.user_text, False, (255, 255, 255))
            self.screen.blit(name_text, self.input_box)
            pygame.display.flip()
            self.clock.tick(60)

    def initialize_starting_screen(self):
        self.screen.fill((0, 0, 0))
        highscore_font = pygame.font.SysFont('arial black', 20)
        start_text = self.font.render(
            "START GAME BY PRESSING SPACE", False, (200, 150, 100))
        highscore_text = highscore_font.render(
            "HIGHSCORES", False, (107, 183, 210))
        logo_image = pygame.image.load(
            os.path.join(os.path.dirname(__file__), "..", "assets", "logo.png")
        )
        self.screen.blit(logo_image, (100, 200))
        self.screen.blit(start_text, (100, 300))
        self.screen.blit(highscore_text, (170, 0))
        self._get_highscores_from_db()
        pygame.display.update()

    def initialize_gameloop(self):
        self.screen.fill((0, 0, 0))
        pygame.draw.rect(self.screen, (0, 0, 0), self.score_box)
        self._update_lives()
        self.level.all_sprites.draw(self.screen)
        pygame.display.update()

    def initialize_gameover(self):
        self.screen.fill((0, 0, 0))
        gameover_text = self.font.render(
            "GAME OVER", False, (190, 150, 100))
        score_text = self.font.render(
            f"SCORE: {self.level.score}", False, (107, 183, 210))
        score_check = self._check_highscores_from_db()
        if self.level.score > score_check:
            self.input_box = pygame.Rect(190, 100, 100, 30)
            self.user_text = ''
        self.screen.blit(score_text, (200, 0))
        self.screen.blit(gameover_text, (200, 200))
        pygame.draw.rect(self.screen, (0, 0, 0), self.input_box)
        pygame.display.update()

    def handle_starting_events(self):
        """Tarkistetaan tapahtumat ja palautetaan jokin arvo
        jos painettu näppäin on välilyönti, escape tai
        ikkuna on suljettu.

        Returns:
            False, jos painettu näppäin on välilyönti. Escape-näppäimestä
            tai quit-tapahtumasta palautetaan None, jolloin ohjelma suljetaan.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    return False
                if event.key == pygame.K_ESCAPE:
                    return None
            if event.type == pygame.QUIT:
                return None
        return True

    def handle_gameloop_events(self):
        """Tarkistetaan itse pelin aikaiset tapahtumat. Jos painettu näppäin on
        jokin nuolinäppäimistä, asetetaan Pacman-luokan spritelle uusi suunta.
        Tämän jälkeen päivitetään kierroksen tapahtumat ja tarkistetaan tapahtuuko
        törmäystä.

        Returns:
            Jos painettu näppäin on escape, tapahtuma on quit-tyyppinen tai pacman-sprite
            törmää haamuun eikä elämiä enää ole, palautetaan False.
        """
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

        self._update_round()

        if self.check_collision():
            return False
        return True

    def handle_gameover_events(self):
        """Tarkistetaan game over-ruudun aikaset tapahtumat.

        Returns:
            False, jos painetaan escape-näppäintä tai tapahtuman tyyppi on quit.
        """
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return False
                if event.key == pygame.K_BACKSPACE:
                    self.user_text = self.user_text[:-1]
                    pygame.draw.rect(self.screen, (0, 0, 0), self.input_box)
                if event.key == pygame.K_RETURN:
                    self.enter_name_to_db()
                    return False
                else:
                    self.user_text += event.unicode
            if event.type == pygame.QUIT:
                return False
        return True

    def _get_highscores_from_db(self):
        connection = sqlite3.connect('highscores.db')
        cur = connection.cursor()
        y_coordinate = 2*CELL_SIZE
        cur.execute(
            'SELECT player, score FROM highscores ORDER BY score DESC LIMIT 3')
        if cur.fetchall() == []:
            no_scores_text = self.font.render(
                "NO SCORES YET", False, (107, 183, 210))
            self.screen.blit(no_scores_text, (170, y_coordinate))

        for player, score in cur.execute('SELECT player, score FROM highscores ORDER BY score DESC LIMIT 3'):
            player_score = player + ": " + str(score)
            highscores = self.font.render(player_score, False, (107, 183, 210))
            self.screen.blit(highscores, (170, y_coordinate))
            y_coordinate += CELL_SIZE
        connection.close()

    def _check_highscores_from_db(self):
        connection = sqlite3.connect('highscores.db')
        cur = connection.cursor()
        cur.execute('SELECT score FROM highscores ORDER BY score ASC LIMIT 3')
        result = cur.fetchone()
        connection.close()
        if result == None:
            return 0
        return result[0]

    def enter_name_to_db(self):
        connection = sqlite3.connect('highscores.db')
        cur = connection.cursor()
        cur.execute("INSERT INTO highscores VALUES (?, ?)",
                    (self.user_text, self.level.score))
        connection.commit()
        connection.close()

    def _update_score(self):
        score_text = self.font.render(
            f"SCORE: {self.level.score}", False, (107, 183, 210))
        self.screen.fill((0, 0, 0), self.score_box)
        self.screen.blit(score_text, self.score_box)

    def _update_lives(self):
        lives_text = self.font.render(
            f"LIVES: {self.level.lives}", False, (107, 183, 210))
        self.screen.blit(lives_text, (400, 0))

    def _update_round(self):
        self.move_ghosts()
        self.level.move_pacman(self.level.pacman.new_direction)
        self._update_score()
        pygame.display.update()

        if self.level.all_pellets_eaten():
            self.start_over_with_pellets()

        self.level.all_sprites.draw(self.screen)
        self.clock.tick(10)

    def move_ghosts(self):
        """Liikutetaan kaikki haamut.
        """
        for ghost in self.level.ghosts:
            self.level.move_ghost(ghost)

    def check_collision(self):
        """Tarkistetaan törmääkö pacman-sprite ghost-spritejen kanssa
        ja tarvittaessa aloitetaan uudelleen tai näytetään game over-ruutu.

        Returns:
            True jos peli päättyy, False jos elämiä on jäljellä. None jos törmäystä
            ei tapahtunut.
        """
        collision = self.level.pacman_meets_ghost()
        if collision and self.level.lives >= 0:
            pygame.time.delay(1000)
            self.start_over()
            return False
        if collision and self.level.lives < 0:
            pygame.time.delay(1000)
            self.gameover()
            return True
        return None

    def start_over(self):
        """Aloitetaan uudelleen kun pacman-sprite menettää elämän.
        """
        self.screen.fill((0, 0, 0))
        self._update_lives()
        self._update_score()
        self.level.position_pacman_and_ghosts_to_start()
        self.level.all_sprites.draw(self.screen)
        pygame.display.update()

    def start_over_with_pellets(self):
        """Aloitetaan uudelleen kun kaikki pelletit on syöty.
        """
        pygame.time.delay(1500)
        self.level.cleared += 1
        self.level.initialize_sprites()
        self.level.position_pacman_and_ghosts_to_start()
