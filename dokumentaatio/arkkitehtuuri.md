# Arkkitehtuurikuvaus
## Pakkausrakenne
Ohjelma muodostuu seuraavista pakkauksista: assets, gamelogic, levels, sprites ja ui. Näistä tärkeimmät ovat gamelogic, joka sisältää pelin toimintalogiikkaan liittyvän koodin ja ui, joka sisältää käyttöliittymään liittyvän koodin. Assets sisältää png-kuvia, joita sprites pakkauksen luokat käyttävät. Sprites sisältää kaikki luokat, joista pelimaailman oliot rakentuvat. Levels pakkauksessa on pelikentän pohja ruudukkona.

## Sovelluslogiikka
Pelin käynnistys tapahtuu app.py-tiedostosta. App-luokassa luodaan Level-luokan instanssi, joka annetaan parametrinä Gameloop luokan määrityksessä. Gameloop-luokasta kutsutaan ensin `draw_starting_screen` metodia joka piirtää näytölle aloitusruudun. Kun haluttua näppäintä painetaan, poistutaan tästä metodista ja kutsutaan `gameloop` metodia.

Tämä aloittaa itse pelin toiminnan. Gameloop-metodissa tarkistetaan silmukassa ensin onko jotakin näppäintä painettu, jonka jälkeen päivitetään tapahtumat. Silmukassa ollessa pelin tapahtumat toteutetaan Level-luokan metodikutsuilla ja muutamassa tapauksessa spriten (Ghost tai Pacman) metodeilla.

Tätä jatketaan kunnes elämät loppuvat, jolloin kutsutaan `gameover` metodia, joka piirtää näytölle tekstin "Game Over" ja näyttää pelaajan pistesaldon. 

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
	Gameloop->>Pacman: new_direction = (0, self.size)
	Gameloop->>Level: move_pacman(new_direction)
	Note right of Level: if centered(self.pacman)
	Level->>Pacman: direction = new_direction
	Pacman-->>Level: ;
	Note right of Level: if moving_is_possible()
	Level->>Pacman: Rect.move_ip(direction[0], direction[1])
	Pacman-->>Level: ;
	Note right of Level: self.pacman_eats()
	Level-->>Gameloop: ;
```
