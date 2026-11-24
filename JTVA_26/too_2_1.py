




eesnimi = input("Sisesta oma eesnimi: ")
if eesnimi.lower() == "juku": #"JUKU". lower() => "juku"
    print("Lähme Jukuga kinno!")
    if eesnimi.isupper():
        print("Ära karju, Juku!")
else:
    print("Täna kinno ei minda.")
vanus = input("Sisesta oma vanus:")
if not vanus.isdigit():
       print("Palun sisesta kehtiv vanus täisarvuna.")
else:
    vanus = int(vanus)
if vanus < 0 or vanus > 100:
       print("Viga andmetes: vanus peab olema vahemikus 0-100.")
elif vanus < 6:
       print("Sulle on kinno sissepääs TASUTA!")
elif vanus <= 14:
       print("Sulle on vaja osta LAPSEPILET.")
elif vanus <=65:
       print("Sulle on vaja osta TÄISPILET")
elif vanus > 65:
       print("Sulle on vaja osta SOODUSPILET")

else:
       print("Täna kinno ei minda.")


       
# Küsi kahe inimese nimed. Kontrolli, kas mõlemad nimed koosnevad ainult tähtedest. Kui jah, teata kasutajale, kas nad on täna pinginaabrid või mitte. Kui mõnes nimes on numbreid või muid märke, kuva veateade.

# Otsusta ise, kuidas „pinginaabrid“ määratakse, näiteks juhuslikult või nimede algustähtede järgi.

# Kasuta: isalpha(), capitalize()

Pinginaabrid = ["Mati","Kati","Juku"]
eesnimi1 = input("Sisesta esimese inimese eesnimi: ")
eesnimi2 = input("Sisesta teise inimese eesnimi: ")
if eesnimi1.isalpha() and eesnimi2.isalpha():
    if eesnimi1.capitalize() is Pinginaabrid and eesnimi2.capitalize() in Pinginaabrid:
        print("Inimesed on täna pinginaabrid.")
    else:
        print("Inimesed ei ole täna pinginaabrid.")
else:
        print("Palun sisesta kehtivad nimed.")
        

        #3 ül - remont
try:
    pikkus = float(input("Sisesta toa pikkus meetrites: "))
    laius = float(input("Sisesta toa laius meetrites: "))
    pindala = pikkus * laius
    print(f"Põranda pindala on {round(pindala, 2)} ruutmeetrit.") #round() ümardab 2 kohta
    #pärast koma
    
    remont = input("Kas soovid remonti teha? (jah/ei)").lower()
    if remont == "jah":
        try:
            hind = float(input("Sisesta põrandakatte hind ruutmeetri kohta: "))
            koguhind = pindala * hind
            print(f"Põranda vahetamise hind on {round(hind, 2)} eurot.")
            abi = input("Kas kasutad professionaali abi?").lower()
            if abi == "jah":
                too = float(input("Sisesta töö hind ruutmeetri kohta: "))
                koguhind = koguhind + pindala * too
        except ValueError:
            print("Palun sisesta kehtiv ujukomaarv ruutmmeetri hinnaks.")
    else:
            print("Remonti ei tehta.")

except ValueError:
            print("Palun sisesta kehtiv ujukomaarv.")


# 4 ül - allahindlus
hind = int(input("Sisesta toote alghind: "))
try:
    if hind > 700:
        hind = hind * 0.7
except ValueError:
    print("Palun sisesta arv.")
print("Lõplik hind on ", round(hind, 2), "eurot")

#5 ül - temp
try:
    temperatuur = int(input("Sisesta toatemperatuuri näit: "))
    if temperatuur > 18:
        print("Temperatuur on üle 18 kraadi.")
    else:
        print("Temperatuur ei ole üle 18 kraadi.")
except ValueError:
    print("Sisesta temperatuur numbrina.")

    #6 ül pikkus
    pikkus = float(input("Sinu pikkus sentimeetrites: "))
    if pikkus < 160:
        print("Oled lühike")
    elif pikkus <= 180:
        print("Oled keskmise pikkusega")
    else:
        print("Oled pikk")


    #7. pikkus ja sugu

pikkus = float(input("Sisesta oma pikkus sentimeetrites: "))
sugu = input("sisesta oma sugu (M või N): ").lower()
if sugu == "m" or sugu == "mees":
    print("Sinu sugu on mees")
    if pikkus < 170:
        print("Oled lühike mees.")
    elif pikkus <= 185:
        print("Oled keskmise pikkusega mees.")
    else:
        print("Oled pikk mees.")
elif sugu == "n" or sugu == "naine":
    print("Sinu sugu on naine.")
    if pikkus <160:
        print("Oled lühike naine.")
    elif pikkus <= 175:
        print("Oled keskmise pikkusega naine.")
    else:
        print("Oled pikk naine.")
else:
    print("Vigane sisestus!")

    #8. ül - poes

    import random
    tooted = ["piim", "leib", "sai", "kohupiim"]
    ostukorv = []
    kogusumma = 0

    for toode in tooted:
        hind = round(random.uniform(0.5, 3), 2)
        print(toode, "hind:", hind, "eurot")

        vastus = input("Kas tahad osta? ").lower()

        if vastus == "jah":
            while True:
                kogus = input("Sisesta kous: ")

                if kogus.isdigit():
                    kogus = int(kogus)
                    break
                else:
                    print("Sisesta täisarv")

            summa = hind * kogus
            kogusumma += summa

            ostukorv.append([toode, kogus, hind, summa])
print("\nOstukorv:")
for toode in ostukorv:
    print(toode[0], "Kogus:", toode[1],
          "Hind:", toode[2], "Summa:", round(toode[3], 2))
    print("Kõigi ostude summa:", round(kogusumma, 2), "eurot")