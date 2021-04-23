import math
class Figura():
    def __init__(self, iloscBokow, kolo):
        self.iloscBokow = iloscBokow
        self.kolo = kolo
class Prostokąt(Figura):
    def __init__(self, ilosBokow, kolo):
        super().__init__(ilosBokow, kolo)
    def Pole(self,bokA, bokB):
        if bokA or bokB <= 0:
            print("Bok nie może być ujemny lub równy 0")
        else:
            _pole = bokA * bokB
            print(f"Pole {object.__name__} wynosi: {_pole}")
    def Obw(self, bokA, bokB):
        if bokA or bokB <= 0:
            print("Bok nie może być ujemny lub równy 0")
        else:
            _pole = bokA * 2 + bokB * 2
            print(f"Obwód {object.__name__} wynosi: {_pole}")
class Kwadrat(Prostokąt):
    def __init__(self, ilosBokow, kolo):
        super().__init__(ilosBokow, kolo)
    def Pole(self, bokA):
        if bokA <= 0:
            print("Bok nie może być ujemny lub równy 0")
        else:
            _pole = bokA ** 2
            print(f"Pole {object.__name__} wynosi: {_pole}")
    def Obw(self, bokA):
        if bokA <= 0:
            print("Bok nie może być ujemny lub równy 0")
        else:
            _pole = bokA * 4
            print(f"Obwód {object.__name__} wynosi: {_pole}")
class Trapez(Prostokąt):
    def __init__(self, ilosBokow, kolo):
        super().__init__(ilosBokow, kolo)
    def Pole(self,bokA, bokB, wysokosc):
        if bokA or bokB or wysokosc <= 0:
            print("Bok nie może być ujemny lub równy 0")
        else:
            _pole = 0.5 * wysokosc * (bokB + bokA)
            print(f"Pole {object.__name__} wynosi: {_pole}")
class Trojkat():
    def __init__(self, ilosBokow, kolo):
        super().__init__(ilosBokow, kolo)
    def Pole(self,podstawa, wysokosc):
        if podstawa or wysokosc <= 0:
            print("Bok nie może być ujemny lub równy 0")
        else:
            _pole = podstawa * wysokosc * 0.5
            print(f"Pole {object.__name__} wynosi: {_pole}")
class Kolo():
    def __init__(self, ilosBokow, kolo):
        super().__init__(ilosBokow, kolo)
    def Pole(self,promien):
        if promien <= 0:
            print("Bok nie może być ujemny lub równy 0")
        else:
            _pole = promien ** 2 * math.pi
            print(f"Pole {object.__name__} wynosi: {_pole}")
    def Obw(self, promien):
        if promien <= 0:
            print("Bok nie może być ujemny lub równy 0")
        else:
            _pole = promien * 2 * math.pi
            print(f"Obwód {object.__name__} wynosi: {_pole}")
kwadrat = Kwadrat(2, False)
kwadrat.Pole(2)


