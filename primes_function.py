def primes(number):
    """
    Return a list of prime numbers smaller than or equal to the given number.

    Parameters:
    - number (int): The input positive integer.

    Returns:
    list: List of prime numbers.
    """
    primes_list = []
    for i in range(2, number + 1):
        is_prime = all(i % j != 0 for j in range(2, int(i**0.5) + 1))
        if is_prime:
            primes_list.append(i)
    return primes_list
