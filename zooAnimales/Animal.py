from gestion import Zona

class Animal():
    _totalAnimales = 0

    def __init__(self, nombre, edad, habitad, genero):
        self._nombre = nombre
        self._edad = edad
        self._habitad = habitad
        self._genero = genero
        self._zona = []

    def movimiento(self):
        pass

    def totalPorTipo(self):
        pass

    def toString(self):
        pass
