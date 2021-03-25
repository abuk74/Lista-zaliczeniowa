#ZAD1
'''
class Car:
    def __init__(self, brand, age, color, capacity, fuelType):
        self.brand = brand
        self.age = age
        self.color = color
        self.capacity = capacity
        self.fuelType = fuelType
    def Refueling(self):
        print("Zatankowano: {} {} litrów ".format(self.fuelType, self.capacity))
    def CarInfo(self):
        print("Marka:", self.brand)
        print("Wiek:", self.age)
        print("Kolor:", self.color)
        print("Pojemność baku:", self.capacity)
        print("Rodzaj paliwa:", self.fuelType)
    def ChangeColor(self, newColor):
        print("Zmieniono kolor z {} na {}".format(self.color, newColor))
    def Velocity(self):
        if(self.color == "red"):
            print("Bardzo szybki")
        else:
            print("Nie tak szybki jak czerwony")
    def CallService(self):
        print("Jesteś 10 w kolejce")

opelek = Car("Opel", 10, "Silver", 50, "diesel")

opelek.Refueling()
opelek.ChangeColor("blue")
opelek.CarInfo()
opelek.Velocity()
opelek.CallService()
'''

#ZAD 2

class Book:
    def __init__(self, author, title, frame, pages, exampleText):
        self.title = title
        self.author = author
        self.frame = frame
        self.pages = pages
        self.exampleText = exampleText

    def SayMyName(self):
        print(self.author)
        print(self.title)
        print(self.frame)
        print(self.pages)
        print(self.exampleText)
nowaKsiazka = Book("Sapkowski Andrzej", "Wiedźmin - ostatnie rozszczenie", "hard", 300, "jakiś tekst")
books = []
def Main():
    books.append(nowaKsiazka)
    print("Witaj!")
    AnalizeChoice()
    while True:
        choice = input("Czy chcesz wykonać jeszcze jakąś operację? Tak / Nie")
        if choice == "Tak":
            AnalizeChoice()
        else:
            break
def AnalizeChoice():
    choice = input("Czy chcesz dodać nową książke, wyświetlić listę obecnie istniejących książek lub usunąć jedną z nich? wybierz 1, 2 lub 3")
    if (choice == "1"):
        AddBook()
    elif (choice == "2"):
        ShowBooks()
    else:
        RemoveBook()
def AddBook():
    author = input("Podaj autora: Nazwisko Imie")
    title = input("Podaj tytuł")
    frame = input("Podaj rodzaj oprawy")
    pages = int(input("Podaj ilość stron"))
    exampleText = input("Podaj przykładowy fragment tekstu")
    book = Book(author, title, frame, pages, exampleText)
    print("Dodano nową książke!")
    books.append(book)

def ShowBooks():
    books.sort(key=SortKey)
    for i in books:
        i.SayMyName()
def SortKey(obj):
    return obj.author
def RemoveBook():
    choice = int(input("podaj indeks książki: "))
    yesOrNot = input("Czy na pewno chcesz usunąć książke: {} tej operacji nie będzie można cofnąć! Tak/Nie".format(choice))
    if yesOrNot == "Tak":
        books.pop(choice)
        ShowBooks()
Main()
'''
class Main:
    def __init__(self):
        self.books = books[]
    def CreateNewBook(self):
        self.books.append(Book(string author,))
'''
