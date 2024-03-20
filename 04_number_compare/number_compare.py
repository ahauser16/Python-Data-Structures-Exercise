#This is the most straightforward and intuitive way to implement this function. It's easy to understand and efficient, as it only requires a maximum of two comparisons. This method is the best choice for most situations.
def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

    >>> number_compare(1, 1)
    'Numbers are equal'

    >>> number_compare(-1, 1)
    'Second is greater'

    >>> number_compare(1, -2)
    'First is greater'
    """
    if a > b:
        return "First is greater"
    elif a < b:
        return "Second is greater"
    else:
        return "Numbers are equal"


# Using a dictionary to map conditions to return values:
# This method uses a dictionary to map the conditions a > b and a < b to their respective return values. If neither condition is True, it defaults to 'Numbers are equal'. This method is less intuitive than the first one, but it can be more efficient if there are many conditions, as it only requires one lookup in the dictionary.
def number_compare2(a, b):
    """Report on whether a>b, b>a, or b==a

    >>> number_compare2(1, 1)
    'Numbers are equal'

    >>> number_compare2(-1, 1)
    'Second is greater'

    >>> number_compare2(1, -2)
    'First is greater'
    """
    return {a > b: "First is greater", a < b: "Second is greater"}.get(
        True, "Numbers are equal"
    )


# Using a list of tuples and a loop to check each condition:
# This method uses a list of tuples, where each tuple contains a condition and its corresponding return value. It then uses a loop to check each condition in order. If a condition is True, it returns the corresponding result. If no condition is True, it returns 'Numbers are equal'. This method is less efficient than the first two, as it requires iterating through the list, but it can be useful if the conditions and return values are dynamic or need to be calculated at runtime.
def number_compare3(a, b):
    """Report on whether a>b, b>a, or b==a

    >>> number_compare3(1, 1)
    'Numbers are equal'

    >>> number_compare3(-1, 1)
    'Second is greater'

    >>> number_compare3(1, -2)
    'First is greater'
    """
    conditions = [(a > b, 'First is greater'), (a < b, 'Second is greater')]
    for condition, result in conditions:
        if condition:
            return result
    return 'Numbers are equal'




