# Arkkitehtuurikuvaus
## Pakkausrakenne
Ohjelma muodostuu seuraavista pakkauksista: assets, gamelogic, levels, sprites ja ui. Näistä tärkeimmät ovat gamelogic, joka sisältää pelin toimintalogiikkaan liittyvän koodin ja ui, joka sisältää käyttöliittymään liittyvän koodin. Assets sisältää png-kuvia, joita sprites-pakkauksen luokat käyttävät. Sprites sisältää kaikki luokat, joista pelimaailman oliot rakentuvat. Levels pakkauksessa on pelikentän pohja ruudukkona.
![Pakkauskaavio](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/pakkauskaavio.png)

## Sovelluslogiikka
Pelin käynnistys tapahtuu app.py-tiedostosta. App-luokassa luodaan Level-luokan instanssi, joka annetaan parametrinä Gameloop luokan määrityksessä. Gameloop-luokka muodostuu kolmesta päämetodista: 
- draw_starting_screen
- gameloop
- gameover

Nämä metodin suoritetaan tässä järjestyksessä. Jokaisella metodilla on alussa initialize-alkuinen apumetodin kutsu, jossa ruudun sisältö piirretään ja tehdään tarvittavat tietokannan toimenpiteet. Tämän jälkeen suoritetaan silmukassa metodia, joka tarkistaa pygame-event tapahtumia. Tarkistettavat asiat vaihtelevat siitä, missä vaiheessa pelin suoritus on menossa. Esimerkiksi draw_starting_screen metodin aikana tarkistetaan painaako pelaaja välilyöntiä. Gameloop-metodissa taas fokus on pelaajan painamilla nuolinäppäimillä. Gameover-metodissa on omat toimintonsa sille saako pelaaja laittaa nimensä huipputuloksiin vai ei.

Pelin toiminnoista suurin osa toteutetaan handle_gameloop_events()-metodissa event-silmukassa. Peli etenee kierroksittain. Jokaisen kierroksen aikana:
- Tarkistetaan painoiko pelaaja nuolinäppäintä
- Päivitetään kierros
- Tarkistetaan tapahtuiko törmäystä (tässä tapauksessa törmäys tarkoittaa tilannetta, jossa elämät loppuvat ja peli päättyy).

Silmukassa ollessa pelin tapahtumat toteutetaan Level-luokan metodikutsuilla ja muutamassa tapauksessa spriten (Ghost tai Pacman) metodeilla.

## Luokkakaavio keskeisistä luokista
```mermaid
classDiagram
	Level "1" --> "1" Gameloop
	Gameloop "1" --> "1" App
	Pacman "1" --> "1" Level
	Wall "*" --> "1" Level
	Floor "*" --> "1" Level
	Pellet "*" --> "1" Level
	Powerpellet "*" --> "1" Level
	Ghost "4" --> "1" Level
```

## Sekvenssidiagrammi Pacman-luokan spriten liikuttamisesta. 
Kyseisessä tilanteessa Pacman liikkuu y-akselilla alaspäin.
```mermaid
sequenceDiagram
	Note left of Gameloop: event.key == pygame.K_DOWN:
	Gameloop->>Pacman: new_direction = (0, CELL_SIZE)
	Gameloop->>Level: move_pacman(new_direction)
	Note right of Level: if centered(self.pacman)
	Note right of Level: if moving_is_possible(new_direction)
	Level->>Pacman: direction = new_direction
	Pacman-->>Level: ;
	Note right of Level: if moving_is_possible(direction)
	Level->>Pacman: Rect.move_ip(direction[0], direction[1])
	Pacman-->>Level: ;
	Note right of Level: self.pacman_eats()
	Level-->>Gameloop: ;
```
Tapahtumaketju update_round()-metodia kutsuttaessa.
```mermaid
sequenceDiagram
	Gameloop->>Gameloop: self.move_ghosts()
	Gameloop->>Level: move_pacman(pacman.new_direction)
	Gameloop->>Gameloop: update_score()
	Note left of Gameloop: score_text.render(), screen.blit(score_text)
	Note left of Gameloop: pygame.display.update()
	Gameloop->>Level: if all_pellets_eaten()
	Gameloop->>Gameloop: start_over_with_pellets()
	Gameloop->>Level: all_sprites.draw(screen)
	Gameloop->>Gameloop: clock.tick(10)
```
