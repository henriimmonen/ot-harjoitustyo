# Käyttöohje

- Ennen pelin pelaamista täytyy olla asennettuna [sqlite3](https://www.sqlite.org/index.html), [pygame](https://www.pygame.org/news) ja [poetry](https://python-poetry.org/).
- Lataa pelin viimeisin [release](https://github.com/henriimmonen/ot-harjoitustyo/releases/tag/Loppupalautus).
- Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla `poetry install`.
- Tämän jälkeen ohjelman käynnistäminen tapahtuu juurihakemistosta komennolla `poetry run invoke start`.
- Muita komentoja, joita voit suorittaa löytyvät projektin [README.md tiedostosta](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/README.md).
- Aloituskomennon jälkeen peli käynnistyy aloitusruutuun, josta pääset pelaamaan painamalla välilyöntiä. Tässä ruudussa näet kolme parasta pelaajaa pisteineen (jos sellaisia jo on).
- Ohjelman voi sulkea missä tahansa vaiheessa Esc-näppäimellä tai painamalla yläkulman vinoristiä. 
- Peliä ohjataan nuolinäppäimillä. Tavoitteena on syödä kaikki pelikentän nappulat ennen kuin elämät loppuvat.
- Jokaisen kerran kun saat tyhjennettyä koko kentän, haamujen nopeus kasvaa ja kenttä alkaa alusta.
- Peli jatkuu kunnes kaikki elämät on käytetty.
- Jos saatu kerättyä enemmän pisteitä, kuin kolmanneksi paras pelaaja, voit laittaa oman nimesi ns. leaderboardille. 
