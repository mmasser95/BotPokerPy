__author__ = 'Weed'
import Comparador

class Jugador():

    def __init__(self, name, pot, ):
        self.ma = []
        self.taula = []
        self.name = name
        self.pot = pot
        self.comparador = Comparador.Comparator()

    def compara(self):
        print "Jugador " + str(self.name)
        self.comparador.comparar(self.ma, self.taula)