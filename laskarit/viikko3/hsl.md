```mermaid
sequenceDiagram
	main ->> laitehallinto
	main ->> rautatietori
	main ->> ratikka6
	main ->> bussi244
	main ->> laitehallinto: lisaa_lataaja(rautatietori)
	main ->> laitehallinto: lisaa_lukija(ratikka6)
	main ->> laitehallinto: lisaa_lukija(bussi244)
	main ->> lippu_luukku
	main ->> lippu_luukku: osta_matkakortti("Kalle")
	lippu_luukku -->> main: kallen_kortti
	main ->> rautatietori: lataa_arvoa(kallen_kortti,3)	
	rautatietori ->> kallen_kortti: kasvata_arvoa(3)
	main ->> ratikka6: osta_lippu(kallen_kortti,0)
	ratikka6 -->> main: True 
	main ->> bussi244: osta_lippu(kallen_kortti,2)
	bussi244 -->> main: False
```
