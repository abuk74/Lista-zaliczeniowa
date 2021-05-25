import time

class Citizen:
    def __init__(self, name, surname, street, houseNum, postcode, town):
        self.name = name
        self.surname = surname
        self. street = street
        self.houseNum = houseNum
        self.postcode = postcode
        self.town = town

    def businessCard(self):

        print("Drukowanie wizytówki, proszę czekać...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("...")
        time.sleep(1)
        print("zzzzzip")

        print("..............................")
        print(f"{self.name}  {self.surname}")
        line2 = f"{self.name} {self.surname}"
        print("ul.", self.street, " ", self.houseNum)
        line3 = f"ul.{self.street}  {self.houseNum}"
        print(self.postcode, " ", self.town)
        line4 = f"{self.postcode}  {self.town}"
        print("..............................")

        text = open("businesCard.txt", "w")
        text.write("..............................\n")
        text.write(f"{line2}\n")
        text.write(f"{line3}\n")
        text.write(f"{line4}\n")
        text.write("..............................\n")

PatkaSzmatka = Citizen("Patka", "Szmatka", "Betonowa", "69", "69-420", "Gdzieś na podlasiu")
print(PatkaSzmatka.businessCard())