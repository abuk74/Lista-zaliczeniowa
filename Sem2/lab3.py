class Restaurant:
    def __init__(self, nazwa, NIP, REGON, adres, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow, oferujeDowoz)
        self.nazwa = nazwa
        self.NIP = NIP
        self.REGON = REGON
        self.adres = adres
        self.specjalizacja = specjalizacja
        self.wielkoscLokalu = wielkoscLokalu
        self.iloscPracownikow = iloscStolikow
        self.iloscPracownikow = iloscPracownikow
        self.oferujeDowoz = oferujeDowoz

class IceCreamStand(Restaurant):
    flavour = ["vanilla", "cherry", "kiwi", "chocolatte", "strawberry", "mango", "mascarpone", "pistace", "cream", "lemon", "watermelon", "melon", "coffeeEspresso", "coffeLatte", "whiteChocolatte"]
    def __init__(self, nazwa, NIP, REGON, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow, flavour):
        super().__init__(self, nazwa, NIP, REGON, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow)
        self.flavour = flavour

    def present(self):
        print(f"Tutaj pelna lista smaków: {self.flavour}")

    def numbersIce(self):
        rodzaj = input("Czy chcesz do kubka czy do różka? (Kubek / Rozek)")
        if rodzaj.capitalize() == "Kubek":
            num = int(input("Wybrałeś kubek. Możesz do niego poprosić maksymalnie trzy gałki. Ile chcesz? "))
        elif rodzaj.capitalize() == "Rozek":
            num = int(input("Wybrałeś rożek. Ile chcesz gałek? "))
        return num



class CoffeShop(Restaurant):
    coffeTypes = ["latte", "americano", "cappuccino", "flatWhite", "mocca", "latteMacchiato", "espresso"]
    def __init__(self, coffeType)
        super().__init__()
        self.coffeType = coffeType
    def AddCofeeType():
        newCoffe = input("Podaj nazwe nowej kawy")
        exists = false
        for item in coffeTypes:
            if newCoffe == item:
                exists = true
        if !exists:
            coffeTypes.append(newCoffe)
    def availableCoffes():
        for items in coffeTypes:
            print("Dostępne kawy:")
            print items
    def orderCoffe():
        print availableCoffes
        order = input("Wybierz kawę: ")
        if order in coffeTypes:
            addEspresso = input(("Wzmocnić kawę dodatkowym espresso?"))
            if addEspresso.upper() == "TAK":
                print(order " + double espresso")
            else:
                print (order)
        else:
            print("Nie posiadamy takiej kawy :c")



class Main:
    lokalneRestauracje = []
    def AddRestaurant():
        newRestaurant = input("Podaj nazwe nowej restauracji")
        lokalneRestauracje.append(newRestaurant)
    def ShowLocalRestaurants():
        print(lokalneRestauracje)
