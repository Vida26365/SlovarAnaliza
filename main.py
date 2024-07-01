from pridobivanje_podatkov import *
import time


def main(downlovdaj=True, pocsvjaj=True):
    #spremenljivke____________________________________________________
    mapa_slovar = "slovarski_podatki"
    html = "html.html"
    csv = "csv.csv"
    
    mapa_hitrosti = "programski_podatki" #posebna mapa, ker se ta ne briše
    file_hitrosti = "podatki.csv"

    url = lambda n: f"https://www.fran.si/iskanje?page={n}&View=1&Query=*&All=*&FilteredDictionaryIds=133" 
    
    od = 1
    do = 3 #vključno z    (do 4884)
    
    
    

    
    pot = os.path.join(mapa_slovar, html)
    if downlovdaj or not os.path.exists(pot):
        t1 = vse_strani_to_html(od, do, url, mapa_slovar, html)
    else:
        print("Datoteka html že obstaja")
    
    pot = os.path.join(mapa_slovar, csv)
    if pocsvjaj or not os.path.exists(pot):
        t2 = html_to_csv(mapa_slovar, html, csv)
    else:
        print("datoteka csv že obstaja")
    
    podatki_to_csv(mapa_hitrosti, file_hitrosti, od, do, t1=None, t2=None)
    
    
if __name__ == '__main__':
    main()

