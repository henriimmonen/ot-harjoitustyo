# Repositorio Ohjelmistotekniikka-kurssia varten
Harjoitustyön aiheena on Pacman pelin versio. Tarkempi määrittely pelin ominaisuuksista löytyy vaatimusmäärittely-dokumentista. Harjoitustyössä on alustavasti käytetty ohjelmoinnin jatkokurssilla käytettyjä png-kuvia (lattia, seinä). Lisäksi Pac-Man-hahmo ja muita png-kuvia on lainattu David Reillyn [Pac-Man](https://github.com/greyblue9/pacman-python) projektista.

## Harjoitustyön dokumentaatio
- [Vaatimusmäärittely](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)
- [Tuntikirjanpito](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)
- [Changelog](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Harjoitustyön komentorivitoiminnot
- Pelin käynnistys suoritetaan käskyllä:
```bash
poetry run invoke start
```

- Testien ajaminen suoritetaan käskyllä:
```bash
poetry run invoke test
```

- Testikattavuusraportin koostaminen suoritetaan käskyllä:
```bash
poetry run invoke coverage
```

- Koodin siistiminen PEP8 mukaiseksi suoritetaan käskyllä:
```bash
poetry run invoke format
```

- Pylint-raportin koostaminen suoritetaan käskyllä:
```bash
poetry run invoke lint
```
