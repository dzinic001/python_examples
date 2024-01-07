def power(base, exponent):
    return 1 if exponent == 0 else base * power(base, exponent - 1)

# Beispielaufruf
result = power(2, 3)
print(result)