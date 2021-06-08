import heapq
from timeit import default_timer as timer
list = [4, 10, 11, 5, 73, 5, 1]
print(f"Początkowy ciąg liczb: {list}")

def numbersFromFile():
    with open(r"C:\Users\Mateusz Jarosiński\PycharmProjects\pythonProject\PodstawyProgramowaniaDSW\Semestr II\Labolatorium#18\numbers_for_4.txt") as textFile:
        for line in textFile:
            strings = line.split()

    for i in range(0, len(strings)):
        strings[i] = int(strings[i])

    return strings

def HeapSort(list):
    heapTime1 = timer()
    print("Heap sort:")
    heapq.heapify(list)
    print(list)
    heapTime2 = timer()
    print("Wykonanie tego sortowania zajęło: ", heapTime2 - heapTime1)

def Quicksort(list):
    quickTime1 = timer()
    print("Quicksort:")
    list.sort()
    print(list)
    quickTime2 = timer()
    print("Wykonanie tego sortowania zajęło: ", quickTime2 - quickTime1)

print(HeapSort(list))
print(Quicksort(list))
print(HeapSort(numbersFromFile()))
print(Quicksort(numbersFromFile()))