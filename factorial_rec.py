def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)


# Beispielaufruf
result = factorial(5)
print(result)