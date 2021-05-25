import time


class SmartPhone:
    def __init__(self, brand, model, memory, system, camera, batteryCondition, phoneNumber, ):
        self.brand = brand
        self.model = model
        self.memory = memory
        self.system = system
        self.camera = camera
        self.batteryCondition = batteryCondition
        self.phoneNumber = phoneNumber

    def IsCharged(self):
        if self.batteryCondition == 100:
            print("W pełni naładowany!")
        elif self.batteryCondition >= 80:
            print("W granicach tolarancji")
        elif self.batteryCondition < 80:
            print("Mniej niż 80%, uważaj!")
        else:
            print("System down...")

    def BasicInfo(self):
        print(self.brand, self.model)

    def QuickCharge(self, batteryCondition):
        print("Ładowanie baterii: ")
        while batteryCondition != 100:
            batteryCondition += 1
            time.sleep(1)
            print(batteryCondition)

            self.batteryCondition = batteryCondition

        print("Bateria naładowana!")

    def AddMemory(self):
        print(f"Pamięć wbydowana w urządzenie: {self.memory} ")
        addMemory = int(input("Podaj ile GB posiada twoja karta SD: "))
        if self.brand.upper() == "IPHONE":
            print("Brak możliwości rozszerzenia pamięci :c")
        else:
            newMemory = self.memory + addMemory
            self.memory = newMemory
            print(f"Łączna pamięć wynosi: {self.memory} GB")

SamsungS21 = SmartPhone("Samsung", "S21", 256 , "Android", "108MPX", 69, "123456789")
IP8 = SmartPhone("Iphone", "8", 64, "IOS", "12MPX", 100, "696420666")
print(IP8.IsCharged())
print(IP8.BasicInfo())
print(IP8.QuickCharge(90))
print(IP8.AddMemory())
print(SamsungS21.AddMemory())

