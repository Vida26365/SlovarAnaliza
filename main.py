from pridobivanje_podatkov import *


def main(downlovdaj=True, pocsvjaj=True):
    #spremenljivke____________________________________________________
    mapa = "podatki"
    html = "html.html"
    csv = "csv.csv"
    url = "https://www.fran.si/iskanje?View=1&Query=*&All=*&FilteredDictionaryIds=133"

    
    pot = os.path.join(mapa, html)
    if downlovdaj or not os.path.exists(pot):
        url_to_file(url, mapa, html)
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

