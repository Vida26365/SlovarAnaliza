from pridobivanje_podatkov import *
import time
from spremenljivke import *


def obstaja(mapa, datoteka):
    os.makedirs(mapa, exist_ok=True)
    for file in os.listdir(mapa):
        if datoteka in file:
            return True
    return False


def main(downlovdaj=False, pocsvjaj=False, od=prva_stran, do=zadnja_stran, mapa_slovar=mapa_slovar):
    if do > 4884:
        do = 4884
    if od < 1:
        od = 1
    #pridobivanje_podatkov____________________________________________________________________________________________________

    #html_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_   
    if downlovdaj or not obstaja(mapa_slovar, ".html"):
        for i in range(0, 49):
            pot_html = os.path.join(mapa_slovar, html(i//delitelj))
            if os.path.exists(pot_html):
                os.remove(pot_html)
        t1 = vse_strani_to_html(od, do, url, mapa_slovar, html)
    else:
        print("Datoteka html že obstaja")
        t1 = None
    
    #csv_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
    if pocsvjaj or not obstaja(mapa_slovar, "besede.csv"):
        pot_csv = os.path.join(mapa_slovar, csv)
        if os.path.exists(pot_csv):
            os.remove(pot_csv)
        t2 = html_to_csv(mapa_slovar, html, csv, od, do)
    else:
        print("Datoteka csv že obstaja")
        t2 = None
    
    #ostali podatki_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    # podatki_to_csv(mapa_hitrosti, file_hitrosti, od, do, t1, t2)

    print("Končano")

#klicanje main__________________________________________________________________________________________________
if __name__ == '__main__':
    main(True, True, od=1, do=10)

