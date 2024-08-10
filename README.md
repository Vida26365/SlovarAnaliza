# SlovarAnaliza

# Program za analiziranje besed iz Slovarja Slovenskega knjižnjega jezika 2.

POZOR! Program potrebuje zelo dolgo časa da ridobi pridovbljene podatke iz interneta (predvideno 5 ur). Zato sem dodala možnost uporabe že pridobljenih podatkov (v mapi `cel_slovar`). Več o tem v datoteki `analiza.ipynb`.

## Kaj potrebujete za uporabo programa?
Za uporabo programa potrebujete 
1. Dostop do interneta
2. Naslednje python knjižnjice:
    * pandas
    * jupyter
    * requests
    * html5lib
    * bs4


# Kaj vsebuje program?
Program vsebuje naslednje datoteke:
* `main.py` datoteka, ki poskrbi, da se pridobivanje podatkov lahko izvede
* `pridobivanje_podatkov.py` datoteka, v kateri so shranjene posamezne funkcije, ki jih uporabimo v datoteki `main.py`
* `spremenljivke.py` datoteka v kateri so shranjene spremenljivke, da so na enem mestu
* `analiza.ipynb` je jupyter datoteka, kjer se nahaja interktiven program za uporabnika
* mapa `cel_slovar`, kjer se nahaja datoteka `besede.csv` kjer so že zapisani vsi iskani podatkim, da uporabniku ni potrebno čakati, da program pridobi podatke iz interneta