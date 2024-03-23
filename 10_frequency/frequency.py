# Pros: This function is straightforward and easy to understand. It uses Python's built-in list method count to count the occurrences of search_term in lst. Cons: The count method traverses the entire list, which can be inefficient for large lists if the search_term is found early.


def frequency(lst, search_term):
    """Return frequency of term in lst.

    >>> frequency([1, 4, 3, 4, 4], 4)
    3

    >>> frequency([1, 4, 3], 7)
    0
    """
    return lst.count(search_term)


# Pros: This function uses a manual approach to count the occurrences, which allows for more control and potential optimizations. Cons: It's slightly more complex than the first function and may be slower for large lists due to the overhead of the loop and conditional statement.
def frequency2(lst, search_term):
    """Return frequency of term in lst.

    >>> frequency2([1, 4, 3, 4, 4], 4)
    3

    >>> frequency2([1, 4, 3], 7)
    0
    """
    count = 0
    for item in lst:
        if item == search_term:
            count += 1
    return count


# Pros: This function uses the Counter class from the collections module, which provides a high-level, efficient way to count elements in a list. Cons: It's more complex than the other two functions and may be harder to understand for someone not familiar with the Counter class. It also counts all elements in the list, which can be inefficient if the list is large and the search_term is rare.
from collections import Counter


def frequency3(lst, search_term):
    """Return frequency of term in lst.

    >>> frequency3([1, 4, 3, 4, 4], 4)
    3

    >>> frequency3([1, 4, 3], 7)
    0
    """
    return Counter(lst)[search_term]
