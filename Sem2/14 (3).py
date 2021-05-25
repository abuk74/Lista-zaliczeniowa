class Vechicle:
    def __init__(self, plate, number_of_seats, lacquier_color, max_speed):
        self.plate = plate
        self.number_of_seats = number_of_seats
        self.lacquier_color = lacquier_color
        self.max_speed = max_speed

class Car(Vechicle):
    def __init__(self, plate, number_of_seats, lacquier_color, max_speed, fuel, horsepower, body_type):
        super().__init__(plate, number_of_seats, lacquier_color, max_speed)
        self.fuel = fuel
        self.horsepower = horsepower
        self.body_type = body_type

    def changeColor(self, new_color):
        old_color = self.lacquier_color
        self.lacquier_color = new_color
        print(f"Psss, zmieniono kolor lakieru z {old_color} na {self.lacquier_color}")

    def __del__(self):
        print("Obekt usunięty")

class Motorcycle(Vechicle):
    def __init__(self, plate, number_of_seats, lacquier_color, max_speed, type, ):
        super().__init__(plate, number_of_seats, lacquier_color, max_speed)
        self.type = type

    def Accelerate(self, initialSpeed):
        if initialSpeed <= self.max_speed:
            print(f"Poruszasz sięz prędkością {initialSpeed} km/h")
            plusSpeed = int(input("O ile chcesz przyszpieszyć [km/h] ?"))
            initialSpeed += plusSpeed
            while initialSpeed <= self.max_speed:
                print(f"Poruszasz sięz prędkością {initialSpeed} km/h")
                answer = input("Chcesz przyspieszyć więcej? ")
                if answer.upper() == "TAK":
                    answer = int(input("O ile chcesz przyszpieszyć [km/h] ?"))
                    initialSpeed += answer
                else:
                    break
        else:
            print("Nie możesz poruszać się tak szybko")

    def __del__(self):
        print("Obiekt usunięty")

pastuch = Car("DOL 123456", "5", "szybki czerwony", "200 km/h", "deasel", "110KM", "kombi")

pastuch.changeColor("królewski niebieski")

kawasakiNinja = Motorcycle("DOL 654321", "2", "zielony", 300, "ścigacz czy coś" )

kawasakiNinja.Accelerate(0)


