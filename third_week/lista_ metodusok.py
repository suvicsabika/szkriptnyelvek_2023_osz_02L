#!/usr/bin/env python3

def main():
    li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        
    li.pop()
    li.pop(0)
    print(li)
    
    li.append(10)
    print(li)
    
    li.insert(0, 1)
    li.insert(8, 9)
    print(li)
    
    li2 = [11, 12, 13, 14, 15]
    li.extend(li2)
    print(li)
    
    li.remove(1)
    print(li)
    
if __name__ == "__main__":
    main()