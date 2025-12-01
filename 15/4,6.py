plik = input("Podaj nazwe pliku ")

try:
    with open(plik,"r") as f:
        tekst = f.read()

    linie = tekst.count('\n')

    znaki = len(tekst)
    slowa = len(tekst.split())

    print(f"File name: {plik}")
    print(f"Number of lines: {linie}")
    print(f"Number of characters: {znaki}")
    print(f"Number of words: {slowa}")

except FileNotFoundError:
    print("Błąd: plik nie istnieje!")