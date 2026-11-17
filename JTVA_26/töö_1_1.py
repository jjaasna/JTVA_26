# 1. harjutus
from cmath import pi
from random import randint
import math



print("Tere, maailm!")
nimi = input ("Mis on sinu nimi? ")
print(f"Tere, maailm! Tervitan sind {nimi}")
vanus = input ("Mis on sinu vanus? ")
print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")


# 2. harjutus
vanus = 19
eesnimi = "Jaak"
pikkus = 16.5
kas_käib_koolis = True
print("vanus", type(vanus))
print("eesnimi", type(eesnimi))
print("pikkus", type(pikkus))
print("kas käib koolis", type(kas_käib_koolis))

# 3. harjutus
kommid = randint(1, 100)
print("kommide arv: ", kommid)
karv = int(input("Mitu kommi tahad ära võtta?"))
print(kommid - karv)

# 4. harjutus
C = float(input("Ringjoone pikkus: "))
D = round(C / math.pi, 2)
print (f"puu läbimõõt on: {D}")