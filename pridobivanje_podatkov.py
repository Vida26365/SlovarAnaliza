import requests
import re
import os
import csv
import time
import speedtest


print("to ni main, napačen file si pognala")

def url_to_file(url, mapa, file):
    try:
        headers = {"User-agent":"Chrome/124.0.6367.207"}
        vsebina = requests.get(url, headers=headers)
    except requests.exceptions.RequestException:
        print ("spletna stran ni dosegljiva")
        return None
    tekst = vsebina.text
    
    os.makedirs(mapa, exist_ok=True)
    pot = os.path.join(mapa, file)
    with open(pot, "a", encoding="utf-8") as file:
        file.write(tekst)
    return

def file_to_string(mapa, file):
    pot = os.path.join(mapa, file)
    with open(pot, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def dict_to_csv(slovar, mapa, file, način, naslov=True):
    pot = os.path.join(mapa, file)
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



def regexanje(tekst): #se bom potem ukvarjala s tem. to je kr neki_________________________________________________________________________--_
    vzorec = r'<span class="font_xlarge"><a href.*?>(?P<ime>.+?)</a></span>.*?(?P<vrsta>ž|m|s|medm.|predl.|predpona|člen.|dov.|nedov.|prid.|prisl)</span>.*?' 
    
    #vzorec = r'<span class="font_xlarge"><a href.*?>(?P<ime>.+?)</a></span>.*?(title="Oblika" data-group="header">(?P<oblika>.*?)</span>){0,1}<span.*?(title="Izgovor" data-group="header">(?P<izgovor>.*?)</span>.*?] </span>){0,1}<span data-group="header qualifier"><span class="color_lightdark font_small" data-toggle="tooltip" data-placement="top" title=.*?>(?P<vrsta>ž|m|s|medm.|predl.|predpona|člen.|dov.|nedov.|prid.|prisl)</span>.*?(title="Tonemski naglas" data-group="header">(?P<tonemski_naglas>.*?)</span>){0,1}<span .*?'# title="Razlaga" data-group="explanation ">ples v štiričetrtinskem taktu, po izvoru iz Brazilije:</span> <span data-group=""><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Zgled" data-group="example">plesati bosso novo </span></span><br /><span class="color_lightdark" data-toggle="tooltip" data-placement="top" title="Podpomen" data-group="other">// </span><span class="color_lightdark"><span class="color_dark italic" data-toggle="tooltip" data-placement="top" title="Razlaga" data-group="explanation ">skladba za ta ples:</span></span>'
    # zadetki = re.match(vzorec, tekst, re.DOTALL)
    # koristno = zadetki.groupdict()
    # print(re.findall(vzorec, tekst, re.DOTALL))
    # return re.findall(vzorec, tekst, re.DOTALL)
    
    return [m.groupdict() for m in re.finditer(vzorec, tekst, re.DOTALL)]
    
    return koristno





def vse_strani_to_html(od, do, url, mapa, file): #url je funkcija
    zač = time.time()
    for i in range(od, do+1):
        url_to_file(url(i), mapa, file)
        print("stran", i)
        
    t1 = time.time()-zač
    # print(do-od+1, t1)
    return t1
    
def html_to_csv(mapa, html, csv):
    zač = time.time()
    print("v procesu pridobivanja posatkov iz htmlja v csv")
    tekst = file_to_string(mapa, html)
    dict_to_csv(regexanje(tekst), mapa, csv, "w")
    
    t2 = time.time()-zač
    return t2

def get_internet_speed():
    return speedtest.Speedtest(secure=True).download()

def podatki_to_dict(hitrost, t1, t2, od, do):
    št = do-od+1
    # if t1 != None and t2 != None:
    #     čas = t1+t2
    # else:
    #     čas = None
    return [{"internetna_hitrost":hitrost, "čas_html":t1, "čas_csv":t2, "strani": št}]

def podatki_to_csv(mapa, file, od, do, t1=None, t2= None):
    t = time.time()
    print("merim hitrost interneta")
    hitrost = get_internet_speed()
    slovar = podatki_to_dict(hitrost, t1, t2, od, do)
    dict_to_csv(slovar, mapa, file, "a", naslov=False)
    print(time.time()-t)

def test_časa(func):
    t = time.time()
    func
    return time.time()-t