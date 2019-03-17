__author__ = 'Weed'
import random
dic = {"A": 13,
       "2": 1,
       "3": 2,
       "4": 3,
       "5": 4,
       "6": 5,
       "7": 6,
       "8": 7,
       "9": 8,
       "T": 9,
       "J": 10,
       "Q": 11,
       "K": 12}
dic2 = {1: "2",
        2: "3",
        3: "4",
        4: "5",
        5: "6",
        6: "7",
        7: "8",
        8: "9",
        9: "T",
        10: "J",
        11: "Q",
        12: "K",
        13: "A",
        }


def maz2val(c):
    for i in range(0, len(c)):
        c[i][0] = dic.get(c[i][0])
    return c


def val2maz(val):
    return dic2.get(val)


def genmazo():
    val = "23456789TJQKA"
    pal = "CPTR"
    maz = []
    for i in pal:
        for j in val:
            maz.append([j, i])
    return maz


def shuff(maz):
    c = []
    d = []
    while len(maz)>0:
        c = random.choice(maz)
        maz.remove(c)
        d.append(c)
    return d

