#https://www.instalki.pl/aktualnosci/hardware/22174-dlaczego-dysk-ma-mniej-gb.html

def PrawdziwaPojemnosc(pojemnoscWedlugProducenta):
    bajty = pojemnoscWedlugProducenta * 1000000000
    return round(bajty / 1024 / 1024 / 1024, 2)


gb = float(input("Podaj rozmiar w GB"))
print("Faktyczny rozmiar w GB wynosi: ", PrawdziwaPojemnosc(gb))
