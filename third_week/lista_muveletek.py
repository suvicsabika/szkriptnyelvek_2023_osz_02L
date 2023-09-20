#!/usr/bin/env python3

def main():
    li = [1, 2, 3]
    
    li.append(4)
    print(li)
    
    li.pop()
    li.pop(0)
    del li[0]
    print(li)
    
    li2 = [1, 2, 3] + [4, 5 ,6]
    print(li2)
    
    print(3 in li)
    
    print(sum(li2))
    print(min(li2))
    print(max(li2))
    
if __name__ == "__main__":
    main()