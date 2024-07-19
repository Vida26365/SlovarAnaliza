from pridobivanje_podatkov import *
import time
from spremenljivke import *


def obstaja(mapa, datoteka):
    for file in os.listdir(mapa):
        if "."+datoteka in file:
            return True
    return False


def main(downlovdaj=False, pocsvjaj=False, od=prva_stran, do=zadnja_stran, mapa_slovar=mapa_slovar):
    if do > 4884:
        do = 4884
    if od < 1:
        od = 1
    #pridobivanje_podatkov____________________________________________________________________________________________________

    #html_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_   
    if downlovdaj or not obstaja(mapa_slovar, "html"):
        for i in range(od, do+1):
            pot_html = os.path.join(mapa_slovar, html(i))
            if os.path.exists(pot_html):
                os.remove(pot_html)
        t1 = vse_strani_to_html(od, do, url, mapa_slovar, html)
    else:
        print("Datoteka html že obstaja")
        t1 = None
    
    #csv_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
    if pocsvjaj or not obstaja(mapa_slovar, "csv"):
        t2 = html_to_csv(mapa_slovar, html, csv, od, do)
    else:
        print("datoteka csv že obstaja")
        t2 = None
    
    #ostali podatki_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    podatki_to_csv(mapa_hitrosti, file_hitrosti, od, do, t1, t2)

    print("končano")

#klicanje main__________________________________________________________________________________________________
if __name__ == '__main__':
    main(True, True)

