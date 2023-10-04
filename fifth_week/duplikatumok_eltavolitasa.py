#!/usr/bin/env python3

def main():
    szamok = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
    print(szamok)
    #A sorted() minden esetben egy új rendezett LISTÁVAL tér vissza
    duplikatumok_nelkul = sorted((set(szamok)))
    print(duplikatumok_nelkul)
    
if __name__ == "__main__":
    main()