import re

tekst = input("Wpisz dowolny tekst: ")

samogloski = re.findall(r'[aeiouyąęóąAEIOUYĄĘÓ]', tekst)

liczba = len(samogloski)

print(f"Liczba samogłosek: {liczba}")