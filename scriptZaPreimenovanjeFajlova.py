import os
import tkinter
from tkinter import filedialog
from tkinter import simpledialog

# Otvaranje dijaloškog okvira za odabir datoteka
root = tkinter.Tk()
root.withdraw() # Sakrivanje glavnog prozora
putanja = filedialog.askopenfilenames(title="Odaberite datoteke za preimenovanje")

# Ako korisnik nije odabrao datoteke, izađi iz programa
if not putanja:
    print("Niste odabrali nijednu datoteku.")
    exit()

# Traži od korisnika novo ime za datoteke
novo_ime = simpledialog.askstring("Novo ime", "Unesite novo ime za datoteke (bez ekstenzije):")

# Ako korisnik nije unio novo ime, izađi iz programa
if not novo_ime:
    print("Niste unijeli novo ime.")
    exit()

# Petlja kroz odabrane datoteke i preimenuj ih
for put in putanja:
    direktorij, staro_ime = os.path.split(put)
    ekstenzija = os.path.splitext(staro_ime)[1]
    novo_put = os.path.join(direktorij, novo_ime + ekstenzija)
    os.rename(put, novo_put)
    print(f"Preimenovala datoteka: {staro_ime} -> {novo_ime}{ekstenzija}")

print("Preimenovanje je završeno!")
