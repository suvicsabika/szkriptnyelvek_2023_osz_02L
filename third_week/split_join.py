#!/usr/bin/env python3

def main():
    li = ["c", "i", "c", "a"]
    cica = "".join(li)
    print(cica)
   
    weblap_kod = """<!DOCTYPE html>
<html lang="hu">
    <head>
        <title>Szkriptnyelvek</title>
    </head>
    <body>
        <p>Szkriptnyelvek</p>
    </body>
</html>"""
    print(weblap_kod)
    weblap_kod_darabonkent = weblap_kod.split()
    print(weblap_kod_darabonkent)
    
    ip_cim = "192.168.1.1"
    ip_cim_darabonkent = ip_cim.split(".")
    print(ip_cim_darabonkent)
    
if __name__ == "__main__":
    main()