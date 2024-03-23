# Pros: This function is straightforward and easy to understand. It uses list comprehension, which is a compact way to filter a list and apply a function to each element. Cons: It iterates over nums once, which can be inefficient for large inputs.
def triple_and_filter1(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.

        >>> triple_and_filter1([1, 2, 3, 4])
        [12]

        >>> triple_and_filter1([6, 8, 10, 12])
        [24, 36]

        >>> triple_and_filter1([1, 2])
        []
    """
    return [num * 3 for num in nums if num % 4 == 0]


# Pros: This function uses the filter and map functions, which provide high-level, efficient ways to filter elements in a list and apply a function to each element. It only iterates over nums once. Cons: It's more complex than the first function and may be harder to understand for someone not familiar with the filter and map functions and lambda expressions.
def triple_and_filter2(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.

        >>> triple_and_filter2([1, 2, 3, 4])
        [12]

        >>> triple_and_filter2([6, 8, 10, 12])
        [24, 36]

        >>> triple_and_filter2([1, 2])
        []
    """
    return list(map(lambda num: num * 3, filter(lambda num: num % 4 == 0, nums)))


# Pros: This function uses a manual approach to filter the list and apply the function, which allows for more control and potential optimizations. It only iterates over nums once. Cons: It's slightly more complex than the first function and may be slower for small lists due to the overhead of the loop and conditional statement.
def triple_and_filter3(nums):
    """Return new list of tripled nums for those nums divisible by 4.

    Return every number in list that is divisible by 4 in a new list,
    except multipled by 3.

        >>> triple_and_filter3([1, 2, 3, 4])
        [12]

        >>> triple_and_filter3([6, 8, 10, 12])
        [24, 36]

        >>> triple_and_filter3([1, 2])
        []
    """
    result = []
    for num in nums:
        if num % 4 == 0:
            result.append(num * 3)
    return result
