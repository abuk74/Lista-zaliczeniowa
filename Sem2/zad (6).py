try:
    first_file = open("firstFile.txt", "r")
except Exception:
    userFirstFile = input("Nie podano nazwy pliku! Podaj nazwę pliku, bez rozszerzenia: ")
    first_file = open(f"{userFirstFile}.txt", "r")

try:
    second_file = open("secondFile.txt", "r")
except Exception:
    userSecondtFile = input("Nie podano nazwy pliku! Podaj nazwę pliku, bez rozszerzenia: ")
    second_file = open(f"{userSecondtFile}.txt", "r")


plik = open("plik.txt", "w+")

for line in range(0, 3):
    plik.write(f"{first_file.readline()}\n")
    plik.write(f"{second_file.readline()}\n")




