# NOTE: don't worry about an optimized runtime here; it's fine if
# you have a runtime worse than O(n)

# NOTE: you can sort lists with lst.sort(), which works in place (mutates);
# you may find it helpful to research the `sorted(iter)` function, which
# can take *any* type of list-like-thing, and returns a new, sorted list
# from it.


# Function 1: Using sorted and set
# Pros: This function is very concise and easy to understand. It uses set to remove duplicates and sorted to sort the ages.
# Cons: This function creates a new list when sorting the ages, which could use more memory than necessary for large lists.
#
def two_oldest_ages1(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages1([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages1([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages1([1, 5, 5, 2])
        (2, 5)
    """
    distinct_ages = sorted(set(ages))
    return (distinct_ages[-2], distinct_ages[-1])


# Function 2: Using sort in place and set
# Pros: This function sorts the ages in place, which uses less memory than creating a new sorted list.
# Cons: This function is a bit longer than the first one. It also modifies the original list, which could be a problem if the original list is needed later.
def two_oldest_ages2(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages2([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages2([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages2([1, 5, 5, 2])
        (2, 5)
    """
    distinct_ages = list(set(ages))
    distinct_ages.sort()
    return (distinct_ages[-2], distinct_ages[-1])


# Function 3: Using heapq.nlargest
# Pros: This function uses heapq.nlargest to find the two largest ages, which is more efficient than sorting the entire list for large lists.
# Cons: This function uses the heapq module, which might be less familiar to some people. It also returns the ages in reverse order, so it needs to reverse them again before returning.
import heapq
def two_oldest_ages3(ages):
    """Return two distinct oldest ages as tuple (second-oldest, oldest)..

        >>> two_oldest_ages3([1, 2, 10, 8])
        (8, 10)

        >>> two_oldest_ages3([6, 1, 9, 10, 4])
        (9, 10)

    Even if more than one person has the same oldest age, this should return
    two *distinct* oldest ages:

        >>> two_oldest_ages3([1, 5, 5, 2])
        (2, 5)
    """
    two_oldest = heapq.nlargest(2, set(ages))
    return (two_oldest[1], two_oldest[0])
