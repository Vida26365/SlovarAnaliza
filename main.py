from pridobivanje_podatkov import *


def main(downlovdaj=True, pocsvjaj=True):
    #spremenljivke____________________________________________________
    mapa_slovar = "slovarski_podatki"
    html = "html.html" #razdelim html na več datotek, da ne bi preveč v eni datoteki. Nisem sicer preverila, ampak sklepam da bi lahko bilo preveč
    csv = "csv.csv"
    
    mapa_hitrosti = "programski_podatki"
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
    
    podatki_to_csv(get_internet_speed(), t1, t2, od, do, mapa_hitrosti, file_hitrosti)
    
    
if __name__ == '__main__':
    main(True)

