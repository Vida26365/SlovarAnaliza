import pandas as pd
import os
#spremenljive_spremenljivke_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
prva_stran = 1
zadnja_stran = 10 #vključno z    (do 4884)

#nespremenljive_spremenljivke_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
mapa_slovar = "slovar"
html = "html.html"
csv = "besede.csv"

mapa_hitrosti = "program" #posebna mapa, ker se ta ne briše
file_hitrosti = "podatki.csv"

url = lambda n: f"https://www.fran.si/iskanje?page={n}&View=1&Query=*&All=*&FilteredDictionaryIds=133" 

#spremenljivke za analizo_________________________________________
pd.set_option("display.max_rows", 10)
# %matplotlib inline
pot_slovar = os.path.join(mapa_slovar, csv)
razpredelnica = pd.read_csv(pot_slovar)