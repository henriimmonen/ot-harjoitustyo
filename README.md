# Repositorio Ohjelmistotekniikka-kurssia varten
Harjoitustyön aiheena on Pacman pelin versio. Tarkempi määrittely pelin ominaisuuksista löytyy vaatimusmäärittely-dokumentista. Harjoitustyössä on käytetty Pac-Man-hahmo ja muita png-kuvia David Reillyn [Pac-Man](https://github.com/greyblue9/pacman-python) projektista. [A Plus Coding](https://github.com/a-plus-coding/pacman-with-python) tekemästä Pacman-projektista on ideoitu leveyshaku Ghost-spritejen liikkumista varten.

## Releaset
- [Release 1](https://github.com/henriimmonen/ot-harjoitustyo/releases/tag/Viikko5)
- [Release 2](https://github.com/henriimmonen/ot-harjoitustyo/releases/tag/Viikko6)
- [Loppupalautus](https://github.com/henriimmonen/ot-harjoitustyo/releases/tag/Loppupalautus)

## Harjoitustyön dokumentaatio
- [Vaatimusmäärittely](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)
- [Arkkitehtuuri](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/arkkitehtuuri.md)
- [Käyttöohje](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/kayttoohje.md)
- [Testausdokumentti](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/testausdokumentti.md)

## Harjoitustyön komentorivitoiminnot
- Riippuvuuksien asentaminen lataamisen jälkeen:
```poetry install```

- Pelin käynnistys suoritetaan käskyllä:
```poetry run invoke start```

- Testien ajaminen suoritetaan käskyllä:
```poetry run invoke test```

- Testikattavuuden tarkistaminen suoritetaan käskyllä:
```poetry run invoke coverage```

- Testikattavuusraportin muodostaminen (htmlcov-hakemistoon) suoritetaan käskyllä:
```poetry run invoke coverage-report```

- Koodin siistiminen PEP8 mukaiseksi suoritetaan käskyllä:
```poetry run invoke format```

- Pylint-raportin (.pylintrc-tiedoston mukainen) koostaminen suoritetaan käskyllä:
```poetry run invoke lint```
