class Beer:
    def __init__(self, name, category, percent_of_alcochol, price, opinion, grade):
        self.name = name
        self.category = category
        self.percent_of_alcochol = percent_of_alcochol
        self.price = price
        self.opinion = opinion
        self.grade = grade

    def __repr__(self):
        return repr((self.name, self.category, self.percent_of_alcochol, self.price, self.opinion, self.grade))

class LiquorStore:
    def __init__(self):
        self.fridge = []

    def AddToFridge(self):
        print("Podaj dane piwa które chcesz dodać do lodówki: ")
        name = input("Nazwa: ")
        category = input("Kategoria: ")
        percent_of_alcochol = input("Stężenie alkocholowe: ")
        price = input("Cena: ")
        opinion = input("Twoja opinia: ")
        grade = int(input("Ilość gwiazdek [1 - 5]"))

        newBeer = Beer(name, category, percent_of_alcochol, price, opinion, grade)

        self.fridge.append(newBeer)
        print("Dodano nowe piwo do lodówki!")

    def GradeSort(self):
        print("Lista posortowana według oceny: ")
        self.fridge.sort(key=lambda Beer: Beer.grade)
        for obj in self.fridge:
            print(obj)

    def NameSort(self):
        print("Lista posortowana według nazwy: ")
        self.fridge.sort(key=lambda Beer: Beer.name)
        for obj in self.fridge:
            print(obj)


SklepZWinemUAni = LiquorStore()
SklepZWinemUAni.AddToFridge()
SklepZWinemUAni.AddToFridge()
SklepZWinemUAni.AddToFridge()
SklepZWinemUAni.GradeSort()
SklepZWinemUAni.NameSort()





