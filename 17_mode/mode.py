# Pros: This function uses the Counter class from the collections module, which provides a high-level, efficient way to count elements in a list and find the most common element. Cons: It's more complex than a manual approach and may be harder to understand for someone not familiar with the Counter class. It also requires the collections module, which is not part of Python's standard library.
from collections import Counter


def mode1(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode1([1, 2, 1])
        1

        >>> mode1([2, 2, 3, 3, 2])
        2
    """
    return Counter(nums).most_common(1)[0][0]


# Pros: This function uses the built-in max function with a custom key function, which is a compact way to find the element that maximizes a certain function. It also uses a set to eliminate duplicate checks. Cons: It's more complex than a manual approach and may be slower for large lists due to the overhead of the max function and the count method.
def mode2(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode2([1, 2, 1])
        1

        >>> mode2([2, 2, 3, 3, 2])
        2
    """
    return max(set(nums), key=nums.count)


#Pros: This function uses a manual approach to find the mode, which allows for more control and potential optimizations. Cons: It's more complex than the other two functions and may be slower for large lists due to the overhead of the loop and the count method. It also doesn't take advantage of Python's high-level features.
def mode3(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode3([1, 2, 1])
        1

        >>> mode3([2, 2, 3, 3, 2])
        2
    """
    max_count = 0
    mode = None
    for num in nums:
        count = nums.count(num)
        if count > max_count:
            max_count = count
            mode = num
    return mode
