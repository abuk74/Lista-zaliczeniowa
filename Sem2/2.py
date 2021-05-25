class Book:
    def __init__(self, title, author, publishingHouse, exampleText, publishmentYear):
        self.title = title
        self.author = author
        self.publishingHouse = publishingHouse
        self.exampleText = exampleText
        self.publishingYear = publishmentYear

    def __str__(self):
        return self.title

    def readBook(self):
        return self.exampleText

    def BasicInfo(self):
        print(self.title)
        print(self.author)
        print(self.publishingHouse)
        print(self.publishingYear)

class Library:

    def __init__(self):
        self.library = []

    def AddBookToLibrary(self):
        title = input("Podaj tytuł książki: ")
        author = input("Podaj autora(imię, nazwisko): ")
        publishingHouse = input("Podaj wydawnictwo: ")
        exampleText = input("Wpisz tekst: ")
        publishingYear = input("Podaj rok wydania: ")

        newBook = Book(title, author, publishingHouse, exampleText, publishingYear)

        self.library.append(newBook)

    def ShowLibrary(self):
        print("Lista książek:")
        for obj in self.library:
            print(f"{obj.author} - {obj.title}")

    def Choice(self):
        print("Chcesz wyśiwtlić listę książek czy dodać nową?")
        choice = int(input("1 = wyświetl książki , 2 = dodaj nową"))
        if choice == 1:
            self.ShowLibrary()
        if choice == 2:
            self.AddBookToLibrary()
    def Main(self):
        self.Choice()
        answer = int(input("Czy chcesz wykonać coś jeszcze? [1 = tak , 2 = nie] "))
        while True:
            if answer == 1:
                self.Choice()
            else:
                print("Do widzenia!")
                break

KsięgarniaKsiazkaIKawa = Library()
KsięgarniaKsiazkaIKawa.Main()




