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



class Room:
    def __init__(self, floor, roomNumber, beds, empty):
        self.floor = floor
        self.roomNumber = roomNumber
        self.beds = beds
        self.empty = empty
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




barak = Hotel("Barak")
