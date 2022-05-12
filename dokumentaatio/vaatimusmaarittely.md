# Vaatimusmäärittely

## Sovelluksen tarkoitus
- Sovellus on versio suositusta Pac-Man pelistä. Pelin tarkoituksena on kerätä pisteitä ja varoa kentässä liikkuvia vihollisia saamasta sinua kiinni. 

## Käyttäjät
- Käyttäjinä toimivat pelin pelaajat. Muita tarpeellisia rooleja käyttäjille ei ole.
 
## Pelin toiminnallisuudet
- Peli alkaa aloitusruudulla, jossa näytetään ns. leaderboard kolmen parhaan pistesaldon keränneistä pelaajista (paikallisesti).
- Painamalla välilyöntiä, peli alkaa.
- Pelaaja liikuttaa hahmoa nuolinäppäimillä ympäri kenttää ja koittaa kerätä mahdollisimman monta pistettä.
- Pelissä on vaikeustasoja etenemisen mukaan. Pelaajaa jahtaavat haamut liikkuvat nopeampaa jokaisen pelikentän tyhjennyksen jälkeen.
- Haamut jahtaavat Pacman-hahmoa käyttäen leveyshakua.
- Pisteistä pidetään kirjaa ja pelin päätyttyä pelaajan saama pistesaldo näytetään ruudulla.
- Peli tarkistaa tietokannasta riittävätkö pisteet leaderboardille.
- Jos pisteet ylittävät kolmanneksi parhaan pelaajan pisteet, on mahdollista laittaa oma nimi leaderboardille.
- Jos pisteet eivät riitä, siitä kerrotaan pelaajalle.
- Kun game over-näkymä suljetaan, peli loppuu.
