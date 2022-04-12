```mermaid
classDiagram
	Level "1" --> "1" Gameloop
	Gameloop "1" --> "1" App
	Pacman "1" --> "1" Level
	Wall "*" --> "1" Level
	Floor "*" --> "1" Level
	Pellet "*" --> "1" Level 
```

