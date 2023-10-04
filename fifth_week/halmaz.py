#!/usr/bin/env python3

def main():
    kosar = ["alma", "alma", "alma", "banán", "banán", "citrom"]
    gyumolcsok = set(kosar)
    print(gyumolcsok, type(gyumolcsok))
    
    ures_halmaz = set()
    
    print("Benne van-e az ananász?", "ananász" in gyumolcsok)
    
    gyumolcsok2 = set()
    print(gyumolcsok2)
    gyumolcsok2.add("alma")
    print(gyumolcsok2)
    
    print(gyumolcsok.intersection(gyumolcsok2))
    print(gyumolcsok.difference(gyumolcsok2))
    print(gyumolcsok.union(gyumolcsok2))
    
    gyumolcsok2.remove("alma")
    print(gyumolcsok2)
    
if __name__ == "__main__":
    main()