from pridobivanje_podatkov import *
import time
from spremenljivke import *


def main(downlovdaj=True, pocsvjaj=True):
    #pridobivanje_podatkov____________________________________________________________________________________________________

    #html_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    pot = os.path.join(mapa_slovar, html)
    if downlovdaj or not os.path.exists(pot):
        t1 = vse_strani_to_html(od, do, url,  mapa_slovar, html)
    else:
        print("Datoteka html že obstaja")
        t1 = None
    
    #csv_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
    pot = os.path.join( mapa_slovar, csv)
    if pocsvjaj or not os.path.exists(pot):
        t2 = html_to_csv( mapa_slovar, html, csv)
    else:
        print("datoteka csv že obstaja")
        t2 = None
    
    #ostali podatki_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
    podatki_to_csv( mapa_hitrosti, file_hitrosti, od, do, t1, t2)
    
    #prikaz_in_analiza__________________________________________________________________________________________
    


#klicanje main__________________________________________________________________________________________________
if __name__ == '__main__':
    main(True, True)

