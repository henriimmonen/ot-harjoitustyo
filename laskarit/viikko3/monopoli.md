```mermaid
classDiagram
	Pelilauta "1" -- "40" Ruutu
	Pelilauta "1" -- "2..8" Pelaaja
	Ruutu "1" -- "*" Pelinappula
	Pelinappula "1" -- "1" Pelaaja
	Nopat -- "*" Pelaaja
	Nopat .. Pelinappula
	Class Ruutu {
	    seuraava_ruutu()
	}
```
