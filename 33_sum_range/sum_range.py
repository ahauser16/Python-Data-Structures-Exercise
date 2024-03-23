# Pros: This function is simple and straightforward. It sums the numbers from the start index to the end index. If end is not provided, it sums to the end of the list.
# Cons: The end index is exclusive, which might be counter-intuitive to some users who expect the end index to be inclusive.
def sum_range1(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range1(nums)
        10

        >>> sum_range1(nums, 1)
        9

        >>> sum_range1(nums, end=2)
        6

        >>> sum_range1(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range1(nums, 1, 99)
        9
    """
    if end is None:
        end = len(nums)
    else:
        end += 1  # make end inclusive
    return sum(nums[start:end])


# Pros: This function makes the end index inclusive, which might be more intuitive to some users.
# Cons: If the end index is greater than the length of the list, it will not throw an error but will return a result that might not be expected. For example, sum_range2([1, 2, 3], end=99) will return 6, not an error.
def sum_range2(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range2(nums)
        10

        >>> sum_range2(nums, 1)
        9

        >>> sum_range2(nums, end=2)
        6

        >>> sum_range2(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range2(nums, 1, 99)
        9
    """
    if end is None:
        end = len(nums)
    return sum(nums[start : end + 1])


# Pros: This function handles the case where the end index is greater than the length of the list. If end is greater than the length of the list, it sums to the end of the list, which might be the expected behavior.
# Cons: Like sum_range1, the end index is exclusive. Also, this function is slightly more complex than the other two because it has an additional condition to check.
def sum_range3(nums, start=0, end=None):
    """Return sum of numbers from start...end.

    - start: where to start (if not provided, start at list start)
    - end: where to stop (include this index) (if not provided, go through end)

        >>> nums = [1, 2, 3, 4]

        >>> sum_range3(nums)
        10

        >>> sum_range3(nums, 1)
        9

        >>> sum_range3(nums, end=2)
        6

        >>> sum_range3(nums, 1, 3)
        9

    If end is after end of list, just go to end of list:

        >>> sum_range3(nums, 1, 99)
        9
    """
    if end is None:
        end = len(nums)
    else:
        end += 1  # make end inclusive
    return sum(nums[start:end]) if end <= len(nums) else sum(nums[start:])
