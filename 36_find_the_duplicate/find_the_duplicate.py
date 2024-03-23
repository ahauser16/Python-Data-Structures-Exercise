# Function 1: Using collections.Counter
# Pros: This function is easy to understand. It uses collections.Counter to count the occurrences of each number in nums.
# Cons: This function iterates over nums twice: once to count the occurrences and once to find the duplicate. This could be slower than necessary for large lists.
#
from collections import Counter
def find_the_duplicate1(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate1([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate1([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate1([2, 1, 3, 4]) is None
        True
    """
    counts = Counter(nums)
    for num, count in counts.items():
        if count > 1:
            return num
    return None


# Function 2: Using a set
# Pros: This function only iterates over nums once, which is more efficient than the first function. It uses a set to keep track of the numbers that have been seen.
# Cons: This function uses additional memory to store the set of seen numbers.
#
def find_the_duplicate2(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate2([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate2([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate2([2, 1, 3, 4]) is None
        True
    """
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None


# Function 3: Using list.sort
# Pros: This function does not use any additional memory (apart from a small amount for the recursion stack during the sort).
# Cons: This function sorts nums, which takes O(n log n) time. It also modifies the original list, which could be a problem if the original list is needed later.
#
def find_the_duplicate3(nums):
    """Find duplicate number in nums.

    Given a list of nums with, at most, one duplicate, return the duplicate.
    If there is no duplicate, return None

        >>> find_the_duplicate3([1, 2, 1, 4, 3, 12])
        1

        >>> find_the_duplicate3([6, 1, 9, 5, 3, 4, 9])
        9

        >>> find_the_duplicate3([2, 1, 3, 4]) is None
        True
    """
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]
    return None
