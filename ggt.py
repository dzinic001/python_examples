#größter gemeinsamer teiler

def gct(a, b):
    return a if b == 0 else gct(b, a % b)

# Beispielaufruf
result = gct(48, 18)
print(result)