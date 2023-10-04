#!/usr/bin/env python3

def xor(kif_egy, kif_ketto):
    b1 = bool(kif_egy)
    b2 = bool(kif_ketto)
    
    if b1 and not b2 or not b1 and b2:
        return True
    
    return False

def main():
    print(xor("", "cica"))
    print(xor("", ""))
    print(xor("cica", "cica"))
    print(xor("cica", ""))

if __name__ == "__main__":
    main()
    