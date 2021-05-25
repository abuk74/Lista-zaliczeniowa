with open("inwokacja.txt", "r", encoding='UTF8') as readfile:
    for lines in readfile:
        print(lines.rstrip("\n"))
