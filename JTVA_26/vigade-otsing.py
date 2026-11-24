from math import * # oli valesti pandud seega panin õigesti
import math

print("Ruudu karakteristikud")

a = int(input("Sisesta ruudu külje pikkus =>")) #panin int() kuna see tahab ,et ma sisestaks külje pikkuse

S = a ** 2 # panin vahed sisse ,et õige oleks

print("Ruudu pindala on", S)

P = 4 * a # panin vahed sisse ,et õige oleks

print("Ruudu ümbermõõt", P) # '' oli pandud lõppu, vahetasin " vastu

di = a * math.sqrt(2) # jätsin vahed sisse 

print("Ruudu diagonaal", round(di,2)) # 

print()

print("Ristküliku karakteristikud")

b = int(input("Sisesta ristküliku 1. külje pikkus => "))

c = int(input("Sisesta ristküliku 2. külje pikkus => "))

S = b * c

print("Ristküliku pindala", S)

P =  2*(a+b)

print("Ristküliku ümbermõõt", P)

di=math.sqrt(b*2+c*2)

print("Ristküliku diagonaal", round(di))

print()

print("Ringi karakteristikud")

r = int(input("Sisesta ringi raadiusi pikkus => "))

d = 2 * r

print("Ringi läbimõõt", d)

S = pi * r *2

print("Ringi pindala", round(S))

C = 2 * pi * r

print("Ringjoone pikkus ", round(C))
