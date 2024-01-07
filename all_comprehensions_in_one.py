# comprehensions.py

def divisors(number):
    """Return a list of positive divisors for the given number.


    >>> divisors(6)
    [1, 2, 3, 6]
    >>> divisors(12)
    [1, 2, 3, 4, 6, 12]
    """
    return [i for i in range(1, number + 1) if number % i == 0]

def filter_by_first_letter(strings, letter):
    """Return a list of strings starting with the given letter.


    >>> filter_by_first_letter(['apple', 'banana', 'cherry'], 'b')
    ['banana']
    >>> filter_by_first_letter(['apple', 'banana', 'cherry'], 'a')
    ['apple']
    
    """
    return [s for s in strings if s.startswith(letter)]

def primes(number):
    """Return a list of prime numbers smaller than or equal to the given number.

    
    >>> primes(10)
    [2, 3, 5, 7]
    >>> primes(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    return [i for i in range(2, number + 1) if all(i % j != 0 for j in range(2, int(i**0.5) + 1))]

def roll_n_times(n):
    """Return a list of n random integers between 1 and 6.
    
    
    >>> result = roll_n_times(3)
    >>> all(1 <= value <= 6 for value in result)
    True
    """
    import random
    return [random.randint(1, 6) for _ in range(n)]
