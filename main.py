from pridobivanje_podatkov import *


def main(downlovdaj=True, pocsvjaj=True):
    #spremenljivke____________________________________________________
    mapa = "podatki"
    html = lambda n: f"html{n}.html" #razdelim html na več datotek, da ne bi preveč v eni datoteki. Nisem sicer preverila, ampak sklepam da bi lahko bilo preveč
    csv = "csv.csv"

    url = lambda n: f"https://www.fran.si/iskanje?page={n}&View=1&Query=*&All=*&FilteredDictionaryIds=133" 

    
    pot = os.path.join(mapa, html(1))
    if downlovdaj or not os.path.exists(pot):
        for i in range(1, 4884):
            url_to_file(url(i), mapa, html(i))
    else:
        print("Datoteka html že obstaja")
    
    pot = os.path.join(mapa, csv)
    if pocsvjaj or not os.path.exists(pot):
        tekst = file_to_string(mapa, html)
        dict_to_csv(regexanje(tekst), mapa, csv)
    else:
        print("datoteka csv že obstaja")
    
    
    
if __name__ == '__main__':
    main(False)

