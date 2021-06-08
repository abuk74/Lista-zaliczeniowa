#zadanie grupowe

class Restaurant:
    def __init__(self, nazwa, NIP, REGON, adres, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow,
                 oferujeDowoz):
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
    flavour = ["vanilla", "cherry", "kiwi", "chocolatte", "strawberry", "mango", "mascarpone", "pistace", "cream",
               "lemon", "watermelon", "melon", "coffeeEspresso", "coffeLatte", "whiteChocolatte"]

    def __init__(self, nazwa, NIP, REGON, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow, oferujeDowoz,
                 flavour):
        super().__init__(self, nazwa, NIP, REGON, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow,
                         oferujeDowoz)
        self.flavour = flavour

    def present(self):
        print(f"Tutaj pelna lista smaków: {self.flavour}")

    def numbersIce(self):
        rodzaj = input("Czy chcesz do kubka czy do różka? (Kubek / Rozek)")
        if rodzaj.capitalize() == "Kubek":
            num = int(input("Wybrałeś kubek. Możesz do niego poprosić maksymalnie trzy gałki. Ile chcesz? "))
            return num
        elif rodzaj.capitalize() == "Rozek":
            num = int(input("Wybrałeś rożek. Ile chcesz gałek? "))
            return num

    def kubek(self, num):
        galki = []

        IceCreamStand.present(self)
        for i in num:
            galka = str(input(f"Podaj smak gałki: "))
            galki.append(galka)
        return "Zamówiłeś: ", galki


class CoffeShop(Restaurant):
    coffeTypes = ["latte", "americano", "cappuccino", "flatWhite", "mocca", "latteMacchiato", "espresso"]

    def __init__(self, nazwa, NIP, REGON, adres, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow,
                 oferujeDowoz, coffeType):
        super().__init__(nazwa, NIP, REGON, adres, specjalizacja, wielkoscLokalu, iloscStolikow, iloscPracownikow,
                         oferujeDowoz)
        self.coffeType = coffeType


    def AddCofeeType(self):
        newCoffe = input("Podaj nazwe nowej kawy")
        exists = False
        for item in self.coffeTypes:
            if newCoffe == item:
                exists = True
        if not exists:
            self.coffeTypes.append(newCoffe)

    def availableCoffes(self):
        for items in self.coffeTypes:
            print("Dostępne kawy:")
            return items

    def orderCoffe(self):
        CoffeShop.availableCoffes(self)
        order = input("Wybierz kawę: ")
        if order in self.coffeTypes:
            addEspresso = input("Wzmocnić kawę dodatkowym espresso?")
            if addEspresso.upper() == "TAK":
                print(order + "double espresso")
            else:
                print(order)
        else:
            print("Nie posiadamy takiej kawy :c")


class Main:
    def __init__(self):
        self.lokalneRestauracje = []
        lodziarnia = IceCreamStand("Fabryka lodów", 123456789, 987654321, "Lodziarnia", 40, 8, 4, False, IceCreamStand.flavour)
        self.lokalneRestauracje.append(lodziarnia)

    def AddRestaurant(self):
        nazwa = input("Podaj nazwe nowej restauracji ")
        NIP = int(input("Podaj NIP "))
        REGON = int(input("Podaj REGON "))
        adres = input("Podaj adres: ")
        powierzchnia = int(input("Jaka jest powierzchnia lokalu? "))
        stoliki = int(input("Ile jest stolików w lokalu? "))
        dowoz = bool(input("Czy oferuje dowóz? "))
        specjalizacja = input("Jaka jest specjalizacja? ")
        if specjalizacja.capitalize() == "Lodziarnia":
            newRestaurant = IceCreamStand(nazwa, NIP, REGON, adres, specjalizacja, powierzchnia, stoliki, dowoz,
                                          IceCreamStand.flavour)
            self.lokalneRestauracje.append(newRestaurant)
        elif specjalizacja.capitalize() == "Kawiarnia":
            newRestaurant = CoffeShop(nazwa, NIP, REGON, adres, specjalizacja, powierzchnia, stoliki, dowoz, "lol",
                                      CoffeShop.coffeTypes)
            self.lokalneRestauracje.append(newRestaurant)

    def ShowLocalRestaurants(self):
        repr(self.lokalneRestauracje)


Main.ShowLocalRestaurants(Main)