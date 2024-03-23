# Pros: This function is straightforward and easy to understand. It uses list comprehension, which is a compact way to filter a list. Cons: It iterates over lst twice, which can be inefficient for large inputs.
def partition1(lst, fn):
    """Partition lst by predicate.

    - lst: list of items
    - fn: function that returns True or False

    Returns new list: [a, b], where `a` are items that passed fn test,
    and `b` are items that failed fn test.

       >>> def is_even(num):
       ...     return num % 2 == 0

       >>> def is_string(el):
       ...     return isinstance(el, str)

       >>> partition1([1, 2, 3, 4], is_even)
       [[2, 4], [1, 3]]

       >>> partition1(["hi", None, 6, "bye"], is_string)
       [['hi', 'bye'], [None, 6]]
    """
    return [[x for x in lst if fn(x)], [x for x in lst if not fn(x)]]


# Pros: This function uses a manual approach to filter the list, which allows for more control and potential optimizations. It only iterates over lst once. Cons: It's slightly more complex than the first function and may be slower for small lists due to the overhead of the loop and conditional statement.
def partition2(lst, fn):
    """Partition lst by predicate.

    - lst: list of items
    - fn: function that returns True or False

    Returns new list: [a, b], where `a` are items that passed fn test,
    and `b` are items that failed fn test.

       >>> def is_even(num):
       ...     return num % 2 == 0

       >>> def is_string(el):
       ...     return isinstance(el, str)

       >>> partition2([1, 2, 3, 4], is_even)
       [[2, 4], [1, 3]]

       >>> partition2(["hi", None, 6, "bye"], is_string)
       [['hi', 'bye'], [None, 6]]
    """
    pass_list = []
    fail_list = []
    for item in lst:
        (pass_list if fn(item) else fail_list).append(item)
    return [pass_list, fail_list]


# Pros: This function uses the filter and filterfalse functions from the itertools module, which provide high-level, efficient ways to filter elements in a list. It only iterates over lst once. Cons: It's more complex than the other two functions and may be harder to understand for someone not familiar with the filter and filterfalse functions. It also requires the itertools module, which is not part of Python's standard library.
from itertools import filterfalse


def partition3(lst, fn):
    """Partition lst by predicate.

    - lst: list of items
    - fn: function that returns True or False

    Returns new list: [a, b], where `a` are items that passed fn test,
    and `b` are items that failed fn test.

       >>> def is_even(num):
       ...     return num % 2 == 0

       >>> def is_string(el):
       ...     return isinstance(el, str)

       >>> partition3([1, 2, 3, 4], is_even)
       [[2, 4], [1, 3]]

       >>> partition3(["hi", None, 6, "bye"], is_string)
       [['hi', 'bye'], [None, 6]]
    """
    pass_iter = filter(fn, lst)
    fail_iter = filterfalse(fn, lst)
    return [list(pass_iter), list(fail_iter)]
