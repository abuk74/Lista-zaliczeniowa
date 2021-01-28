
def Main():
    odp = input("Czy wymieniasz dolary na inna walute? TAK/NIE")
    if odp == "TAK":
        kwota = float(input("Podaj kwote do wymiany: "))
        waluta = input("Na jaka walute wymienic? THB, BTC, BTN, MRO, ETH, PLN ")
        print(f"{kwota}$ = {Wymiana(kwota, waluta, True)}{waluta}")
    else:
        waluta = input("Jaka walute wymienic na dolary? THB, BTC, BTN, MRO, ETH, PLN")
        kwota = float(input("Podaj kwote do wymiany: "))
        print(f"{kwota}{waluta} = {Wymiana(kwota, waluta, False)}$")

def Wymiana(kwota, waluta, dolar):
    przelicznik = {
        "THB" : 0.33,
        "BTC" : 37320,
        "BTN" : 0.14,
        "MRO" : 0.27,
        "ETH" : 1416.12,
        "PLN" : 0.27 #najdziwniejsza waluta
    }
    if waluta in przelicznik:
        if dolar:
            return kwota / przelicznik[waluta]
        else:
            return kwota * przelicznik[waluta]
        
Main()
