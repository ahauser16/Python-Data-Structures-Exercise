### hint: to find out if something is a float, you should use the "isinstance" function --- research how to use this to find out if something is a float!
# Pros: This function is straightforward and easy to understand. It uses the 'isinstance' function to check if each number is a float, and the sum function to add them up. This is efficient and idiomatic Python. Cons: It iterates over nums once, which can be inefficient for large inputs.
def sum_floats1(nums):
    """Return sum of floating point numbers in nums.

    >>> sum_floats1([1.5, 2.4, 'awesome', [], 1])
    3.9

    >>> sum_floats1([1, 2, 3])
    0
    """
    return sum(num for num in nums if isinstance(num, float))


# Pros: This function is similar to the first one, but uses the type function instead of 'isinstance'. This can be faster for large inputs, as type is slightly faster than isinstance. Cons: The type function does not consider inheritance, so it would not consider subclasses of float to be floats. However, this is unlikely to be an issue in this case.
def sum_floats2(nums):
    """Return sum of floating point numbers in nums.

    >>> sum_floats2([1.5, 2.4, 'awesome', [], 1])
    3.9

    >>> sum_floats2([1, 2, 3])
    0
    """
    return sum(num for num in nums if type(num) is float)


# Pros: This function uses a manual approach to sum the floats, which allows for more control and potential optimizations. It only iterates over nums once. Cons: It's slightly more complex than the other two functions due to the use of a loop and conditional statement. It also does not take advantage of Python's high-level features.
def sum_floats3(nums):
    """Return sum of floating point numbers in nums.

    >>> sum_floats3([1.5, 2.4, 'awesome', [], 1])
    3.9

    >>> sum_floats3([1, 2, 3])
    0
    """
    total = 0
    for num in nums:
        if isinstance(num, float):
            total += num
    return total
