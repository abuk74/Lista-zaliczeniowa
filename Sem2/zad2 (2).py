import time
class Hotel:
    numberOfRooms = 0
    numberOfFloors = 0
    floors = []
    def __init__(self, name):
        self.name = name
        self.CreateHotel()
    def CreateHotel(self):
        print("Witamy w kreatorze tworzenia hotelu!")
        time.sleep(1)
        print("Tworzysz Hotel: ", self.name)
        time.sleep(1)
        numberOfFloors = int(input("Podaj liczbę pięter: "))
        self.numberOfFloors = numberOfFloors
        for i in range(numberOfFloors):
            newFloor = Floor(i)
            self.floors.append(newFloor)
            self.numberOfRooms += newFloor.numberOfRooms
        print("Kreator zakończył prace")
    def AvailableRooms(self):
        availableRooms = 0
        for i in range(0, self.numberOfFloors):
            for j in range(0, len(self.floors[i].rooms)):
                if self.floors[i].rooms[j].empty == True:
                    print(f"Na piętrze {i} jest wolny pokój {j}")
                    availableRooms += 1
        print(f"Jest {availableRooms} wolnych pokoi")
    def Rent(self, floor, roomNumber, person):
        self.floors[floor].rooms[roomNumber].empty = False
        self.floors[floor].rooms[roomNumber].rentedBy = person
        print(f"Wynajęto pokój {roomNumber} na piętrze {floor} osobie: {person.name} {person.surname}")
    def __del__(self):
        print("Wywołanie destruktora!")

class Room:
    def __init__(self, floor, roomNumber, beds, empty):
        self.floor = floor
        self.roomNumber = roomNumber
        self.beds = beds
        self.empty = empty
        self.rentedBy = Person

class Floor:
    def __init__(self, floor):
        self.floor = floor
        self.numberOfRooms = 0
        self.rooms = []
        self.Create(self.floor)
    def Create(self, floor):
        while True:
                option = int(input(f"Czy chcesz dodać pokój na piętrze: {floor} ? 1 - tak 2 - nie"))
                if option == 1:
                    self.CreateRoom(floor, self.numberOfRooms)
                else:
                    break
    def CreateRoom(self, floor, roomNumber):
        print("Tworzę pokój: ", roomNumber, "na piętrze: ", floor)
        beds = int(input("Podaj liczbę łóżek: "))
        newRoom = Room(floor, roomNumber, beds, True)
        self.numberOfRooms += 1
        self.rooms.append(newRoom)

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname


barak = Hotel("Barak")
barak.AvailableRooms()
kowalski = Person("Jan", "Kowalski")
barak.Rent(0, 0, kowalski)