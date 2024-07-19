from bs4 import BeautifulSoup
import requests
import re
import os
import csv
import time ##############################################
import pandas as pd


# to_funkcije___________________________________________________________________________________________________

# html_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
def url_to_file(url,  mapa, file, način = "a"):
    try:
        headers = {"User-agent":"Chrome/124.0.6367.207"}
        vsebina = requests.get(url, headers=headers)
    except requests.exceptions.RequestException:
        print (f"spletna {url} stran ni dosegljiva")
        return None
    tekst = vsebina.text
    
    os.makedirs(mapa, exist_ok=True)
    pot = os.path.join(mapa, file)
    try:
        with open(pot, način, encoding="utf-8") as file:
            file.write(tekst)
    except PermissionError:
        print("wop wop")
        return [url]
    return []

def file_to_string(mapa, file):
    pot = os.path.join(mapa, file)
    with open(pot, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def vse_strani_to_html(od, do, url, mapa, file): #url je funkcija
    zač = time.time()#########################################################33
    print("v procesu pridobivanja html-ja...")
    
    žalostni_list = []
    print("stran", od)
    žalostni_list += url_to_file(url(od), mapa, file(od), "w") #prva stran je posebna, ker mora prva stran začeti pisati datoteko od začetka, namesto dodajati, kot to delajo naslednje strani
    for i in range(od+1, do+1):
        način = "a"
        print("stran", i)
        žalostni_list += url_to_file(url(i), mapa, file(i), "a")
    print(žalostni_list)
    while žalostni_list != []: #poskrbi da so vse strani shranjene v datoteki
        url_to_file(žalostni_list[0], mapa, file(do), "w")
    return time.time()-zač################################################33

# csv_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
def html_to_csv(mapa, html, csv, od, do):
    zač = time.time()####################################
    print("v procesu pridobivanja posatkov iz htmlja v csv...")
    print("regexanje...")
    tekst = ""
    for i in range(od, do+1):
        tekst = file_to_string(mapa, html(i))
        dict_to_csv(regexanje(tekst), mapa, csv, "w")
    return time.time()-zač ######################################3333

def html_to_parquet(mapa, html, file):
    zač = time.time()####################################
    print("v procesu pridobivanja posatkov iz htmlja v parquet...")
    tekst = file_to_string(mapa, html)
    df = pd.DataFrame.from_dict(regexanje(tekst))
    os.makedirs(mapa, exist_ok=True)
    pot = os.path.join(mapa, file)
    df.to_parquet(pot)
    return time.time()-zač ######################################3333



def dict_to_csv(slovar,  mapa, file, način="w", naslov=True): ##################################################
    #print("shranjevanje v csv...")
    pot = os.path.join( mapa, file)
    if not os.path.exists(pot): #to bom leahko asneje spremenila#################################################
        naslov = True
    
    os.makedirs(mapa, exist_ok=True)
    oznake = list(slovar[0].keys())
    with open(pot, način, encoding="utf-8") as file:
        pisatelj = csv.DictWriter(file, fieldnames=oznake)
        if naslov == True: #############################################################
            pisatelj.writeheader()
        for stvar in slovar:
            pisatelj.writerow(stvar)
    return


def podatki_to_dict(t1, t2, od, do): ##############################################################3
    št = do-od+1
    if t1 == None: 
        html_hitrost = None
    else:
        html_hitrost = št/t1
    if t2 == None:
        csv_hitrost = None
    else:
        csv_hitrost = št/t2
    return [{"čas_html":t1, "čas_csv":t2, "strani": št, "html_hitrost":html_hitrost, "csv_hitrost":csv_hitrost}]

def podatki_to_csv(mapa, file, od, do, t1=None, t2= None): ###################################################################
    slovar = podatki_to_dict(t1, t2, od, do)
    dict_to_csv(slovar,  mapa, file, "a", naslov=False)




# pridobi_type_funkcije_____________________________________________________________________________________________
def regexanje(tekst):
    
    #stvari_ki_jih_iščem:
    re_ime = r'<span class="font_xlarge"><a href.*?>(?P<ime>.+?)</a'
    re_vrsta = r'span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="(?P<vrsta>samostalnik ženskega spola|samostalnik moškega spola|samostalnik srednjega spola|medemet|predlog|predpona|členek|dovršni glagol|nedovršni glagol|dovršni in nedovršni glagol|pridevnik|prislov|zaimek|števnik|veznik)'

    vzorec = ".*?".join((re_ime, re_vrsta))
    #print("urejanje zadetkov...")
    return [m.groupdict() for m in re.finditer(vzorec, tekst, re.DOTALL)]