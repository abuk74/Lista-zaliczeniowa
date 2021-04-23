class Student():
    def __init__(self, name, surname, age, faculty, percentOfAlcohol):
        self.name = name
        self.surname = surname
        self.age = age
        self.faculty = faculty
        self.percentOfAlcohol = percentOfAlcohol
    def DrinkBeer(self, beer):
        if self.percentOfAlcohol <= 0:
            print("A walne se browarka")
            self.percentOfAlcohol += beer.vol
        elif self.percentOfAlcohol >= 2:
            print("Student buja się jak pan JM na wykladzie w rytm 'złotych przeboji'")
            self.percentOfAlcohol += 4 * beer.vol
        else:
            print("Student na kacusiu śpi na wykładzie. Procedura trzeźwienia - czym się strułeś tym się lecz")
            self.percentOfAlcohol -= 0.5 * beer.vol

class Beer():
    def __init__(self, name, vol):
        self.name = name
        self.vol = vol


janKowalski = Student("Jan", "Kowalski", 20, "Informatyka", 0)
tyskie = Beer("Tyskie", 4)
janKowalski.DrinkBeer(tyskie)
