class Student:
    def __init__(self, name, surname, age, energy, percentOfAlcochol,):
        self.name = name
        self.surname = surname
        self.age = age
        self.energy = energy
        self.percentOfAlcochol = percentOfAlcochol

    def DrinkCoffe(self, coffe):
        if self.energy < 50:
            print(f"{self.name} potrzebuje kawy, a nawet dwie!")
            self.energy += coffe.energy
            print(f"Wypito pierwszą kawę: {coffe.type}")
            self.energy += coffe.energy
            print("Wypito drugą kawę, student jest pełen życia!")
        elif self.energy < 80:
            print(f"{self.name} zaczyna tracić energię, warto wypić kawę")
            self.energy += coffe.energy
            print(f"Wypito jedną kawę: {coffe.type}")
        else:
            print("Student ma wystarczającą ilośc energii!")

    def DrinkBeerBro(self, beer):
        if self.percentOfAlcochol <= 0:
            print(f"O nie, {self.name} jest trzeźwy! Koniecznie wypij piwo!")
            while self.percentOfAlcochol <= 10:
                print("Walnę sobie piwko")
                self.percentOfAlcochol += beer.voltage
            print("Studentem miota jak szatan")
            choice = input("Czy chcesz wypić jeszcze ?")
            if choice.upper() == "TAK":
                while self.percentOfAlcochol <= 20:
                    print(f"Jeszcze jedno {beer.name}")
                    self.percentOfAlcochol += beer.voltage
                print("Student odpłynął...")


class Coffe:
    def __init__(self, type, energy):
        self.type = type
        self.energy = energy

class Beer:
    def __init__(self, name, voltage):
        self.name = name
        self.voltage = voltage

mateuszKapelusz = Student("Mateusz", "Kapelusz", 20, 0, 0)
doubleEspresso = Coffe("Double Espressp", 50)
mocnyFull = Beer("Mocny Full", 7)

mateuszKapelusz.DrinkBeerBro(mocnyFull)
