import heapq
from timeit import default_timer as timer

#sortowanie szybkie

start = timer()

sort = [18, 1, 123, 345534, 13, 5, 345, 54, 31, 8]
print("Lista wejściowa to:")
print(sort)
sort.sort()
print(sort)

end = timer()
resoult = end - start
print(resoult)

#Heap
start = timer()
sort = [18, 1, 123, 345534, 13, 5, 345, 54, 31, 8]
heapq.heapify(sort)
print(sort)

end = timer()
resoult = end - start
print(resoult)
