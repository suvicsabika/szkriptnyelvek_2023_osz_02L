#!/usr/bin/env python3

def main():
    s = "Csabi"
    
    print(s.lower())
    print(s.upper())
    print(s.isalpha())
    print(s.startswith("Cs"))
    print(s.find("Cs"))
    print(s.replace("Cs", "cs"))
    
if __name__ == "__main__":
    main()