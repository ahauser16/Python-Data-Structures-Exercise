# Pros: This function uses dictionary comprehension and the union operator to create a dictionary from keys and values. It's efficient and idiomatic Python.
# Cons: It requires Python 3.9 or later to use the dictionary union operator. It's also more complex than the other functions due to the use of two dictionary comprehensions and the union operator.
def two_list_dictionary1(keys, values):
    """Given keys and values, make dictionary of those.

    >>> two_list_dictionary1(['x', 'y', 'z'], [9, 8, 7])
    {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

    >>> two_list_dictionary1(['a', 'b', 'c', 'd'], [1, 2, 3])
    {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

    >>> two_list_dictionary1(['a', 'b', 'c'], [1, 2, 3, 4])
    {'a': 1, 'b': 2, 'c': 3}
    """
    return {k: v for k, v in zip(keys, values)} | {k: None for k in keys[len(values) :]}


# Pros: This function uses the zip function and the dict function to create a dictionary from keys and values. It's straightforward and easy to understand.
# Cons: It creates a new list with values + [None] * (len(keys) - len(values)), which can be inefficient for large inputs.
def two_list_dictionary2(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary2(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary2(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary2(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
    """
    return dict(zip(keys, values + [None] * (len(keys) - len(values))))


# Pros: This function uses the zip_longest function from the itertools module to create a dictionary from keys and values. This function fills in None for missing values, which makes it very convenient for this use case.
# Cons: It requires importing the itertools module to use the zip_longest function. It's also slightly more complex than the second function due to the use of zip_longest.
# NB--> The zip_longest function from the itertools module pairs extra values with None when there are fewer keys than values. To reflect this behavior in the docstring, you can modify the docstring as follows:
# >>> two_list_dictionary3(['a', 'b', 'c'], [1, 2, 3, 4])
#        {'a': 1, 'b': 2, 'c': 3, None: 4}

from itertools import zip_longest


def two_list_dictionary3(keys, values):
    """Given keys and values, make dictionary of those.

        >>> two_list_dictionary3(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}

    If there are fewer values than keys, remaining keys should have value
    of None:

        >>> two_list_dictionary3(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}

    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary3(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3, None: 4}
    """
    return dict(zip_longest(keys, values))
