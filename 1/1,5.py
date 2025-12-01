import os
os.chdir(os.path.dirname(__file__))

with open("countries.txt", "r", encoding="utf-8") as plik:
    linie = plik.readlines()

nr = 1
for linia in linie:
    dane = linia.strip().split()
    print(f"{nr}. {dane[0]}, {dane[1]}, {dane[2]}")
    nr +=1