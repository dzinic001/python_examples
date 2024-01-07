def roll_n_times(n):
    """
    Return a list of n random integers between 1 and 6.

    Parameters:
    - n (int): Number of random integers to generate.

    Returns:
    list: List of n random integers.
    """
    import random
    random_integers = []
    for _ in range(n):
        random_integers.append(random.randint(1, 6))
    return random_integers
