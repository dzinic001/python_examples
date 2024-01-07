def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
# Beispielaufruf
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = binary_search(my_list, 5)
print(result)
