def divisors(number):
    """
    Return a list of positive divisors for the given number.

    Parameters:
    - number (int): The input positive integer.

    Returns:
    list: List of positive divisors.
    """
    divisors_list = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors_list.append(i)
    return divisors_list
