#Pros: This function is straightforward and easy to understand. It uses a list comprehension to create a list of factors of num. This is efficient and idiomatic Python.
#Cons: It checks every number from 1 to num, which can be inefficient for large inputs.
def find_factors1(num):
    """Find factors of num, in increasing order.

    >>> find_factors1(10)
    [1, 2, 5, 10]

    >>> find_factors1(11)
    [1, 11]

    >>> find_factors1(111)
    [1, 3, 37, 111]

    >>> find_factors1(321421)
    [1, 293, 1097, 321421]
    """
    return [i for i in range(1, num + 1) if num % i == 0]



#Pros: This function is similar to the first one, but it uses a for loop and an append method instead of a list comprehension. This can be more efficient for large inputs because it avoids creating a new list for each factor.
#Cons: It's slightly more complex than the first function due to the use of an additional variable and a for loop.
def find_factors2(num):
    """Find factors of num, in increasing order.

    >>> find_factors2(10)
    [1, 2, 5, 10]

    >>> find_factors2(11)
    [1, 11]

    >>> find_factors2(111)
    [1, 3, 37, 111]

    >>> find_factors2(321421)
    [1, 293, 1097, 321421]
    """
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors



#Pros: This function uses a set to store the factors, which eliminates duplicates. It also only checks numbers up to the square root of num, which can be much more efficient for large inputs.
#Cons: It's more complex than the other two functions due to the use of a set, the math.isqrt function, and the sorted function. It also requires importing the math module.
import math
def find_factors3(num):
    """Find factors of num, in increasing order.

    >>> find_factors3(10)
    [1, 2, 5, 10]

    >>> find_factors3(11)
    [1, 11]

    >>> find_factors3(111)
    [1, 3, 37, 111]

    >>> find_factors3(321421)
    [1, 293, 1097, 321421]
    """
    factors = set()
    for i in range(1, math.isqrt(num) + 1):
        if num % i == 0:
            factors.add(i)
            factors.add(num // i)
    return sorted(list(factors))


# follow up explantation of third function: The third function, find_factors3, uses a mathematical property of factors to optimize the process of finding factors. The property is that a factor of a number num that is greater than its square root must be paired with a factor less than the square root. This is because the square root of a number is the point where the factors "flip" over.

# For example, consider the number 36. Its square root is 6. The factors of 36 are 1, 2, 3, 4, 6, 9, 12, 18, and 36. Notice that after 6, the factors are just the pairs of the previous factors "flipped" and multiplied together (136, 218, 312, 49).

# So, to find the factors of a number, you only need to iterate up to its square root and for each factor you find, you can find its pair by dividing the number by the factor. This is what find_factors3 does. It iterates up to the square root of num and for each i that is a factor of num, it adds both i and num // i to the set of factors.

# This approach is much more efficient for large inputs because it significantly reduces the number of iterations. It does not result in undesirable behavior or an error because it still finds all the factors of num, just in a more efficient way.
