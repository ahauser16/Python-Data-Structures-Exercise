# Pros: This function is straightforward and easy to understand. It checks if n is less than 3 and returns a message if it is. Otherwise, it checks if n is greater than the length of phrase and returns phrase if it is. Otherwise, it returns the first n-3 characters of phrase followed by '...'.
# Cons: It uses multiple if-else statements, which can be seen as less Pythonic than using a single return statement with a conditional expression.
def truncate1(phrase, n):
    """Return truncated-at-n-chars version of  phrase.

    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.

        >>> truncate1("Hello World", 6)
        'Hel...'

        >>> truncate1("Problem solving is the best!", 10)
        'Problem...'

        >>> truncate1("Yo", 100)
        'Yo'

    The smallest legal value of n is 3; if less, return a message:

        >>> truncate1('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate1("Woah", 4)
        'W...'

        >>> truncate1("Woah", 3)
        '...'
    """
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    elif n > len(phrase) + 2:
        return phrase
    else:
        return phrase[:n-3] + '...'


# Pros: This function is similar to the first one, but it uses a single return statement with a conditional expression. This is a more Pythonic way of writing the function, and it makes the function shorter and easier to read.
# Cons: It's slightly more complex than the first function due to the use of a conditional expression.
#refactors required:  First, The truncate2 function failed the test truncate2("Yo", 100) because it added '...' to the end of phrase even though n was greater than the length of phrase. According to the docstring, the function should return phrase as is if n is greater than or equal to the length of phrase.  The issue lies in the return statement. The condition n > 2 is always true when n is greater than or equal to the length of phrase, because the function returns earlier if n < 3. Therefore, the function always adds '...' to the end of phrase, even when it shouldn't.  To fix this issue, you can modify the return statement to check if n is greater than or equal to the length of phrase. If it is, the function should return phrase as is. Otherwise, it should return the first n-3 characters of phrase followed by '...'.
#refactors required: Second, The truncate2 function failed the test truncate2("Woah", 4) because it returned the full string "Woah" when n was equal to the length of the string. According to the docstring, if the phrase is longer than, or the same size as, n it should end with '...' and be no longer than n.  To fix this issue, you can modify the return statement to check if n is strictly greater than the length of phrase. If it is, the function should return phrase as is. Otherwise, it should return the first n-3 characters of phrase followed by '...'.
def truncate2(phrase, n):
    """Return truncated-at-n-chars version of  phrase.

    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.

        >>> truncate2("Hello World", 6)
        'Hel...'

        >>> truncate2("Problem solving is the best!", 10)
        'Problem...'

        >>> truncate2("Yo", 100)
        'Yo'

    The smallest legal value of n is 3; if less, return a message:

        >>> truncate2('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate2("Woah", 4)
        'W...'

        >>> truncate2("Woah", 3)
        '...'
    """
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    return phrase if n > len(phrase) else phrase[:n-3] + '...'


# Pros: This function is similar to the first one, but it checks if n is greater than the length of phrase in a separate if statement. This avoids the need to subtract 3 from n in the return statement, which makes the function easier to understand.
# Cons: It's slightly more complex than the first function due to the use of an additional if statement.
def truncate3(phrase, n):
    """Return truncated-at-n-chars version of  phrase.

    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.

        >>> truncate3("Hello World", 6)
        'Hel...'

        >>> truncate3("Problem solving is the best!", 10)
        'Problem...'

        >>> truncate3("Yo", 100)
        'Yo'

    The smallest legal value of n is 3; if less, return a message:

        >>> truncate3('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate3("Woah", 4)
        'W...'

        >>> truncate3("Woah", 3)
        '...'
    """
    if n < 3:
        return 'Truncation must be at least 3 characters.'
    return phrase if n > len(phrase) else phrase[:n-3] + '...'
