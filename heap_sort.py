import heapq

def heapsort(arr):
    heap = []
    for element in arr:
        heapq.heappush(heap, element)

    ordered = []
    while heap:
        ordered.append(heapq.heappop(heap))

    return ordered

# Beispielaufruf
my_list = [64, 34, 25, 12, 22, 11, 90]
result = heapsort(my_list)
print(result)
