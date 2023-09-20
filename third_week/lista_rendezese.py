#!/usr/bin/env python3

def main():
    li = [2, 3, 1, 5, 4]
    
    print(sorted(li))
    print(sorted(li, reverse=True))

    li.sort()
    print(li)
    li.sort(reverse=True)
    print(li)    
    
if __name__ == "__main__":
    main()