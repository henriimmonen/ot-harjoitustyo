# Käyttöohje

- Ennen pelin pelaamista täytyy olla asennettuna [sqlite3](https://www.sqlite.org/index.html), [pygame](https://www.pygame.org/news) ja [poetry](https://python-poetry.org/).
- Lataa pelin viimeisin [release](https://github.com/henriimmonen/ot-harjoitustyo/releases/tag/Viikko6).
- Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla `poetry install`.
- Tämän jälkeen ohjelman käynnistäminen tapahtuu juurihakemistosta komennolla `poetry run invoke start`.
- Muita komentoja, joita voit suorittaa ovat: `poetry run invoke test` (ajaa pelin testit), `poetry run invoke coverage` (tarkistaa testien kattavuuden), `poetry run invoke coverage-report` (tarkistaa testien kattavuuden ja muodostaa tästä raportin hmtlcov/index.html tiedostoon), `poetry run invoke lint`(suorittaa pylint-pisteytyksen pelin lähdekoodille) ja `poetry run invoke format`(muotoilee lähdekoodin autopep8:lla). 
- Aloituskomennon jälkeen peli käynnistyy aloitusruutuun, josta pääset pelaamaan painamalla välilyöntiä. Tässä ruudussa näet kolme parasta pelaajaa pisteineen (jos sellaisia jo on).
- Ohjelman voi sulkea missä tahansa vaiheessa Esc-näppäimellä tai painamalla yläkulman vinoristiä. 
- Peliä ohjataan nuolinäppäimillä. Tavoitteena on syödä kaikki pelikentän nappulat ennen kuin elämät loppuvat.
- Jokaisen kerran kun saat tyhjennettyä koko kentän, haamujen nopeus kasvaa ja kenttä alkaa alusta.
- Peli jatkuu kunnes kaikki elämät on käytetty.
- Jos saatu kerättyä enemmän pisteitä, kuin kolmanneksi paras pelaaja, voit laittaa oman nimesi ns. leaderboardille. 
