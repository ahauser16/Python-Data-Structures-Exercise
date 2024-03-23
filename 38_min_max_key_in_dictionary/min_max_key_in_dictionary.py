# Function 1: Using min and max functions
# Pros: This function is very concise and easy to understand. It uses the built-in min and max functions to find the minimum and maximum keys.
# Cons: This function calls min and max separately, which means it iterates over the keys of d twice.
#
def min_max_keys1(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys1({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys1({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    return (min(d), max(d))


# Function 2: Using sorted
# Pros: This function only iterates over the keys of d once, which is more efficient than the first function.
# Cons: This function sorts the keys, which takes O(n log n) time. This is slower than necessary, since finding the minimum and maximum of a list can be done in O(n) time.
#
def min_max_keys2(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys2({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys2({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    keys = sorted(d)
    return (keys[0], keys[-1])


# Function 3: Using a for loop
# Pros: This function finds the minimum and maximum keys in O(n) time, which is the fastest possible time complexity for this problem.
# Cons: This function is longer and more complex than the other functions. It also uses next(iter(d)) to get the first key of d, which might be confusing to some people.
#
def min_max_keys3(d):
    """Return tuple (min-keys, max-keys) in d.

        >>> min_max_keys3({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'})
        (1, 10)

    Works with any kind of key that can be compared, like strings:

        >>> min_max_keys3({"apple": "red", "cherry": "red", "berry": "blue"})
        ('apple', 'cherry')
    """
    min_key = max_key = next(iter(d))
    for key in d:
        if key < min_key:
            min_key = key
        elif key > max_key:
            max_key = key
    return (min_key, max_key)
