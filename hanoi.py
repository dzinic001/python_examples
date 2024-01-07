def hanoi(n, source, target, auxiliary):
    """
    Die Funktion löst das Problem der Türme von Hanoi für n Scheiben.

    Parameters:
        n (int): Die Anzahl der Scheiben.
        source (str): Der Ausgangsstapel (z.B. 'A').
        target (str): Der Zielstapel (z.B. 'B').
        auxiliary (str): Der Hilfsstapel (z.B. 'C').

    Returns:
        None
    """
    if n > 0:
        # Bewege (n-1) Scheiben vom Ausgangsstapel auf den Hilfsstapel
        hanoi(n-1, source, auxiliary, target)

        # Bewege die größte Scheibe vom Ausgangsstapel zum Zielstapel
        print(f"Move disk {n} from {source} to {target}")

        # Bewege die (n-1) Scheiben vom Hilfsstapel zum Zielstapel
        hanoi(n-1, auxiliary, target, source)

if __name__ == "__main__":
    hanoi(3, 'A', 'C', 'B')