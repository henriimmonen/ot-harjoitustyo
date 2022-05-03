# Käyttöohje

Lataa pelin viimeisin [Release](https://github.com/henriimmonen/ot-harjoitustyo/releases/tag/Viikko6).

Ennen ohjelman käynnistämistä, asenna riippuvuudet komennolla `poetry install`.

Tämän jälkeen ohjelman käynnistää juurihakemistosta komennolla `poetry run invoke start`.

Peli käynnistyy aloitusruutuun, josta pääset pelaamaan painamalla välilyöntiä. Ohjelman voi sulkea missä tahansa vaiheessa Esc-näppäimellä tai painamalla yläkulman raksia. 

Peliä ohjataan nuolinäppäimillä. Tavoitteena on syödä kaikki pelikentän nappulat ennen kuin elämät loppuvat.

Jokaisen kerran kun saat tyhjennettyä koko kentän, haamujen nopeus kasvaa ja kenttä alkaa alusta.

Peli jatkuu kunnes kaikki elämät on käytetty.
