#!/usr/bin/env python3

def main():
    print("1. feladat: ")
    li1 = ['auto', 'villamos', 'metro']
    li1_comp = [s.upper() for s in li1]
    print(li1, "->", li1_comp)
    print()

    print("2. feladat: ")
    li2 = ['aladar', 'bela', 'cecil']
    li2_comp = [s.capitalize() for s in li2]
    print(li2, "->", li2_comp)
    print()

    print("3. feladat: ")
    li3 = [0 for n in range(10)]
    print(li3)
    print()

    print("4. feladat: ")
    li4 = [n for n in range(1, 10 + 1)]
    li4_comp = [n+n for n in li4]
    print(li4, "->", li4_comp)
    print()

    print("5. feladat: ")
    li5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    li5_comp = [int(s) for s in li5]
    print(li5, "->", li5_comp)
    print()

    print("6. feladat: ")
    s1 = "1234567"
    li6 = [int(c) for c in list(s1)]
    print(s1, "->", li6)
    print()
    
if __name__ == "__main__":
    main()