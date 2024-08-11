# Program za analiziranje besed iz Slovarja Slovenskega knjižnega jezika 2.

POZOR! Program potrebuje zelo dolgo časa da ridobi pridovbljene podatke iz interneta (približno 5 ur). Zato sem dodala možnost uporabe že pridobljenih podatkov (v mapi `cel_slovar`). Več o tem v datoteki `analiza.ipynb`. Lahko pa tudi prilagodite iz koliko strani slovarja želite pridobiti podatke.

## Kaj potrebujete za uporabo programa?
Za uporabo programa potrebujete 
1. Dostop do interneta
2. Naslednje python knjižnjice:
    * pandas
    * jupyter
    * requests
    * html5lib
    * bs4


## Kaj vsebuje program in zakaj?
Program vsebuje naslednje datoteke:
* `main.py` datoteka, ki poskrbi, da se pridobivanje podatkov izvede
* `pridobivanje_podatkov.py` datoteka, v kateri so shranjene posamezne funkcije, ki jih uporabimo v datoteki `main.py`
* `spremenljivke.py` datoteka v kateri so shranjene spremenljivke
* `analiza.ipynb` je jupyter datoteka, kjer se nahaja interktiven program za uporabnika. Tam poteka tudi večino analize.
* mapa `cel_slovar`, kjer se nahaja datoteka `besede.csv` kjer so že zapisani vsi iskani podatkim, da uporabniku ni potrebno čakati, da program pridobi podatke iz interneta