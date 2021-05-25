
kod = input("Podaj kod pocztowy w oznaczeniu międzynarodowym: ")

def Add(kod, file):
     file.write(kod)
     file.close()

try:
    file = open('kodPocztowy.txt', 'w')
    if kod[0] == "P":
        if kod[1] == "L":
            Add(kod, file)
except FileNotFoundError:
    print("to nie jesy kod pocztowy Polski")




