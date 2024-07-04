import requests
import re
import os
import csv
import time
import pandas as pd

# print("to ni main, napačen file si pognala")

# to_funkcije___________________________________________________________________________________________________

# html_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
def url_to_file(url,  mapa, file):
    try:
        headers = {"User-agent":"Chrome/124.0.6367.207"}
        vsebina = requests.get(url, headers=headers)
    except requests.exceptions.RequestException:
        print ("spletna stran ni dosegljiva")
        return None
    tekst = vsebina.text
    
    
    os.makedirs(mapa, exist_ok=True)
    pot = os.path.join( mapa, file)
    with open(pot, "a", encoding="utf-8") as file:
        file.write(tekst)
    return

def file_to_string( mapa, file):
    pot = os.path.join( mapa, file)
    with open(pot, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def vse_strani_to_html(od, do, url, mapa, file): #url je funkcija
    zač = time.time()
    for i in range(od, do+1):
        print("stran", i)
        url_to_file(url(i), mapa, file)
    return time.time()-zač

# csv_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
def html_to_csv( mapa, html, csv):
    zač = time.time()
    print("v procesu pridobivanja posatkov iz htmlja v csv")
    tekst = file_to_string( mapa, html)
    dict_to_csv(regexanje(tekst), mapa, csv, "w")
    return time.time()-zač


def dict_to_csv(slovar,  mapa, file, način, naslov=True):
    pot = os.path.join( mapa, file)
    if not os.path.exists(pot):
        naslov = True
    
    
    os.makedirs(mapa, exist_ok=True)
    oznake = list(slovar[0].keys())
    with open(pot, način, encoding="utf-8") as file:
        pisatelj = csv.DictWriter(file, fieldnames=oznake)
        if naslov == True:
            pisatelj.writeheader()
        for stvar in slovar:
            pisatelj.writerow(stvar)
    return


def podatki_to_dict(t1, t2, od, do):
    št = do-od+1
    if t1 == None: html_hitrost = 1
    html_hitrost = št/t1
    csv_hitrost = št/t2
    return [{"čas_html":t1, "čas_csv":t2, "strani": št, "html_hitrost":html_hitrost, "csv_hitrost":csv_hitrost}]

def podatki_to_csv( mapa, file, od, do, t1=None, t2= None):
    # t = time.time()
    # hitrost = get_internet_speed()
    slovar = podatki_to_dict(t1, t2, od, do)
    dict_to_csv(slovar,  mapa, file, "a", naslov=False)
    # print(time.time()-t)


# pridobi_type_funkcije_____________________________________________________________________________________________

def regexanje(tekst):
    #stvari_ki_jih_iščem:
    re_ime = r'<span class="font_xlarge"><a href.*?>(?P<ime>.+?)</a>'
    re_oblika = r'title="Oblika" data-group="header">(?P<oblika>.*?)</span>'
    re_vrsta = r'<span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title=.*?>(?P<vrsta>ž|m|s|medm.|predl.|predpona|člen.|dov.|nedov.|prid.|prisl)</span>'
    re_tonemski_naglas = r'title="Tonemski naglas" data-group="header">(?P<tonemski_naglas>.*?)</span>'
    
    vzorec = ".*?".join((re_ime, re_oblika, re_vrsta, re_tonemski_naglas))
    
    return [m.groupdict() for m in re.finditer(vzorec, tekst, re.DOTALL)]




# analiza_in_prikaz__________________________________________________________________________________________________
