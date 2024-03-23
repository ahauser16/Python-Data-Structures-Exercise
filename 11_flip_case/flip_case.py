# Pros: This function is straightforward and easy to understand. It uses Python's built-in string method swapcase and list comprehension to flip the case of to_swap in phrase. Cons: It creates a new list in memory when using list comprehension, which can be inefficient for large inputs.
def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

    >>> flip_case('Aaaahhh', 'a')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'A')
    'aAAAhhh'

    >>> flip_case('Aaaahhh', 'h')
    'AaaaHHH'

    """
    return "".join(
        [
            char.swapcase() if char.lower() == to_swap.lower() else char
            for char in phrase
        ]
    )


# Pros: This function is more memory-efficient than the first one because it doesn't create a new list in memory. It builds the result string incrementally. Cons: It's slightly more complex than the first function.
def flip_case2(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

    >>> flip_case2('Aaaahhh', 'a')
    'aAAAhhh'

    >>> flip_case2('Aaaahhh', 'A')
    'aAAAhhh'

    >>> flip_case2('Aaaahhh', 'h')
    'AaaaHHH'

    """
    result = ""
    for char in phrase:
        if char.lower() == to_swap.lower():
            result += char.swapcase()
        else:
            result += char
    return result


# Pros: This function uses the translate and maketrans string methods, which can be more efficient than the other two methods for large inputs because they operate at the C level in Python's implementation. Cons: It's more complex than the other two functions and may be harder to understand for someone not familiar with the translate and maketrans methods.
def flip_case3(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

    >>> flip_case3('Aaaahhh', 'a')
    'aAAAhhh'

    >>> flip_case3('Aaaahhh', 'A')
    'aAAAhhh'

    >>> flip_case3('Aaaahhh', 'h')
    'AaaaHHH'

    """
    to_swap = to_swap.lower()
    return phrase.translate(str.maketrans(to_swap + to_swap.upper(), to_swap.upper() + to_swap))