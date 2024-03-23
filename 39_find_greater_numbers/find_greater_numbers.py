# Function 1: Using nested for loops
# Pros: This function is straightforward and easy to understand. It uses nested for loops to compare each pair of numbers.
# Cons: This function has a time complexity of O(n^2), which could be slow for large lists.
#
def find_greater_numbers1(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers1([1, 2, 3])
        3

        >>> find_greater_numbers1([6, 1, 2, 7])
        4

        >>> find_greater_numbers1([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers1([])
        0
    """
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1
    return count


# Function 2: Using list comprehension
# Pros: This function is very concise. It uses list comprehension to count the number of times a number is followed by a greater number in a single line of code.
# Cons: Like the first function, this function has a time complexity of O(n^2). It might also be harder to understand for people who are not familiar with list comprehension.
#
def find_greater_numbers2(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers2([1, 2, 3])
        3

        >>> find_greater_numbers2([6, 1, 2, 7])
        4

        >>> find_greater_numbers2([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers2([])
        0
    """
    return sum(
        1
        for i in range(len(nums))
        for j in range(i + 1, len(nums))
        if nums[j] > nums[i]
    )


# Function 3: Using a modified version of the bubble sort algorithm
# Pros: This function sorts nums while counting the number of times a number is followed by a greater number. This could potentially be faster than the other functions for certain inputs.
# Cons: This function modifies the original list, which could be a problem if the original list is needed later. It also has a time complexity of O(n^2), like the other functions.
#
def find_greater_numbers3(nums):
    """Return # of times a number is followed by a greater number.

    For example, for [1, 2, 3], the answer is 3:
    - the 1 is followed by the 2 *and* the 3
    - the 2 is followed by the 3

    Examples:

        >>> find_greater_numbers3([1, 2, 3])
        3

        >>> find_greater_numbers3([6, 1, 2, 7])
        4

        >>> find_greater_numbers3([5, 4, 3, 2, 1])
        0

        >>> find_greater_numbers3([])
        0
    """
    count = 0
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                count += 1
                nums[i], nums[j] = nums[j], nums[i]  # swap nums[i] and nums[j]
    return count
