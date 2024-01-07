def average(lst):
    return sum(lst) / len(lst) if len(lst) > 0 else 0

# Beispielaufruf
result = average([2, 4, 6, 8, 10])
print(result)