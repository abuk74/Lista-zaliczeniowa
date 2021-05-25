
'''
class Human:
    def __init__(self, type, skin):
        self.type = type
        self.skin = skin
class Osoba:
    def __init__(self, name, surname, type, skin):
        super().__init__(type, skin)
        self.__name = name
        self.__surname = surname


class Druzyna:
    def __init__(self, clubName, trener):
        self.clubName = clubName
        self.trener = trener

    def ShowCase(self):
        return repr(self.clubName + self.trener)
    def ShowCase2(self):
        return str(self.clubName + self.trener)
class Zawodnicy(Druzyna):
    def __init__(self, name, surname, id, clubName, trener):
        super().__init__(clubName, trener)
        self.name = name
        self.surname = surname
        self.id = id
    def StrzelGol(self):
        print(f"Zawodnik {self.name} {self.surname} strzela gola dla drużyny {self.clubName}")
    def ObronBramke(self):
        print(f"Zawodnik {self.name} {self.surname} obronił bramkę")


'''



class Hotel:
    rooms = []
    floors = []
    def __init__(self, name, numberOfRooms, numberOfFloors):
        self.name = name
        self.numberOfRooms = numberOfRooms
        self.numberOfFloors = numberOfFloors
    def ShowAllRooms(self):
        for i in range(0, len(self.rooms)):
            print(self.rooms[i].number)
    def Create(self):
        fun = input("Co chcesz zrobić? 1- dodać pokój, 2 - dodać piętro")
        if fun == 1:
            newRoom = Room(self.numberOfRooms, True)
            self.rooms.append(newRoom)
        else:
            newFloor = Floor(self.numberOfFloors)
            self.rooms.append(newFloor)
class Motel(Hotel):
    rooms = []
    floors = []
    def __init__(self, name, numberOfRooms, numberOfFloors):
        super().__init__(name, numberOfRooms, numberOfFloors)

class Room:
    pass
class Floor:
    pass
