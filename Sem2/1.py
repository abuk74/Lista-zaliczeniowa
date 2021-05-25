class Car:
    def __init__(self, brand, model, mileage, color, price, body):
        self.brand = brand
        self.model = model
        self. mileage = mileage
        self.color = color
        self.price = price
        self.body = body

    def driveStraight(self):
        return "{} {} jedzie prosto. Wrrrr!".format(self.brand, self.model)

    def turnTheCounter(self,):
        print("Stan licznika: {}".format(self.mileage))
        newMileage = int(input("Podaj nowy stan licznika: "))
        self.mileage = newMileage
        return "Stan licznika {} {} wynosi: {}".format(self.brand, self.model, self.mileage)

    def basicInfo(self):
        return"""
        Marka: {}
        Model: {}
        Typ nadwozia: {}
        Kolor: {}
        Przebieg: {}
        Cena: {}""""".format(self.brand, self.model, self.body, self.color, self.mileage, self.price)
    def changeColor(self, newColor):
        return "Psssss. Zmieniono kolor z {} na {}".format(self.color, newColor)

    def sellCar(self):
        return "Wystawiono samochód {} {} w serwsie motoryzacyjnym za cenę : {}".format(self.brand, self.model, self.price)



OpelAstra = Car("Opelek", "Astra", 300000, "koperkowy róż", "7000zł", "hatchback")
AudiA3 = Car("Audi", "A3", 190000, "czarny", "25000zł", "hetchback")
Ferrari = Car("Ferrari", "812 Superfast", 0, "czerwony", "1300000zł", "Coupe")
Maluch = Car("Fiat", "126", 500000, "zielony", "bezcenny", "w sumie nie wiem" )
Passeratti = Car("Volkswagen", "Passeratti", 600000, "błękitny", "7000zł", "kombi")

print(Passeratti.turnTheCounter())
print(OpelAstra.driveStraight())
print(AudiA3.basicInfo())
print(Maluch.changeColor("czerwony"))
print(Ferrari.sellCar())
