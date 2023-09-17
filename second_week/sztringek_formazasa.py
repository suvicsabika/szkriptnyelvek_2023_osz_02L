#!/usr/bin/env python3

def hello(name, color, what):
    #C-ben:
    #printf("%s, %s az %s!\n", name, color, what);
    
    #Python-ban:
    #1
    print("{0}, {1} az {2}".format(name, color, what))
    #2
    print("{}, {} az {}".format(name, color, what))
    #3
    print("{nev}, {szin} az {mi}".format(nev=name, szin=color, mi=what))
    #4
    #print(f"{1+1})
    print(f"{name.capitalize()}, {color} az {what}")
    
def main():
    hello("csabi", "kek", "eg")
    
if __name__ == "__main__":
    main()