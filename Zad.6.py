
def Main():

    inDef = str(input("Wybierz jednostke wejściową: C - Celsjusz, K - Kelwin, F - Fahrenheit, R - Rankine"))
    outDef = str(input("Wybierz jednostke wyjściową: C - Celsjusz, K - Kelwin, F - Fahrenheit, R - Rankine"))
    if inDef == outDef:
        print("serio?")
        return
    namesOfDef = [inDef, outDef]
    value = int(input("podaj wartość temperatury"))

    if namesOfDef[0] == "K":
        if value < 0:
            print("Nie ma skali ujemnej dla stopni Kelwina!")
            return
        newValue = Kelwin(value, namesOfDef)
    elif namesOfDef[0] == "F":
        newValue = Fahrenheit(value, namesOfDef)
    elif namesOfDef[0] == "R":
        newValue = Rankine(value, namesOfDef)
    else:
        newValue = Celsjusz(value, namesOfDef)
    print(newValue)
    if newValue <= 0 and outDef == "C":
        print("woda zamarza")
    elif newValue <= 273 and outDef == "K":
        print("woda zamarza")
    elif newValue <= 32 and outDef == "F":
        print("woda zamarza")
    elif newValue <= 491.67 and outDef == "R":
        print("woda zamarza")
    else:
        print("woda w stanie ciekłym")

def Kelwin(value, namesOfDef):
    if namesOfDef[1] == "C":
        return(value - 273)
    elif namesOfDef[1] == "R":
        return(value * 9 / 5)
    else:
        return(value - 255)


def Fahrenheit(value, namesOfDef):
    if namesOfDef[1] == "C":
        return(value - 32)
    elif namesOfDef[1] == "R":
        return(value + 459.67)
    else:
        return(value + 255)



def Celsjusz(value, namesOfDef):
    if namesOfDef[1] == "K":
        return(value + 273)
    elif namesOfDef[1] == "R":
        return((value + 273)* 9/5)
    else:
        return(value + 32)



def Rankine(value, namesOfDef):
    if namesOfDef[1] == "K":
        return(value * 5 / 9)
    elif namesOfDef[1] == "F":
        return(value / 459.67)
    else:
        return(value * 5 / 9 - 273)



Main()
