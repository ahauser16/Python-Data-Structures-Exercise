# Pros: This function is straightforward and easy to understand. It uses the 'all' function and a generator expression to check if all items in 'lst' are lists. This is efficient and idiomatic Python. Cons: It iterates over lst once, which can be inefficient for large inputs.
def list_check1(lst):
    """Are all items in lst a list?

    >>> list_check1([[1], [2, 3]])
    True

    >>> list_check1([[1], "nope"])
    False
    """
    return all(isinstance(item, list) for item in lst)


# Pros: This function uses a manual approach to check if all items are lists. It stops as soon as it finds a non-list item, which can be more efficient than the first function for large lists with a non-list item near the start. Cons: It's slightly more complex than the first function due to the use of a loop and conditional statement.
def list_check2(lst):
    """Are all items in lst a list?

    >>> list_check2([[1], [2, 3]])
    True

    >>> list_check2([[1], "nope"])
    False
    """
    for item in lst:
        if not isinstance(item, list):
            return False
    return True


# Pros: This function uses list comprehension to create a new list of all list items in lst, and checks if its length is the same as the length of lst. This is a compact way to check if all items are lists. Cons: It creates a new list, which can be inefficient for large inputs. It also iterates over lst twice, once to create the new list and once to get its length.
def list_check3(lst):
    """Are all items in lst a list?

    >>> list_check3([[1], [2, 3]])
    True

    >>> list_check3([[1], "nope"])
    False
    """
    return len(lst) == len([item for item in lst if isinstance(item, list)])
