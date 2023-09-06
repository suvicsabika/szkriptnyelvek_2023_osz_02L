#!/usr/bin/env python3

import sys

def main():
    if sys.argv[1] == "Batman" or sys.argv[1] == "Robin":
        print("Denevérveszély!")
    else:
        print("Hello " + sys.argv[1] + "!")
    
if __name__ == "__main__":
    main()