# Changelog

## Viikko 3 
- Ensimmäiset luokat luotu. Index.py ja level.py vastaavat tällä hetkellä pelin käynnistämisestä ja kentän luomisesta. 
- Sprite-luokkia on: lattia, seinä, pacman. Myöhemmin lisätään ainakin haamu- ja piste-spritet.
- Level-luokan metodi moving_is_possible tarkastaa, ettei hahmo liiku seinien yli.
- Testit tarkastavat, että koordinaatit ovat pacmanillä oikein, eikä liikkumista tapahdu muualle kuin sallituille ruuduille.
 
## Viikko 4 
- Pelin pääluokka on App (app.py-tiedostossa). Pelitasoon liittyvä toiminnallisuus on luokassa Level ja gamelooppiin liittyvä toiminnallisuus luokassa Gameloop.
- Pelin käynnistyessä pelaajalle näytetään aloitusruutu, johon myöhemmin kerätään parhaimman pistesaldon saaneet pelaajat. Lisäksi tässä mäkymässä ohjeistetaan painamaan välilyöntiä, jotta itse peli alkaa. Tätä ensinäkymää jatkokehitetään tulevilla viikoilla. 
- Pacman liikkuu siihen suuntaan mihin nuolinäppäintä painetaan. Mikäli pelihahmo ei voi liikkua siihen suuntaan, liike pysähtyy.
- Lattiaruutujen päälle generoituu pellet-sprite, joita keräämällä yläruudussa näkyvä pistesaldo kasvaa. 

## Viikko 5 
- Pelin ulkonäköä viilattu. Seinäruudut kuvitettu GIMP-ohjelmalla ja lattiaruuduista poistettu reunukset. Lisätty haamut ja powerpellet-kuvat.
- Sprite-luokkiin lisätty Ghost ja Powerpellet. Ghost ja Pacman luokkiin lisätty apufunktioita liikuttamista varten.
- Level-luokkaan lisätty haamujen liikkumisesta vastaavia funktioita 'move_ghost', 'centered', 'find_path' ja 'bfs', eli leveyshakualgoritmi. 
- Pyritty eriyttämään funktioita niin, että yksi funktio tekee vain yhden asian ja selkeytetty samalla Gameloop-luokan toimintaa.
- Mikäli Pacman törmää haamun kanssa, elämistä vähennetään yksi ja peli päättyy. Elämät eivät ole vielä näkyvillä.

## Viikko 6
- Haamut kuolevat ja palaavat aloitusruutuun, kun Pacman syö powerpelletin.
- Haamujen eri persoonallisuudet jätettiin pois yksinkertaisuuden vuoksi. 
- Kun kaikki pelletit on syöty, alkaa kenttä uudelleen alusta, mutta haamut liikkuvat nopeammin.
- Pelin päätyttyä näytetään "Game Over"-näkymä ja kerätty pistesaldo.
- Luotu hakemistot ui- ja gamelogic, johon sijoitettiin gameloop.py ja level.py.
- Testejä lisätty.

### Viikko 7
- Initialize_sprites-metodi refaktoroitu koodikatselmoinnista saadun palautteen perusteella sanakirja-muotoon.
- Leveyshakualgoritmia hajautettu vielä yhteen apumetodiin, jonka myötä saatu pylint-virheilmoitus pois (too-many-nested-blocks).
- Peliin lisätty yksinkertainen tietokanta. Tietokanta kerää highscores.db tiedostoon paikallisen scoreboardin.
- Pelin alussa näytetään kolmen parhaan pelaajan nimet ja pisteet.
- Jos pelaaja saa enemmän pisteitä, kuin kolmanneksi paras pelaaja, annetaan mahdollisuus lisätä oma nimi listalle.
- Haamuille lisätty aloitusruudusta kertova attribuutti.
- Pacmanin liikkumista sujuvoitettu. Nyt Pacman ei pysähdy jos esimerkiksi vasemmalle kuljettaessa painaa ylöspäin, ilman että siihen suuntaan voisi kulkea.
