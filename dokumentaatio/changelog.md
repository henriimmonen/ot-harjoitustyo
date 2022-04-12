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
