
#Bazuje na:
#https://stackoverflow.com/questions/2192533/function-to-return-date-of-easter-for-the-given-year
#https://dateutil.readthedocs.io/en/stable/_modules/dateutil/easter.html
#https://mattomatti.com/pl/a0041

def Main():
    print("Podaj date:")
    dzien = int(input("Podaj dzien"))
    miesiac = int(input("Podaj miesiac"))
    rok = int(input("Podaj rok"))

    print("Podaj date urodzenia:")
    dzienUrodzin = int(input("Podaj dzien urodzenia"))
    miesiacUrodzin = int(input("Podaj miesiac urodzenia"))
    rokUrodzin = int(input("Podaj rok urodzenia"))

    print("Wielkanoc wypada w: ", Wielkanoc(rok))
    print("Wczoraj bylo: ", Wczoraj(dzien, miesiac, rok))
    print("Jutro bedzie:", Jutro(dzien, miesiac, rok))

    dni = ["pon", "wt", "sr", "czw", "pt", "so", "nd"]
    nrDnia = Dzien(dzien, miesiac, rok)
    print("Dzien tygodnia: ", dni[nrDnia])

    DzienUrodzin(dzienUrodzin, miesiacUrodzin, rokUrodzin)

def Wielkanoc(y):
    a = y % 19
    b = y % 4
    c = y % 7
    d = (19*a + 24) % 30
    e = (2*b+4*c+6*d+5) % 7
    marzec = 22 + d + e
    kwiecien = d + e - 9
    if marzec > 31:
        return kwiecien, 4, y
    else:
        return marzec, 3, y

def Wczoraj(dzien, miesiac, rok):
    miesiace = Miesiac(rok)
    nowyRok = rok
    nowyMiesiac = miesiac
    nowyDzien = dzien - 1
    if nowyDzien == 0:
        nowyMiesiac = miesiac - 1
        if nowyMiesiac == 0:
            nowyRok = rok - 1
            nowyMiesiac = 12
            nowyDzien = 31
        else:
            nowyDzien = miesiace[nowyMiesiac-1]
    return nowyDzien, nowyMiesiac, nowyRok

def Przestepny(rok):
    if rok % 4 == 0 and rok % 100 != 0:
        return True
    elif rok % 400 == 0:
        return True
    else:
        return False


def Miesiac(rok):
    luty = 28
    if Przestepny(rok):
        luty = 29
    miesiace = [31, luty, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return miesiace


def Jutro(dzien, miesiac, rok):
    miesiace = Miesiac(rok)
    nowyRok = rok
    nowyMiesiac = miesiac
    nowyDzien = dzien + 1
    if nowyDzien > miesiace[miesiac - 1]:
        nowyMiesiac = miesiac + 1
        if nowyMiesiac > 12:
            nowyRok = rok + 1
            nowyMiesiac = 1
        nowyDzien = 1
    return nowyDzien, nowyMiesiac, nowyRok

def Dzien(dzien, miesiac, rok):
    miesiace = [0, 3, 3, 6, 1, 4, 6, 2, 5, 0, 3, 5]
    q = (rok - 1) // 4 - (rok - 1)//100 + (rok - 1)//400
    p = (rok - 1) + q
    p += miesiace[miesiac - 1]
    if miesiac > 2 and Przestepny(rok):
        p += 1
    p += dzien - 1
    return p % 7

def DzienUrodzin(dzien, miesiac, rok):
    dni = ["pon", "wt", "sr", "czw", "pt", "so", "nd"]
    nrDnia = Dzien(dzien, miesiac, rok)
    print("Dzien urodznia: ", dni[nrDnia])

Main()
