from bs4 import BeautifulSoup
import requests
# import re  #'#'#'##'#'#'#'#'#'#'#'#'#'##'#'#'#'#'#'#'#''##'#'#
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
    pot = os.path.join( mapa, file)
    with open(pot, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def vse_strani_to_html(od, do, url, mapa, file): #url je funkcija
    zač = time.time()#########################################################33
    print("v procesu pridobivanja html-ja...")
    
    žalostni_list = []
    print("stran", od)
    žalostni_list += url_to_file(url(od), mapa, file, "w") #prva stran je posebna, ker mora prva stran začeti pisati datoteko od začetka, namesto dodajati, kot to delajo naslednje strani
    for i in range(od+1, do+1):
        način = "a"
        print("stran", i)
        žalostni_list += url_to_file(url(i), mapa, file, "a")
    print(žalostni_list)
    while žalostni_list != []: #poskrbi da so vse strani shranjene v datoteki
        url_to_file(žalostni_list[0], mapa, file, "w")
    return time.time()-zač################################################33

# csv_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
def html_to_csv(mapa, html, csv):
    zač = time.time()####################################
    print("v procesu pridobivanja posatkov iz htmlja v csv...")
    tekst = file_to_string(mapa, html)
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
    if t1 == None: html_hitrost = 1
    html_hitrost = št/t1
    csv_hitrost = št/t2
    return [{"čas_html":t1, "čas_csv":t2, "strani": št, "html_hitrost":html_hitrost, "csv_hitrost":csv_hitrost}]

def podatki_to_csv( mapa, file, od, do, t1=None, t2= None): ###################################################################
    slovar = podatki_to_dict(t1, t2, od, do)
    dict_to_csv(slovar,  mapa, file, "a", naslov=False)




# pridobi_type_funkcije_____________________________________________________________________________________________
def regexanje(tekst):
    print("Regexanje...")
    soup = BeautifulSoup(tekst, "html5lib") #poglej si kaj naredi "html5lib"
    seznam = []
    tabela = soup.find_all("div", attrs={"class":"entry-content"}) #najde posamezeo besedo njej pripradajoče stvari 
    
    for odstavek in tabela:
        slovar = {}
        #pridobivanje_stvari____________________________________________________________________________________
        slovar["ime"] = odstavek.a.text
        
        #oblika_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_
        listek = set()
        for span in odstavek.find_all("span", attrs={"title":"Oblika"}):
            
            for c in odstavek.find("span", attrs={"title":"Oblika"}).text.replace(u"\xa0", u"").split():
                listek.add(c)
        slovar["oblika"] = listek
        
        #besedne_vrste_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
        def pomozna_definicija(tag):
            vrste = ["samostalnik", "pridevnik", "glagol", "veznik", "členek", "prislov", "medmet"] #######################################
            if not tag.has_attr("title"):
                return False
            for vrsta in vrste:
                if vrsta in tag["title"]:
                    return True
            return False
        
        if odstavek.find(pomozna_definicija) != None:
            slovar["vrsta"] = odstavek.find(pomozna_definicija)["title"]
        else:
            if odstavek.find(attrs={"title":"Razlaga"}) != None and "pridevnik od" in odstavek.find(attrs={"title":"Razlaga"}).text:
                slovar["vrsta"] = "pridevnik"
            else:
                slovar["vrsta"] = None
        
        #izgovor_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
        listek = set()
        for span in odstavek.find_all(attrs={"title":"Izgovor"}):
            listek.add(span.text)
        slovar["izgovor"] = listek
        
        #tonemski_naglas_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-
        listek = set()
        for span in odstavek.find_all(attrs={"title":"Tonemski naglas"}):
            listek.add(span.text)
        slovar["tonemski naglas"] = listek
        
        seznam.append(slovar)
        
    return seznam



