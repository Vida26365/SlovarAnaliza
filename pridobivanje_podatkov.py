import requests
import re
import os
import csv
import pandas as pd
from spremenljivke import delitelj
from bs4 import BeautifulSoup


# to_funkcije___________________________________________________________________________________________________

# html_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

def vse_strani_to_html(od, do, url, mapa, file): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-
    print("v procesu pridobivanja html-ja...")
    
    žalostni_list = []

    for i in range(od, do+1):
        način = "a"
        print("stran", i)
        žalostni_list += url_to_file(url(i), mapa, file(i//delitelj), "a")
        
    
    i = 0
    while žalostni_list != []: #poskrbi da so vse strani shranjene v datoteki
        url_to_file(žalostni_list[0], mapa, file(do//delitelj), "a")
        žalostni_list = žalostni_list[1::]
        if i > 1000:
            print("na žalost nismo mogli pridobiti sledečih linkov:")
            for link in žalostni_list:
                print(link)
        i += 1
        
    return


def url_to_file(url,  mapa, file, način = "a"): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/
    try:
        headers = {"User-agent":"Chrome/124.0.6367.207"}
        vsebina = requests.get(url, headers=headers)
    except requests.exceptions.RequestException:
        print (f"spletna {url} stran ni dosegljiva")
        return [url]
    
    tekst = vsebina.text
    
    pot = os.path.join(mapa, file)
    
    try:
        with open(pot, način, encoding="utf-8") as file:
            file.write(tekst)
    except PermissionError:
        return [url]
    
    return []




# csv_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def html_to_csv(mapa, html, csv, od, do): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/
    print("v procesu pridobivanja posatkov iz htmlja v csv...")
    print("regexanje...")
    
    tekst = ""
    for file in os.listdir(mapa):
        if file.endswith(".html"):
            print(file)
            tekst += file_to_string(mapa, file)
    dict_to_csv(regexanje(tekst), mapa, csv)
        
    return


def file_to_string(mapa, file): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_
    pot = os.path.join(mapa, file)
    
    with open(pot, "r", encoding="utf-8") as file:
        text = file.read()
    return text


def dict_to_csv(slovar,  mapa, file): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_
    pot = os.path.join(mapa, file)
    
    oznake = list(slovar[0].keys())
    
    with open(pot, "w", encoding="utf-8") as file:
        pisatelj = csv.DictWriter(file, fieldnames=oznake)
        pisatelj.writeheader()
        for stvar in slovar:
            pisatelj.writerow(stvar)
    return


# pridobi_type_funkcije_________________________________________________________________________________________
def regexanje(tekst):
    re_ime = r'<a href.*?>(?P<ime>.+?)</a'
    re_vrsta = r'title="(?P<vrsta>samostalnik ženskega spola|samostalnik moškega spola|samostalnik srednjega spola|medmet|predlog|predpona|členek|dovršni glagol|nedovršni glagol|dovršni in nedovršni glagol|nedovršni in dovršni glagol|pridevnik|prislov|zaimek|števnik|veznik)'

#span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" 
    soup = BeautifulSoup(tekst, 'html5lib')
    
    seznam = []
    for celica in soup.findAll('div', attrs={"class":"entry-content"}):
        slovar = {}
        slovar["ime"] = re.findall(re_ime, str(celica), re.DOTALL)[0]
        vrsta = re.findall(re_vrsta, str(celica), re.DOTALL)
        if vrsta == []:
            slovar["vrsta"] = "neznano"
        else:
            slovar["vrsta"] = vrsta[0]
        seznam.append(slovar)
    return seznam