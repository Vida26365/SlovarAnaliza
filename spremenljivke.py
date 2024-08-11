import pandas as pd
#spremenljive_spremenljivke_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
prva_stran = 1
zadnja_stran = 4884 #vključno z    (do 4884)

delitelj = 100


#nespremenljive_spremenljivke_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

mapa_slovar = "slovar"
html = lambda n: f"html{n}.html"
csv = "besede.csv"

cel_slovar = "cel_slovar"

url = lambda n: f"https://www.fran.si/iskanje?page={n}&View=1&Query=*&All=*&FilteredDictionaryIds=133" 



#dodatno________________________________________________________________________________________________________
abeceda = "abcčdefghijklmnoprsštuvzž"
besedne_vrste = ["samostalnik", "zaimek", "števnik", "pridevnik", "prislov", "glagol", "členek", "veznik", "medmet", "neznano"]
