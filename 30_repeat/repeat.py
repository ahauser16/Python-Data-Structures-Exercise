# Pros: This function is straightforward and easy to understand. It checks if num is a non-negative integer before multiplying phrase by num.
# Cons: It uses an isinstance check, which can be seen as less Pythonic than using a try-except block.
def repeat1(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat1('*', 3)
        '***'

        >>> repeat1('abc', 2)
        'abcabc'

        >>> repeat1('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat1('abc', -1) is None
        True

        >>> repeat1('abc', 'nope') is None
        True
    """
    if not isinstance(num, int) or num < 0:
        return None
    return phrase * num


# Pros: This function uses a try-except block to handle the case where num is not an integer. This is a more Pythonic way of handling errors, and it allows the function to handle any type of num, not just integers.
# Cons: It's slightly more complex than the first function due to the use of a try-except block.
def repeat2(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat2('*', 3)
        '***'

        >>> repeat2('abc', 2)
        'abcabc'

        >>> repeat2('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat2('abc', -1) is None
        True

        >>> repeat2('abc', 'nope') is None
        True
    """
    try:
        if num < 0:
            return None
        return phrase * num
    except TypeError:
        return None


# Pros: This function is similar to the first one, but it uses type hints to indicate the types of the parameters and the return type. This can make the function easier to understand and use correctly.
# Cons: It requires importing the typing module to use the Optional type hint. It's also slightly more complex than the first function due to the additional isinstance check and type hints.
from typing import Optional


def repeat3(phrase: str, num: Optional[int]) -> Optional[str]:
    """Return phrase, repeated num times.

        >>> repeat3('*', 3)
        '***'

        >>> repeat3('abc', 2)
        'abcabc'

        >>> repeat3('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat3('abc', -1) is None
        True

        >>> repeat3('abc', 'nope') is None
        True
    """
    if isinstance(num, int) and num >= 0:
        return phrase * num
    return None
