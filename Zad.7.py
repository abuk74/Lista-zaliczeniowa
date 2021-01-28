
#Bazuje na:
#https://stackoverflow.com/questions/2192533/function-to-return-date-of-easter-for-the-given-year
#https://dateutil.readthedocs.io/en/stable/_modules/dateutil/easter.html

import datetime

def Main():
    print("Podaj date:")
    dzien = int(input("Podaj dzien"))
    miesiac = int(input("Podaj miesiac"))
    rok = int(input("Podaj rok"))
    data(dzien, miesiac, rok)


def data(D, M, R):
    wczoraj = data_wczoraj(D, M, R)
    print(f"Wczoraj bylo: {wczoraj}")
    jutro = data_jutro(D, M, R)
    print(f"Jutro bedzie: {jutro}")
    w = Easter(R)
    print(f"Wielkanoc wypada w: {w}")
    dni = ["pon", "wt", "sr", "czw", "pt", "so", "nd"]
    nr_dnia = dzien_tygodnia(D, M, R)
    print(f"Dzien tygodnia: {dni[nr_dnia]}")


def czy_przestepny(R): #Rok przestępny jest raz na 4 lata ( W 2016, 2020 , 2024 itp )
    if R % 4 == 0 and R % 100 != 0:
        return True
    elif R % 400 == 0:
        return True
    else:
        return False


#Latami przestępnymi są te, których numeracja jest podzielna przez 4 i niepodzielna przez 100 lub jest podzielna przez 400.
def pobierz_miesiace(R):
    luty = 28
    if czy_przestepny(R):
        luty = 29
    miesiace = [31, luty, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return miesiace


def data_wczoraj(D, M, R):
    miesiace = pobierz_miesiace(R)
    nowy_rok = R
    nowy_miesiac = M
    nowy_dzien = D - 1 #przesuwamy sie o jeden dzien do tylu
    if nowy_dzien == 0: #jesli mamny np 1 stycznia to przechodzimy na poprzedni miesiac (a nawet rok)
        nowy_miesiac = M - 1 #przesuwamy sie na poprzedni miesiac
        if nowy_miesiac == 0: #przesuwamy sie na poprzedni rok
            nowy_rok = R - 1
            nowy_miesiac = 12
            nowy_dzien = 31
        else:
            nowy_dzien = miesiace[nowy_miesiac-1]
    return nowy_dzien, nowy_miesiac, nowy_rok


def data_jutro(D, M, R):
    miesiace = pobierz_miesiace(R)
    nowy_rok = R
    nowy_miesiac = M
    nowy_dzien = D + 1
    if nowy_dzien > miesiace[M - 1]:
        nowy_miesiac = M + 1
        if nowy_miesiac > 12:
            nowy_rok = R + 1
            nowy_miesiac = 1
        nowy_dzien = 1
    return nowy_dzien, nowy_miesiac, nowy_rok

def Easter(year, method=3): # 3 to kalendarz gregorianski

    if not (1 <= method <= 3):
        raise ValueError("invalid method")

    # g - Golden year - 1
    # c - Century
    # h - (23 - Epact) mod 30
    # i - Number of days from March 21 to Paschal Full Moon
    # j - Weekday for PFM (0=Sunday, etc)
    # p - Number of days from March 21 to Sunday on or before PFM
    #     (-6 to 28 methods 1 & 3, to 56 for method 2)
    # e - Extra days to add for method 2 (converting Julian
    #     date to Gregorian date)

    y = year
    g = y % 19
    e = 0
    c = y//100
    h = (c - c//4 - (8*c + 13)//25 + 19*g + 15) % 30
    i = h - (h//28)*(1 - (h//28)*(29//(h + 1))*((21 - g)//11))
    j = (y + y//4 + i + 2 - c + c//4) % 7

    # p can be from -6 to 56 corresponding to dates 22 March to 23 May
    # (later dates apply to method 2, although 23 May never actually occurs)
    p = i - j + e
    d = 1 + (p + 27 + (p + 6)//40) % 31
    m = 3 + (p + 26)//30
    return datetime.date(int(y), int(m), int(d))
