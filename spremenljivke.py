import pandas as pd
import os
#spremenljive_spremenljivke_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
prva_stran = 1
zadnja_stran = 5 #vključno z    (do 4884)

#nespremenljive_spremenljivke_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
mapa_slovar = "slovar"
html = lambda n: f"html{n//100}.html"
# html = "html.html"
csv = "besede.csv"
parquet = "parquet.parquet"
mapa_stalni_slovar = "stalni_slovar"


mapa_hitrosti = "program" #posebna mapa, ker se ta ne briše ###################################3333
file_hitrosti = "podatki.csv"##########################################

url = lambda n: f"https://www.fran.si/iskanje?page={n}&View=1&Query=*&All=*&FilteredDictionaryIds=133" 

#obdelane_spremenljivke_________________________________________________________________________________________
pot_slovar_csv = os.path.join(mapa_slovar, csv)
pot_slovar_parquet = os.path.join(mapa_slovar, parquet)
# pot_slovar_html = os.path.join(mapa_slovar, html)


#dodatno________________________________________________________________________________________________________
abeceda = "abcčdefghijklmnoprsštuvzž"
besedne_vrste = ["samostalnik", "zaimek", "števnik", "pridevnik", "prislov", "glagol", "členek", "veznik", "medmet"]
