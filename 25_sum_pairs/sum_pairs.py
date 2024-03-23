#Pros: This function is straightforward and easy to understand. It uses a set to keep track of the numbers it has already seen, which allows it to find pairs that sum to the goal in one pass through the list. This is efficient and idiomatic Python. Cons: It creates a new set, which can be inefficient for large inputs.
def sum_pairs1(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs1([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs1([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs1([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs1([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    already_visited = set()
    for num in nums:
        diff = goal - num
        if diff in already_visited:
            return (diff, num)
        already_visited.add(num)
    return ()


# In this refactored version, the function uses a dictionary to keep track of the numbers it has already seen. When it finds a number that is the difference of the goal and a number it has seen before, it returns that pair. This ensures that the function returns the pair that appears first in the list.
def sum_pairs2(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs2([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs2([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs2([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs2([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    already_visited = {}
    for i, num in enumerate(nums):
        diff = goal - num
        if diff in already_visited:
            return (diff, num)
        already_visited[num] = i
    return ()


# Pros: This function uses a dictionary to map numbers to their indices, which allows it to find pairs that sum to the goal in one pass through the list. This is more efficient than the second function. Cons: It's more complex than the first function due to the use of a dictionary. It also creates a new dictionary, which can be inefficient for large inputs.  ***This function was refactored so that the dictionary is now built as we iterate over the list, instead of being built beforehand. This ensures that we check pairs in the order they appear in the list. When we find a number that is the difference of the goal and a number we have seen before, we return that pair. This ensures that the function returns the pair that appears first in the list.
def sum_pairs3(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs3([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs3([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs3([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs3([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    nums_dict = {}
    for i, num in enumerate(nums):
        diff = goal - num
        if diff in nums_dict:
            return (diff, num)
        nums_dict[num] = i
    return ()


