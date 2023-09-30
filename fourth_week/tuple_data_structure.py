#!/usr/bin/env python3

def get_movie_info():
    return ("Total Recall", 1990, 7.5)

def main():
    tpl = (1, 2, 3, 4, 5)
    print(tpl)
    print(type(tpl))
    print(tpl[0:2])
    #tpl[0] = 2 -> Exception
    
    title, year, score = get_movie_info()
    print(title)
    print(year)
    print(score)
    
if __name__ == "__main__":
    main()