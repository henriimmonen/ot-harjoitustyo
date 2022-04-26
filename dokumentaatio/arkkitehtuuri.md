```mermaid
classDiagram
	Level "1" --> "1" Gameloop
	Gameloop "1" --> "1" App
	Pacman "1" --> "1" Level
	Wall "*" --> "1" Level
	Floor "*" --> "1" Level
	Pellet "*" --> "1" Level 
```

Sekvenssidiagrammi Pacman-spriten liikuttamisesta. Kyseisessä tilanteessa Pacman liikkuu y-akselilla alaspäin.
```mermaid
sequenceDiagram
	Gameloop->>Pacman: direction = [0, self.size]
	Gameloop->>Level: move_pacman()
	Note right of Level: if moving_is_possible()
	Level->>Pacman: Rect.move_ip(direction[0], direction[1])
	Note right of Level: self.pacman_eats()
```
