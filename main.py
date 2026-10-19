#!/usr/bin/env python3

import kleurmemorie, memorie

def main():
    while True:
        print("Kies een spel om te spelen:")
        print("1. Kleurmemorie")
        print("2. Memorie")

        keuze = input("Voer het nummer van het spel in (1 of 2): ")

        if keuze == "1":
            kleurmemorie.main()
        elif keuze == "2":
            memorie.main()
        else:
            print("Ongeldige keuze. Voer 1 of 2 in.")

if __name__ == "__main__":
    main()