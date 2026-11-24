import random

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


