#dokończyć bo nie działą :c

import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return (f"{self.rank} {self.suit}")

class Deck:
    def __init__(self, deckOfCards):
        self.deckOfCards = deckOfCards
# O wiele wygodniej jest uznać waleta, królową, króla i Asa jako 11,12,13 i 14, w prawdziwiej gierce te karty reprezentował by obraz
    def BuildDeck(self):
        for rank in [2,3,4,5,6,7,8,9,10,11,12,13,14]:
            for suit in ["Kier", "Karo", "Pik", "Trefl"]:
                card = Card(rank, suit)
                self.deckOfCards.append(card)
        return self.deckOfCards

    def ShuffleCards(self):
        random.shuffle(self.deckOfCards)
        return self.deckOfCards

    def SortCards(self):
        self.deckOfCards.sort(key=lambda Card: Card.rank)
        print(self.deckOfCards)

    def AddCardToDeck(self):
        print("Doaj nową kartę: ")
        rank = int(input("Podaj wartość [2 - 14]: "))
        if (rank >= 2 and rank <= 14):
            suit = input("Podaj kolor [Kier, Karo, Pik, Trefl]") #chyba mówiło się kolor nwm xD
            if (suit.upper() == "KIER" or suit.upper() == "KARO" or suit.upper() == "PIK" or suit.upper() == "TREFL"):
                newCard = Card(rank, suit)
                self.deckOfCards.append(newCard)
                print("Dodano kartę!")
            else:
                print("Nie ma takiego koloru WTF!")
        else:
            print("Nie ma takiej wartości WTF!")
        print(self.deckOfCards)

    def RemoveFromDeck(self):
        print("Usuń kartę: ")
        rank = int(input("Podaj wartość [2 - 14]: "))
        suit = input("Podaj kolor [Kier, Karo, Pik, Trefl]: ")
        lookingForThisCard = Card(rank, suit)
        for card in self.deckOfCards:
            if (lookingForThisCard.rank == card.rank) and (lookingForThisCard.suit == card.suit):
                self.deckOfCards.remove(card)
                print("Usunięto kartę! ")
                print(self.deckOfCards)
            else:
                continue

    def ShowDeck(self):
        print(self.deckOfCards)

class BiggerLowerGame(Deck):

    def __init__(self, deckOfCards,):
        super().__init__(deckOfCards)
        self.score = 0

    def CardFromDeckRandomizer(self):
        rank = random.choice([2,3,4,5,6,7,8,9,10,11,12,13,14])
        suit = random.choice(["Kier", "Karo", "Pik", "Trefl"])
        randomCard = Card(rank, suit)
        return randomCard

    def MyCardRandomizer(self):
        rank = random.choice([2,3,4,5,6,7,8,9,10,11,12,13,14])
        suit = random.choice(["Kier", "Karo", "Pik", "Trefl"])
        myCard = Card(rank, suit)
        return myCard

    def Game(self):
        print("Witaj w grze karcianej: WIĘKSZY / mniejszy")
        myCard = BiggerLowerGame.MyCardRandomizer(self)
        randomCard = BiggerLowerGame.CardFromDeckRandomizer(self)
        print(randomCard)
        while True:
            print(f"Twój obecny wynik wynosi:{self.score} ")
            print(f"Twoja obecna karta to: {myCard}")
            print("WIEKSZA czy MNIEJSZA ?")
            answer = input()
            if answer.upper() == "W" and myCard.rank > randomCard.rank:
                print("Prawda!")
            if answer.upper() == "W" and myCard < randomCard.rank:
                print("Fałsz!")
            if answer.upper() == "L" and myCard < randomCard.rank:
                print("Prawda!")
            if answer.upper() == "L" and myCard > randomCard.rank:
                print("Fałsz!")




biggerLowerGame = BiggerLowerGame([])
biggerLowerGame.Game()









