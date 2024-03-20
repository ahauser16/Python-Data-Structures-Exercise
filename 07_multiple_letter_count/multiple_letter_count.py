# Using Python's built-in dictionary comprehension:
# This is the most straightforward and Pythonic way to count the occurrences of each character in a string. It uses Python's dictionary comprehension, which is a concise way to create dictionaries. This method is not very efficient as it calls count() for each character in the string, resulting in a time complexity of O(n^2).


def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

    >>> multiple_letter_count('yay')
    {'y': 2, 'a': 1}

    >>> multiple_letter_count('Yay')
    {'Y': 1, 'a': 1, 'y': 1}
    """
    return {char: phrase.count(char) for char in phrase}


# Using a dictionary and a loop:
#     This method uses a loop to iterate through all the characters in the string and a dictionary to keep track of the counts. It is more efficient than the first method as it only requires a single pass through the string, resulting in a time complexity of O(n).


def multiple_letter_count2(phrase):
    """Return dict of {ltr: frequency} from phrase.

    >>> multiple_letter_count2('yay')
    {'y': 2, 'a': 1}

    >>> multiple_letter_count2('Yay')
    {'Y': 1, 'a': 1, 'y': 1}
    """
    letter_counts = {}
    for char in phrase:
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    return letter_counts


# Using Python's built-in collections.Counter class:
# This method uses the Counter class from the collections module, which is a dictionary subclass for counting hashable objects. It is the most efficient method as Counter is implemented in C and can count the characters in the string in O(n). However, it requires importing an additional module.

from collections import Counter
def multiple_letter_count3(phrase):
    """Return dict of {ltr: frequency} from phrase.

    >>> multiple_letter_count3('yay')
    {'y': 2, 'a': 1}

    >>> multiple_letter_count3('Yay')
    {'Y': 1, 'a': 1, 'y': 1}
    """
    return dict(Counter(phrase))
