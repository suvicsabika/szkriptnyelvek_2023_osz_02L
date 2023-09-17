#!/usr/bin/env python3

def main():
    b = "Batman"
    print(len(b))
    print(b[0])
    print(b[1:4])
    print(b[:4])
    print(b[2:])
    print(b[:])
    
    print(b[-1])
    print(b[-6])
    print(b[-3:])
    print(b[:-3])
    print(b[-5:-2])
    
    print(b[::-1])
    print(b[::2])
    print(b[2::2])
    
if __name__ == "__main__":
    main()