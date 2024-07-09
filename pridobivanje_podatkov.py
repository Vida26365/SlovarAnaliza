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
    #<span class="font_xlarge"><a href="/133/sskj2-slovar-slovenskega-knjiznega-jezika-2/4457252/a?View=1&amp;Query=*&amp;All=*&amp;FilteredDictionaryIds=133">a</a></span><span class="color_lightdark font_xsmal sup">5</span> <span data-group="header">
    # <span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="veznik" data-group="header qualifier">vez.</span></span>, <span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="knjižno" data-group="qualifier header ">knjiž. </span></span><br /><span class="color_lightdark strong">1. </span><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="Kvalifikator, pojasnilo" data-group="qualifier header ">v protivnem priredju </span><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Razlaga" data-group="explanation ">za izražanje</span><br /><span class="color_lightdark strong">a) </span><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Razlaga" data-group="explanation ">nasprotja s prej povedanim; </span><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Sopomenka" data-group="explanation"><a class="reference" href="/133/sskj2-slovar-slovenskega-knjiznega-jezika-2/4508133/pa?View=1&amp;Query=*&amp;All=*&amp;FilteredDictionaryIds=133" target="_blank">pa</a></span><span class="sup italic" data-group="other">2</span>, <span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Sopomenka" data-group="explanation"><a class="reference" href="/133/sskj2-slovar-slovenskega-knjiznega-jezika-2/4540453/toda?View=1&amp;Query=*&amp;All=*&amp;FilteredDictionaryIds=133" target="_blank">toda</a>, </span><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Sopomenka" data-group="explanation"><a class="reference" href="/133/sskj2-slovar-slovenskega-knjiznega-jezika-2/4545439/vendar?View=1&amp;Query=*&amp;All=*&amp;FilteredDictionaryIds=133" target="_blank">vendar</a>:</span> <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">prej so ga radi imeli, a zdaj zabavljajo čezenj</span></span>; <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">to so besede, a ne dejanja</span></span>; <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">drugod umetnike slavijo. A pri nas? sicer je miren, a kadar se napije, zdivja</span></span><span class="color_lightdark" data-group="other"> / <span data-group=""><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="Kvalifikator, pojasnilo" data-group="qualifier header ">včasih okrepljen </span><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">bilo ji je malo nerodno, a vendar tako lepo pri srcu </span></span></span><br /><span class="color_lightdark strong">b) </span><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Razlaga" data-group="explanation ">nepričakovane posledice:</span> <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">tipal je po temni veži, a vrat ni našel</span></span>; <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">postarala se je, a ni ovenela </span></span><br /><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Podpomen" data-group="other">// </span><span class="color_lightdark"><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Razlaga" data-group="explanation ">za omejevanje:</span> <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">to more ugotoviti samo zdravnik, a še ta težko</span></span>; <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">bral je, a samo kriminalke </span></span></span><br /><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Podpomen" data-group="other">// </span><span class="color_lightdark"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="Kvalifikator, pojasnilo" data-group="qualifier header ">na začetku novega (od)stavka </span><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Razlaga" data-group="explanation ">za opozoritev na prehod k drugi misli:</span> <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">A vrnimo se k stvari! A dopustimo možnost, da se motimo </span></span></span><br /><span class="color_lightdark strong">2. </span><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="Kvalifikator, pojasnilo" data-group="qualifier header ">v vezalnem priredju </span><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Razlaga" data-group="explanation ">za navezovanje na prej povedano; </span><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Sopomenka" data-group="explanation"><a class="reference" href="/133/sskj2-slovar-slovenskega-knjiznega-jezika-2/4479778/in?View=1&amp;Query=*&amp;All=*&amp;FilteredDictionaryIds=133" target="_blank">in</a>, </span><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Sopomenka" data-group="explanation"><a class="reference" href="/133/sskj2-slovar-slovenskega-knjiznega-jezika-2/4508133/pa?View=1&amp;Query=*&amp;All=*&amp;FilteredDictionaryIds=133" target="_blank">pa</a></span><span class="sup italic" data-group="other">2</span>: <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">sin je šel z doma, a hči se je omožila v sosednjo vas</span></span><span class="color_lightdark" data-group="other"> / <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">nevesta se sramežljivo smehlja, a rdečica ji zaliva lice </span></span></span>

    
    #<span class="font_xlarge"><a href="/133/sskj2-slovar-slovenskega-knjiznega-jezika-2/4457250/a?View=1&amp;Query=*&amp;All=*&amp;FilteredDictionaryIds=133">à</a></span><span class="color_lightdark font_xsmal sup">3</span> <span data-group="header">
    # <span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="členek" data-group="header qualifier">člen.</span>

    #stvari_ki_jih_iščem:
    re_ime = r'<span class="font_xlarge"><a href.*?>(?P<ime>.+?)</a'
    re_oblika = r'(?>title="Oblika" data-group="header">(?P<oblika>.+?)</span>.*?){0,1}'
    re_vrsta = r'span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="(?P<vrsta>samostalnik ženskega spola|samostalnik moškega spola|samostalnik srednjega spola|medemet|predlog|predpona|členek|dovršni glagol|nedovršni glagol|dovršni in nedovršni glagol|pridevnik|prislov|zaimek|števnik)"'
    re_tonemski_naglas = r'(?>title="Tonemski naglas" data-group="header">(?P<tonemski_naglas>.*?)</span>){0,1}<'
        
    #stvari_ki_jih_iščem:
    # re_ime = r'<span class="font_xlarge"><a href.*?>(?P<ime>.+?)</a>'
    # re_oblika = r'title="Oblika" data-group="header">(?P<oblika>.*?)</span>'
    # re_vrsta = r'(<span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title="(?P<vrsta>samostalnik ženskega spola|samostalnik moškega spola|samostalnik srednjega spola|medemet|predlog|predpona|členek|dovršni glagol|nedovršni glagol|dovršni in nedovršni glagol|pridevnik|prislov|zaimek)"'
    # re_tonemski_naglas = r'title="Tonemski naglas" data-group="header">(?P<tonemski_naglas>.*?)</span>'
    
    vzorec = ".*?".join((re_ime, re_oblika, re_vrsta, re_tonemski_naglas))
    
    print(re.findall(vzorec, tekst, re.DOTALL))
    
    return [m.groupdict() for m in re.finditer(vzorec, tekst, re.DOTALL)]




# analiza_in_prikaz__________________________________________________________________________________________________
