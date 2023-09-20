#!/usr/bin/env python3

def main():
    szamok = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    paros = []
    paratlan = []
    for szam in szamok:
        if szam % 2 == 0:
            paros.append(szam)
        else:
            paratlan.append(szam)
    
    print("Páros számok:", paros, sep="  ", end="\n\n")
    print("Páratlan számok:", paratlan, sep="  ", end="\n\n")
    
if __name__ == "__main__":
    main()