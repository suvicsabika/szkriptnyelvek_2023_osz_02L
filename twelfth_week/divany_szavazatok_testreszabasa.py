import time
import random as r

import requests


def sleep(fix=5, plus=5):
    sec = fix + r.uniform(0, plus)
    time.sleep(sec)
    return sec


def main():
    ciki_url = "https://divany.hu/offline/2016/03/19/meno_vagy_ciki_a_gyarilag_koszos_cipo/?p=&ciki=1&posztbol=1"
    # meno_url = "https://divany.hu/offline/2016/03/19/meno_vagy_ciki_a_gyarilag_koszos_cipo/?p=&meno=1&posztbol=1"

    desired_vote_count = 100
    i = 0
    while i < desired_vote_count:
        t = time.localtime()
        r_ciki = requests.get(ciki_url)
        print("Voted 'ciki' -", time.strftime("%H:%M:%S", t))
        sleep()
        i += 1


if __name__ == "__main__":
    main()