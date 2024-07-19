import requests
import re
import os
import csv
import time ##############################################
import pandas as pd


# to_funkcije___________________________________________________________________________________________________

# html_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-

def vse_strani_to_html(od, do, url, mapa, file): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-
    zač = time.time()#########################################################33
    print("v procesu pridobivanja html-ja...")
    
    žalostni_list = []
    # print("stran", od)
    # žalostni_list += url_to_file(url(od), mapa, file(od), "w") 
    for i in range(od, do+1):
        način = "a"
        print("stran", i)
        žalostni_list += url_to_file(url(i), mapa, file(i), "a")
        
    print(žalostni_list)
    
    i = 0
    while žalostni_list != []: #poskrbi da so vse strani shranjene v datoteki
        url_to_file(žalostni_list[0], mapa, file(do), "w")
        žalostni_list = žalostni_list[1::]
        if i > 1000:
            print("na žalost nismo mogli pridobiti sledečih linkov:")
            for link in žalostni_list:
                print(link)
        i += 1
        
    return time.time()-zač################################################33


def url_to_file(url,  mapa, file, način = "a"): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/
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




# csv_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

def html_to_csv(mapa, html, csv, od, do): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/
    zač = time.time()####################################
    print("v procesu pridobivanja posatkov iz htmlja v csv...")
    print("regexanje...")
    
    for i in range(od, do+1, delitelj):
        print(f"{(i-do)//delitelj}/{(do+1-do)//delitelj}")
        tekst = file_to_string(mapa, html(i))
        dict_to_csv(regexanje(tekst), mapa, csv)
        
    return time.time()-zač ######################################3333


def file_to_string(mapa, file): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_
    pot = os.path.join(mapa, file)
    
    with open(pot, "r", encoding="utf-8") as file:
        text = file.read()
    return text

##################################
def dict_to_csv(slovar,  mapa, file): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_
    pot = os.path.join( mapa, file)
    os.makedirs(mapa, exist_ok=True)
    
    oznake = list(slovar[0].keys())
    
    with open(pot, "a", encoding="utf-8") as file:
        pisatelj = csv.DictWriter(file, fieldnames=oznake)
        pisatelj.writeheader()
        for stvar in slovar:
            pisatelj.writerow(stvar)
    return

##################################################
def podatki_to_dict(t1, t2, od, do): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-
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

def podatki_to_csv(mapa, file, od, do, t1=None, t2= None): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_
    slovar = podatki_to_dict(t1, t2, od, do)
    dict_to_csv(slovar,  mapa, file, "a", naslov=False)




# pridobi_type_funkcije_________________________________________________________________________________________

def regexanje(tekst): #_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-/_-
    
    #stvari_ki_jih_iščem:
    re_ime = r'<span class="font_xlarge"><a href.*?>(?P<ime>.+?)</a'
    re_vrsta = r'span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="(?P<vrsta>samostalnik ženskega spola|samostalnik moškega spola|samostalnik srednjega spola|medemet|predlog|predpona|členek|dovršni glagol|nedovršni glagol|dovršni in nedovršni glagol|pridevnik|prislov|zaimek|števnik|veznik)'

    vzorec = ".*?".join((re_ime, re_vrsta))
    return [m.groupdict() for m in re.finditer(vzorec, tekst, re.DOTALL)]