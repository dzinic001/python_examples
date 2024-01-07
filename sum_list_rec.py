def sum_list(lst):
    return lst[0] if len(lst) == 1 else lst[0] + sum_list(lst[1:])


# Beispielaufruf
result = sum_list([1, 2, 3, 4, 5])
print(result)