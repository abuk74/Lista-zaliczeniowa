import random
from timeit import default_timer as timer

def QueueToStack50():
    stack = []
    queue = []
    time1 = timer()
    for number in range(0, 50):
        queue.append(random.randint(0,100))

    for numbers in queue:
        stack.insert(0, numbers)
    time2 = timer()
    total = time2 - time1

    print(f"Kopiec: {stack}")
    print(f"Kolejka: {queue}")
    print(f"Czas wykonywania algorytmu: {total}")

    return total

def QueueToStack100():
    stack = []
    queue = []
    time1 = timer()
    for number in range(0, 100):
        queue.append(random.randint(0,100))

    for numbers in queue:
        stack.insert(0, numbers)
    time2 = timer()
    total = time2 - time1

    print(f"Kopiec: {stack}")
    print(f"Kolejka: {queue}")
    print(f"Czas wykonywania algorytmu: {total}")

    return total

def QueueToStack150():
    stack = []
    queue = []
    time1 = timer()
    for number in range(0, 150):
        queue.append(random.randint(0,100))

    for numbers in queue:
        stack.insert(0, numbers)
    time2 = timer()
    total = time2 - time1

    print(f"Kopiec: {stack}")
    print(f"Kolejka: {queue}")
    print(f"Czas wykonywania algorytmu: {total}")

    return total

def TheSameButFromTxtFile():
    stack = []
    queue = []
    time1 = timer()
    with open(r"C:\Users\Mateusz Jarosiński\PycharmProjects\pythonProject\PodstawyProgramowaniaDSW\Semestr II\Labolatorium#18\numbers.txt") as f:
        for line in f:
            currentLine = line.strip().split(",")

            for elements in currentLine:
                queue.append(int(elements))

            for numbers in queue:
                stack.insert(0, numbers)

            time2 = timer()
            total = time2 - time1

            print(f"Kopiec: {stack}")
            print(f"Kolejka: {queue}")
            print(f"Czas wykonywania algorytmu: {total}")

            return total

print(QueueToStack50())
print(QueueToStack100())
print(QueueToStack150())
print(TheSameButFromTxtFile())

def TimesToTxtFile():
    time50numbers = QueueToStack50()
    time100numbers = QueueToStack100()
    time150numbers = QueueToStack150()
    timeFromTxtFile50Numbers = TheSameButFromTxtFile()

    f = open("results.txt", "w")
    f.write("Wyniki działań algorytmu: \n")
    f.write(f"50 randomowych liczb: {time50numbers}\n")
    f.write(f"100 randomowych liczb: {time100numbers}\n")
    f.write(f"150 randomowych liczb: {time150numbers}\n")
    f.write(f"50 liczb z pliku txt: {timeFromTxtFile50Numbers}")
    f.close()

TimesToTxtFile()