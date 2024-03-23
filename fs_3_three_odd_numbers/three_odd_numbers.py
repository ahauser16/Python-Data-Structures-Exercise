# Function 1: Using a for loop
# Pros: This function is straightforward and easy to understand. It uses a for loop to iterate over the indices of nums.
# Cons: This function uses a loop, which could be slower than a more vectorized approach for large lists.
#
def three_odd_numbers1(nums):
    """Is the sum of any 3 sequential numbers odd?"

    >>> three_odd_numbers1([1, 2, 3, 4, 5])
    True

    >>> three_odd_numbers1([0, -2, 4, 1, 9, 12, 4, 1, 0])
    True

    >>> three_odd_numbers1([5, 2, 1])
    False

    >>> three_odd_numbers1([1, 2, 3, 3, 2])
    False
    """
    for i in range(len(nums) - 2):
        if sum(nums[i : i + 3]) % 2 == 1:
            return True
    return False


# Function 2: Using list comprehension
# Pros: This function is very concise. It uses list comprehension to check if the sum of any three sequential numbers is odd in a single line of code.
# Cons: This function might be a bit harder to understand for people who are not familiar with list comprehension.
#
def three_odd_numbers2(nums):
    """Is the sum of any 3 sequential numbers odd?"

    >>> three_odd_numbers2([1, 2, 3, 4, 5])
    True

    >>> three_odd_numbers2([0, -2, 4, 1, 9, 12, 4, 1, 0])
    True

    >>> three_odd_numbers2([5, 2, 1])
    False

    >>> three_odd_numbers2([1, 2, 3, 3, 2])
    False
    """
    return any(sum(nums[i : i + 3]) % 2 == 1 for i in range(len(nums) - 2))


# Function 3: Using a while loop
# Pros: This function uses a while loop, which can be more efficient than a for loop or list comprehension for certain inputs (it stops as soon as it finds a sequence that sums to an odd number).
# Cons: This function is longer and more complex than the other functions. It also uses a while loop, which might be less familiar to some people.
#
def three_odd_numbers3(nums):
    """Is the sum of any 3 sequential numbers odd?"

    >>> three_odd_numbers3([1, 2, 3, 4, 5])
    True

    >>> three_odd_numbers3([0, -2, 4, 1, 9, 12, 4, 1, 0])
    True

    >>> three_odd_numbers3([5, 2, 1])
    False

    >>> three_odd_numbers3([1, 2, 3, 3, 2])
    False
    """
    i = 0
    while i < len(nums) - 2:
        if sum(nums[i : i + 3]) % 2 == 1:
            return True
        i += 1
    return False
