# ackermann ist so ein typischers rekursion problem bekannt für die wachstumsrate

""" 
def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

# Beispielaufruf
result = ackermann(3, 4) --sobald höher stürzt es ab wegen wachstumsrate
print(result)

lösung wäre itterativ
"""

import sys

# Setzen der maximalen Rekursionstiefe
sys.setrecursionlimit(3000)


