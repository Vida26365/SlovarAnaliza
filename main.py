from pridobivanje_podatkov import *


def main(downlovdaj=True, ):
    #spremenljivke____________________________________________________
    mapa = "podatki"
    html = "html.html"
    csv = "csv.scv"
    
    pot = os.path.join(mapa, html)
    if downlovdaj or not os.path.exists(pot):
        url_to_file(url, mapa, html)
    else:
        print("Datoteka html že obstaja")
    
    
    
    
    
    url = "https://www.fran.si/iskanje?View=1&Query=*&All=*&FilteredDictionaryIds=133"

    url_to_file(url, "datoteke", "html.html")
    test2 = file_to_string("datoteke", "html.html")
    dict_to_csv(regexanje(test2),"datoteke", "csv.csv")














if __name__ == '__main__':
    main(False)