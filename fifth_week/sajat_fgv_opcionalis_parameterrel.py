#!/usr/bin/env python3

def koszono(nev, koszones="Szia", vegjel="!"):
    print(f"{koszones} {nev}{vegjel}")

def main():
    koszono("Csabi")
    koszono("Csabi", koszones="Hi")
    koszono("Csabi", koszones="Hi", vegjel=".")
    koszono("Csabi", "Hi", ".")
    koszono("Csabi", vegjel=".")
    
if __name__ == "__main__":
    main()