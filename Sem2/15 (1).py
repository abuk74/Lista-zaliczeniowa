class Hotel:

    def __init__(self, name):
        self.name = name

    def BuildHotel(self):
        print(f"Rozpoczynamy pracę nad budową hotelu {self.name}")

class Floor:
    def __init__(self, ):


class Room:
    def __init__(self, floor, roomNumber, isRented):
        self.floor = floor
        self.roomNumber = roomNumber
        self.isRented = isRented
