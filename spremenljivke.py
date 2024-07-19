import pandas as pd
import os
#spremenljive_spremenljivke_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
prva_stran = 1
zadnja_stran = 4884 #vključno z    (do 4884)

delitelj = 100


#nespremenljive_spremenljivke_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

mapa_slovar = "slovar"
html = lambda n: f"html{n}.html"
csv = "besede.csv"
parquet = "parquet.parquet"
mapa_stalni_slovar = "stalni_slovar"


mapa_hitrosti = "program" #posebna mapa, ker se ta ne briše ###################################3333
file_hitrosti = "podatki.csv"##########################################

url = lambda n: f"https://www.fran.si/iskanje?page={n}&View=1&Query=*&All=*&FilteredDictionaryIds=133" 



#dodatno________________________________________________________________________________________________________
abeceda = "abcčdefghijklmnoprsštuvzž"
besedne_vrste = ["samostalnik", "zaimek", "števnik", "pridevnik", "prislov", "glagol", "členek", "veznik", "medmet"]
