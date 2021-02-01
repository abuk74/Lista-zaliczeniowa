import json
import random


def Ocena(punkty):
    if punkty < 2:
        return "niedostateczny"
    elif punkty < 4:
        return "dopuszczajacy"
    elif punkty < 6:
        return "dostateczny"
    elif punkty < 8:
        return "dobry"
    elif punkty < 9:
        return "bardzo dobry"
    else:
        return "celujacy"


def Main(pytaniaJSON):
    text = open(pytaniaJSON, "r").read()
    pytania = json.loads(text)
    punkty = 0
    pytania = random.sample(pytania.items(), 10)
    for pytanie, odp in pytania:
        print(pytanie)
        odpowiedz = input("Tak/Nie")
        if odpowiedz == odp:
            punkty += 1
    print("Twoja ocena: ", Ocena(punkty))

Main("pytania.JSON")
