#https://smeo.pl/blog/rozwoj-biznesu/koszty-pracodawcy-w-5-krokach/

def Main():
    brutto = float(input("Podaj kwotę brutto: "))
    print(f"Lacznie pracodawca wydal na Ciebie: {KosztPracodawcy(brutto)}zl")
    print(f"Zarabiasz netto: {ObliczNetto(brutto)} zł")

def ObliczNetto(brutto):
    emerytalna = 0.0976 * brutto
    rentowa = 0.015 * brutto
    chorobowa = 0.0245 * brutto

    podstwa = brutto - (emerytalna + rentowa + chorobowa)

    zdrowotna = podstwa * 0.09

    kwota = brutto - emerytalna - rentowa - chorobowa - zdrowotna

    odliczenieZUS = podstwa * 0.0775
    zaliczka = kwota * 0.17 - 43.76 - odliczenieZUS
    if zaliczka < 0:
        zaliczka = 0

    return round(kwota - zaliczka, 2)

def KosztPracodawcy(brutto):
    emerytalne = brutto * 0.0976
    rentowa = brutto * 0.065
    wypadkowa = brutto * 0.0167
    fundusz = brutto * 0.0245
    fgsp = brutto * 0.01
    return brutto + emerytalne + rentowa + wypadkowa + fundusz + fgsp

Main()
