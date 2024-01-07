def filter_by_first_letter(strings, letter):
    """
    Return a list of strings starting with the given letter.

    Parameters:
    - strings (list): List of strings.
    - letter (str): Single character to filter strings.

    Returns:
    list: List of strings starting with the given letter.
    """
    filtered_strings = []
    for s in strings:
        if s.startswith(letter):
            filtered_strings.append(s)
    return filtered_strings
