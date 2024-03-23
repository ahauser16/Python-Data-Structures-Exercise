# Pros: This function is straightforward and easy to understand. It uses list comprehension, which is a compact way to filter a list. Cons: It creates a new list in memory, which can be inefficient for large inputs.

# The return statement return [item for item in lst if item] is using a list comprehension, which is a compact way to create a list in Python. Here's a breakdown of its syntax:

## return: This is a keyword in Python used to exit a function and return a value.

## [item for item in lst if item]: This is a list comprehension. It creates a new list by iterating over lst and including item for each item that is truthy.

### item for item in lst: This is a for loop that iterates over lst. item is a variable that gets assigned the value of each element in lst in turn. it generates a new list that's a copy of lst. Each element in lst is added to the new list in the same order.

#### for item in lst: This is a for loop that iterates over each element in the list lst. In each iteration, item is set to the current element.

#### item: This is the output expression that gets evaluated for each iteration of the loop. In this case, it's just the variable item, so the output is the same as the input.

### if item: This is a condition that filters the elements from lst. Only elements that are truthy (i.e., evaluate to True in a boolean context) are included in the new list. In Python, some values are considered False in a boolean context, such as None, False, zero (0, 0.0), empty collections ([], {}, '', ()), etc. All other values are considered True.

# So, the entire line of code returns a new list that includes only the truthy elements from lst.


def compact(lst):
    """Return a copy of lst with non-true elements removed.

    >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
    [1, 2, 'All done']
    """
    return [item for item in lst if item]


# Pros: This function uses a manual approach to filter the list, which allows for more control and potential optimizations. Cons: It's slightly more complex than the first function and may be slower for large lists due to the overhead of the loop and conditional statement.


def compact2(lst):
    """Return a copy of lst with non-true elements removed.

    >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
    [1, 2, 'All done']
    """
    result = []
    for item in lst:
        if item:
            result.append(item)
    return result


# Pros: This function uses the filterfalse function from the itertools module, which provides a high-level, efficient way to filter elements in a list. Cons: It's more complex than the other two functions and may be harder to understand for someone not familiar with the filterfalse function. It also requires the itertools module, which is not part of Python's standard library.

# Here's a breakdown of the syntax of the return statement:

## return: This is a keyword in Python used to exit a function and return a value.

## list(...): This is a function call to the built-in list function, which creates a new list from an iterable.

## filterfalse(lambda x: not x, lst): This is a function call to filterfalse, which is a function from the itertools module. filterfalse returns an iterator yielding those items of iterable for which function(item) is false. In this case, the function is lambda x: not x, and the iterable is lst.

### lambda x: not x: This is a lambda function, which is a small anonymous function. x is the parameter of this function, not x is the body of the function. It returns True if x is falsy (i.e., evaluates to False in a boolean context), and False if x is truthy.

### lst: This is the iterable being passed to filterfalse. The filterfalse function will apply the lambda function to each element in lst.

# So, the entire line of code returns a new list that includes only the falsy elements from lst. Since filterfalse returns the elements for which the function is false and the function is not x, it effectively returns the truthy elements.

from itertools import filterfalse


def compact3(lst):
    """Return a copy of lst with non-true elements removed.

    >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
    [1, 2, 'All done']
    """
    return list(filterfalse(lambda x: not x, lst))
