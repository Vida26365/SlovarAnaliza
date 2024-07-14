from pridobivanje_podatkov import *
import time
from spremenljivke import *


def main(downlovdaj=False, pocsvjaj=False, od=prva_stran, do=zadnja_stran):
    if do > 4884:
        do = 4884
    if od < 1:
        od = 1
    #pridobivanje_podatkov____________________________________________________________________________________________________

    #html_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    if downlovdaj or not os.path.exists(pot_slovar_html):
        vse_strani_to_html(od, do, url, mapa_slovar, html)
    else:
        print("Datoteka html že obstaja")
    
    #csv_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
    if pocsvjaj or not os.path.exists(pot_slovar_csv):
        html_to_csv(mapa_slovar, html, csv)
    else:
        print("datoteka csv že obstaja")
    
    #ostali podatki_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    # podatki_to_csv( mapa_hitrosti, file_hitrosti, od, do, t1, t2)

    print("končano")

#klicanje main__________________________________________________________________________________________________
if __name__ == '__main__':
    main()

