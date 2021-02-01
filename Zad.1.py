#https://poradnikprzedsiebiorcy.pl/-jak-wyliczac-wynagrodzenia
#ubezpieczenie emerytalne, rentowe, chorobowe, zdrowotne, zaliczka na PIT

#odjęcie od otrzymanego podatku kwoty wolnej od podatku, kwota ta jest ustanowiona ustawowo i jej miesięczna wysokość wynosi 43,76 zł

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


kwota = float(input("Podaj kwote brutto: "))
print("Kwota netto wynosi: ", ObliczNetto(kwota))
