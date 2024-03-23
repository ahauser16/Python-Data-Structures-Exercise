# Pros: This function is straightforward and easy to understand. It uses Python's built-in string methods and slicing to reverse the string. Cons: It creates a new string in memory when reversing the phrase, which can be inefficient for large inputs.


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
    phrase = phrase.replace(" ", "").lower()
    return phrase == phrase[::-1]


# Pros: This function is more memory-efficient than the first one because it doesn't create a new string in memory. It only checks up to the middle of the string, which can save time for large inputs. Cons: It's slightly more complex than the first function.
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
    phrase = phrase.replace(" ", "").lower()
    for i in range(len(phrase) // 2):
        if phrase[i] != phrase[-i - 1]:
            return False
    return True


# Pros: This function uses regular expressions to remove all non-alphanumeric characters, not just spaces. This makes it more flexible and able to handle a wider range of inputs. Cons: It's more complex than the other two functions and may be harder to understand for someone not familiar with regular expressions. It also has the same memory inefficiency as the first function when reversing the string.  import re is a statement in Python that includes the re module in your program. The re module stands for Regular Expressions, which is a powerful tool for manipulating text and data.  You can use it to check if a string contains a certain pattern, replace parts of a string, and much more. In the context of the is_palindrome3 function, re.sub(r'\W+', '', phrase) is used to remove all non-alphanumeric characters from the phrase. The \W+ is a regular expression pattern that matches any non-alphanumeric character.

import re
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
    phrase = re.sub(r"\W+", "", phrase).lower()
    return phrase == phrase[::-1]
