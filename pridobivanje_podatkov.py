from bs4 import BeautifulSoup
import requests
import re
import os
import csv
import time
import pandas as pd

# print("to ni main, napačen file si pognala")

# to_funkcije___________________________________________________________________________________________________

# html_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
def url_to_file(url,  mapa, file, način = "a"):
    try:
        headers = {"User-agent":"Chrome/124.0.6367.207"}
        vsebina = requests.get(url, headers=headers)
    except requests.exceptions.RequestException:
        print ("spletna stran ni dosegljiva")
        return None
    tekst = vsebina.text
    
    
    os.makedirs(mapa, exist_ok=True)
    pot = os.path.join( mapa, file)
    with open(pot, način, encoding="utf-8") as file:
        file.write(tekst)
    return

def file_to_string( mapa, file):
    pot = os.path.join( mapa, file)
    with open(pot, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def vse_strani_to_html(od, do, url, mapa, file): #url je funkcija
    zač = time.time()
    print("v procesu pridobivanja html-ja")
    for i in range(od, do+1):
        način = "a"
        if i == od:
            način = "w"
        print("stran", i)
        url_to_file(url(i), mapa, file, način )
    return time.time()-zač

# csv_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
def html_to_csv( mapa, html, csv):
    zač = time.time()
    print("v procesu pridobivanja posatkov iz htmlja v csv")
    tekst = file_to_string( mapa, html)
    dict_to_csv(regexanje(tekst), mapa, csv, "w")
    return time.time()-zač


def dict_to_csv(slovar,  mapa, file, način="w", naslov=True):
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
    slovar = podatki_to_dict(t1, t2, od, do)
    dict_to_csv(slovar,  mapa, file, "a", naslov=False)


# pridobi_type_funkcije_____________________________________________________________________________________________
def regexanje(tekst):
    soup = BeautifulSoup(tekst, "html5lib")
    # print(soup.prettify)
    seznam = []
    tabela = soup.find_all("div", attrs={"class":"entry-content"})
    
    for odstavek in tabela:
        slovar = {}
        slovar["ime"] = odstavek.a.text
        
        listek = set()
        for span in odstavek.find_all("span", attrs={"title":"Oblika"}):
            
            for c in odstavek.find("span", attrs={"title":"Oblika"}).text.replace(u"\xa0", u"").split():
                listek.add(c)
        slovar["oblika"] = listek
        
        def pomozna_definicija(tag):
            vrste = ["samostalnik", "pridevnik", "glagol", "veznik", "členek", "prislov", "medmet"]
            if not tag.has_attr("title"):
                return False
            for vrsta in vrste:
                if vrsta in tag["title"]:
                    return True
            return False
            # return tag.has_attr("title") and tag["title"] in ["samostalnik ženskega spola"]
            # return tag["data-toggle"] == "tooltip" and tag["data-placement"] == "top" and tag["title"] not in ["Oblika"]
        if odstavek.find(pomozna_definicija) != None:
            print(odstavek.find(pomozna_definicija)["title"]) 
            slovar["vrsta"] = odstavek.find(pomozna_definicija)["title"]
        else:
            print(odstavek)
            slovar["vrsta"] = odstavek.find(pomozna_definicija)
            if odstavek.find(attrs={"title":"Razlaga"}) != None and "pridevnik" in odstavek.find(attrs={"title":"Razlaga"}).text:
                slovar["vrsta"] = "pridevnik"
                print("zadetek____________________________________________")
            # elif odstavek.find(attrs={"title":"Kazalka"}) != None and odstavek.find(attrs={"title":"Kazalka"}) == "gl. ":
            #     slovar["vrsta"] = "glej "+odstavek.find(attrs={"title":"Oblika"})["title"]
            #     print("dfvjdkrgsrhsrhsrthsrthrthrthrat")
        print()
        
        
        listek = set()
        for span in odstavek.find_all(attrs={"title":"Izgovor"}):
            listek.add(span.text)
        slovar["izgovor"] = listek
        
        
        
        #<span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="samostalnik moškega spola" data-group="qualifier header ">m </span>
        
        #<span data-group="header"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="veznik, vezniška raba" data-group="qualifier header ">vez., </span>


        
        listek = set()
        for span in odstavek.find_all(attrs={"title":"Tonemski naglas"}):
            listek.add(span.text)
        slovar["tonemski naglas"] = listek
        

        seznam.append(slovar)
    
    #print(seznam, len(seznam))

from spremenljivke import *
regexanje(file_to_string(mapa_slovar, html))


# def regexanje(tekst):

#     #stvari_ki_jih_iščem:
#     re_ime = r'<span class="font_xlarge"><a href.*?>(?P<ime>.+?)</a'
#     re_oblika = r'(?>title="Oblika" data-group="header">(?P<oblika>.+?)</span>.*?){0,1}'
#     re_vrsta = r'span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="(?P<vrsta>samostalnik ženskega spola|samostalnik moškega spola|samostalnik srednjega spola|medemet|predlog|predpona|členek|dovršni glagol|nedovršni glagol|dovršni in nedovršni glagol|pridevnik|prislov|zaimek|števnik)"'
#     re_tonemski_naglas = r'(?>title="Tonemski naglas" data-group="header">(?P<tonemski_naglas>.*?)</span>){0,1}<'
        
#     #stvari_ki_jih_iščem:
#     # re_ime = r'<span class="font_xlarge"><a href.*?>(?P<ime>.+?)</a>'
#     # re_oblika = r'title="Oblika" data-group="header">(?P<oblika>.*?)</span>'
#     # re_vrsta = r'(<span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="(?P<vrsta>samostalnik ženskega spola|samostalnik moškega spola|samostalnik srednjega spola|medemet|predlog|predpona|členek|dovršni glagol|nedovršni glagol|dovršni in nedovršni glagol|pridevnik|prislov|zaimek)"'
#     # re_tonemski_naglas = r'title="Tonemski naglas" data-group="header">(?P<tonemski_naglas>.*?)</span>'
    
#     vzorec = ".*?".join((re_ime, re_oblika, re_vrsta, re_tonemski_naglas))
    
#     print(re.findall(vzorec, tekst, re.DOTALL))
    
#     return [m.groupdict() for m in re.finditer(vzorec, tekst, re.DOTALL)]




# analiza_in_prikaz__________________________________________________________________________________________________
