
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

def WylosujPytanie(pytania):
    nrPytania = random.randint(0, len(pytania) - 1)
    #del pytania[nrPytania]
    j = 0
    for pytanie, odp in pytania.items():
        if j == nrPytania:
            return pytanie, odp
        j += 1



def QuizMain(pytaniaJSON):
    text = open(pytaniaJSON, "r").read()
    pytania = json.loads(text)
    punkty = 0

    for i in range(10):
        pytanie, odp = WylosujPytanie(pytania)
        print(pytanie)
        odpowiedz = input("Tak/Nie")
        if odpowiedz == odp:
            punkty += 1
    print(f"Twoja ocena: {Ocena(punkty)}")

QuizMain("pytania.JSON")
