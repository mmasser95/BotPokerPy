__author__ = 'Weed'
import Tools, Jugador, random

class Taula:

    def __init__(self):
        self.PL = []
        self.C1 = []
        self.C2 = []
        self.MAZO = Tools.shuff(Tools.genmazo())
        self.total = 0

    def returnc(self):
        return self.C2

    def repartir(self):
        for i in range(0, 2):
            for j in self.PL:
                j.ma.append(self.MAZO[0])
                self.MAZO.remove(self.MAZO[0])

        self.C2[:] = []
        for i in range(0,5):
            self.C2.append(self.MAZO[0])
            self.MAZO.remove(self.C2[i])

        for k in self.PL:
            k.taula = self.C2




lok = Taula()
for i in range(0,6):
    lok.PL.append(Jugador.Jugador(str(i),random.randint(100,999)))

lok.repartir()
for l in lok.PL:
    l.compara()