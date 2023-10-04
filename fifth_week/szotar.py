#!/usr/bin/env python3

def main():
    d = {}
    d['a'] = 'alfa'
    d['b'] = 'beta'
    
    #Vagy így is lehet inicializálni egy szótárat:
    # d = {
    #     'a': 'alfa',
    #     'b': 'beta'
    # }
    
    print(d, type(d))
    print(d['a'])
    
    #print(d['o']) -> KeyError Exception
    print(d.get('o'))
    print(d.get('o', "Nem található kulcs"))
    
    # in operátor kulcsokat keresi!
    print("o" in d)
    print("a" in d)
    
    d['a'] = "cica"
    print(d)
    
    #Ezek iterátorok(!) lesznek:
    print(d.keys(), type(d.keys()))
    print(d.values(), type(d.values()))
    print(d.items(), type(d.items()))
    
    #|-> Gyakori használatuk ciklusokban:
    for k, v in d.items():
        print(f"Kulcs: {k} - Érték: {v}")
        
    del d['a']
    print(d)
    
if __name__ == "__main__":
    main()