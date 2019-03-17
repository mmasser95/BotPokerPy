__author__ = 'Weed'
from Tools import maz2val, val2maz


class Comparator:

    def __init__(self):
        self.values = {"valcartaalta": [], #se necessita una llista per ficar el valor i el kick
                       "valparella": [],
                       "valtrio": [],
                       "valdobleparella": [],
                       "valescala": [],
                       "valcolor": [],
                       "valfull": [],
                       "valpoker": [],
                       "valescolor": [],
                       "valreal": []}
        self.id = {"idcartaalta": 0,
                   "idparella": 1,
                   "iddobleparella": 2,
                   "idtrio": 3,
                   "idescala": 4,
                   "idcolor:": 5,
                   "idfull": 6,
                   "idpoker": 7,
                   "idescolor": 8,
                   "idreal": 9}

    def comparar(self, ma, taula):
        mix = []
        c = []
        m1 = maz2val(ma)
        m2 = maz2val(taula)
        for i in m1:
            mix.append(i)
        for i in m2:
            mix.append(i)
        for i in range(0, 1):
            for j in range(i+1, len(mix)-4):
                for k in range(j+1, len(mix)-3):
                    for l in range(k+1, len(mix)-2):
                        for m in range(l+1, len(mix)-1):
                            c[:] = []
                            c.append(mix[i])
                            c.append(mix[j])
                            c.append(mix[k])
                            c.append(mix[l])
                            c.append(mix[m])
                            #fins aqui guay, ara comensa la puta tralla
                            # if self.parella(c)and not self.trio(c) and not self.poker(c) and not self.dobleParella(c)\
                            #         and not self.full(c):
                            #     print "parella"
                            # elif self.dobleParella(c) and not self.poker(c):
                            #     print "doble parella"
                            # elif self.trio(c) and not self.poker(c) and not self.full(c):
                            #     print "trio"
                            # elif self.escalera(c):
                            #     print "escalera"
                            # elif self.color(c):
                            #     print "color"
                            # elif self.poker(c):
                            #     print "poker"
                            # elif self.full(c):
                            #     print "full"
                            if self.escalerareal(c):
                                print "Escala Real"

                            elif self.escaleracolor(c):
                                print "Escala Color"
                            elif self.poker(c):
                                print "Poker"
                            elif self.full(c):
                                print "Full"
                            elif self.color(c):
                                print "Color"
                            elif self.escalera(c):
                                print "Escala"
                            elif self.trio(c):
                                print "Trio"
                            elif self.dobleParella(c):
                                print "Doble Parella"
                            elif self.parella(c):
                                print "Parella" + str(self.values.get("valparella"))
                            else:
                                print "Carta Alta"
                            pass

    def parellaFunc(self, c1, c2):
        if c1[0] == c2[0]:
            return True
        else:
            return False

    def parella(self, c):
        for i in range(0, len(c)-1):
            for j in range(i+1, len(c)):
                if self.parellaFunc(c[i], c[j]):
                    self.values["valparella"].append(c[i][0])
                    return True
        return False

    def trio(self, c):
        for i in range(0, len(c)-2):
            for j in range(i+1, len(c)-1):
                for k in range(j+1, len(c)):
                    if c[i][0] == c[j][0] and c[j][0] == c[k][0]:
                        self.values["valtrio"].append(c[i][0])
                        return True
        return False

    def dobleParella(self, c):
        count = 0
        for i in range(0, len(c)-1):
            for j in range(i+1, len(c)):
                if self.parellaFunc(c[i], c[j]):
                    self.values["valdobleparella"].append(c[i][0])
                    if count == 2:
                        return True
        return False

    def poker(self, c):
        for i in range(0, len(c)-3):
            for j in range(i+1, len(c)-2):
                for k in range(j+1, len(c)-1):
                    for l in range(k+1, len(c)):
                        if c[i][0] == c[j][0] and c[j][0] == c[k][0] and c[k][0] == c[l][0]:
                            self.values["valpoker"].append(c[i][0])
                            return True
        return False

    def full(self, c):
        if not len(c) < 4:
            for i in range(0, len(c)-3):
                for j in range(i+1, len(c)-2):
                    for k in range(j+i, len(c)-1):
                        if c[i] == c[j] and c[j] == c[k]:
                            c.remove(c[i])
                            c.remove(c[j])
                            c.remove(c[k])
                            if self.parella(c):
                                return True
        return False

    def color(self, c):
        count = 0
        palo = c[0][1]
        for i in range(0, len(c)):
            if c[i][1] == palo:
                count += 1
        if count == 5:
            return True
        return False

    def escalera(self, c):
        a = []
        for i in c:
           a.append(i[0])
        a.sort()
        b = a[0]
        try:
            for i in range(1, len(a)):
                if a[i] != int(b) + 1:
                    return False
                else:
                    b = a[i]
            return True
        except:
            print "Error am mierda escalera"
            return False

    def escaleracolor(self, c):
        if self.escalera(c)and self.color(c):
            return True
        return False



    def escalerareal(self, c):
        pass
