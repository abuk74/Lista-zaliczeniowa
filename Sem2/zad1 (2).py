with open(r"C:\Users\Mateusz Jarosiński\PycharmProjects\pythonProject\PodstawyProgramowaniaDSW\Semestr II\Labolatorium#18\pantadeusz.txt", encoding="utf-8") as panTadeuszText:
    count = -1
    for i, line in enumerate(panTadeuszText):
        count +=1
        if i == 8 or i == 12 or i == 60 or i == 98 or i == 104:
            print(line)
            count += 1
    print("Ilość wierszy: ", count)
