# Testausdokumentti
Pelin testaus on tapahtunut kirjoitusvaiheessa sekä manuaalisesti peliä pelaamalla, että automatisoiduin testein.
Automatisoidut testit on kirjoitettu all_test.py tiedostoon.

## Automatisoidut yksikkö- ja integraatiotestit
Suurin osa testeistä testaa Sprite-olioihin liittyviä koordinaatteja ja toimintoja. Lisäksi testeissä tarkistetaan yksittäisten metodien toimintaa Level-luokassa.
Käyttöliittymästä vastaavaa Gameloop-luokkaa ei testata automatisoidusti.

## Manuaalinen testaus
Gameloop-luokkaa ja siinä tapahtuvia toimintoja (näppäinten painaminen, kierroksen eteneminen silmukan sisällä, tietokannan tapahtumat) on testattu manuaalisesti kehityksen aikana.
