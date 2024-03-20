# Using Python's built-in string methods and slicing:
# This method first cleans the input phrase by converting it to lowercase and removing any non-alphanumeric characters. It then checks if the cleaned phrase is the same as its reverse. This method is very efficient as it only requires a single pass through the string, resulting in a time complexity of O(n).


def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    cleaned = "".join(c for c in phrase.lower() if c.isalnum())
    return cleaned == cleaned[::-1]


# Using a loop to compare characters from both ends:
def is_palindrome2(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome2('tacocat')
        True

        >>> is_palindrome2('noon')
        True

        >>> is_palindrome2('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome2('taco cat')
        True

        >>> is_palindrome2('Noon')
        True
    """
    cleaned = "".join(c for c in phrase.lower() if c.isalnum())
    for i in range(len(cleaned) // 2):
        if cleaned[i] != cleaned[-i - 1]:
            return False
    return True


# Using Python's built-in reversed() function and join():
# This method cleans the input phrase and then uses the reversed() function to create a reversed copy of the cleaned phrase. It then checks if the cleaned phrase is the same as its reversed copy.


def is_palindrome3(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome3('tacocat')
        True

        >>> is_palindrome3('noon')
        True

        >>> is_palindrome3('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome3('taco cat')
        True

        >>> is_palindrome3('Noon')
        True
    """
    cleaned = "".join(c for c in phrase.lower() if c.isalnum())
    return cleaned == "".join(reversed(cleaned))
