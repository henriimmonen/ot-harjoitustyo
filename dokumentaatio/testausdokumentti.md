# Testausdokumentti
Pelin testaus on tapahtunut kirjoitusvaiheessa sekä manuaalisesti peliä pelaamalla, että automatisoiduin testein.Automatisoidut testit on kirjoitettu all_test.py tiedostoon.

## Automatisoidut yksikkö- ja integraatiotestit
Suurin osa testeistä testaa Sprite-olioihin liittyviä koordinaatteja ja toimintoja. Lisäksi testeissä tarkistetaan yksittäisten metodien toimintaa Level-luokassa.Käyttöliittymästä vastaavaa Gameloop-luokkaa ei testata automatisoidusti.
Testien haaraumakattavuus on 88%.
![Testien haaraumakattavuus](https://github.com/henriimmonen/ot-harjoitustyo/blob/master/dokumentaatio/kuvat/haaraumakattavuus.png)

Testien ulkopuolelle jäi joitakin metodeja Level-luokasta, joita on haastavampi testata sekä Ghost-luokan kuvan valitsemisesta vastaava metodi. Näitä Level-luokan metodeja ovat mm. aikaan liittyvät metodit ja leveyshaun apumetodit, joita Ghost-spritet käyttävät.

## Manuaalinen testaus
Gameloop-luokkaa ja siinä tapahtuvia toimintoja (näppäinten painaminen, kierroksen eteneminen silmukan sisällä, tietokannan tapahtumat) on testattu manuaalisesti kehityksen aikana. Pelin kesto on lyhyehkö, joten tämä oli helposti toteutettava lähestymistapa. Laajemmassa projektissa tämä voisi käydä työlääksi.
