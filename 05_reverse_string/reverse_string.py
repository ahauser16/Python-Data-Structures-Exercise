# Using Python's built-in string slicing:
# This is the most straightforward and Pythonic way to reverse a string. It uses Python's slicing syntax with a step of -1, which means it starts from the end and works its way to the start. This method is very efficient as slicing a string is O(n), where n is the length of the string.

def reverse_string(phrase):
    """Reverse string,

    >>> reverse_string('awesome')
    'emosewa'

    >>> reverse_string('sauce')
    'ecuas'
    """
    return phrase[::-1]

# Using the reversed() function and join():
# This method uses the reversed() function, which returns a reverse iterator, and then uses the join() method to concatenate all the characters into a string. This method is less efficient than the first one because reversed() is O(n) and join() is also O(n), but it can be useful if you need to do something with each character as you iterate through it.

def reverse_string2(phrase):
    """Reverse string,

    >>> reverse_string2('awesome')
    'emosewa'

    >>> reverse_string2('sauce')
    'ecuas'
    """
    return "".join(reversed(phrase))

# Using a loop to build the reversed string:
#     This method uses a loop to iterate through all the characters in the string and adds each character to the start of reversed_phrase. This method is the least efficient of the three because it requires iterating through the entire string and concatenating strings, which is O(n^2). However, it can be useful in situations where you need to do something with each character as you iterate through it.

def reverse_string3(phrase):
    """Reverse string,

    >>> reverse_string3('awesome')
    'emosewa'

    >>> reverse_string3('sauce')
    'ecuas'
    """
    reversed_phrase = ""
    for char in phrase:
        reversed_phrase = char + reversed_phrase
    return reversed_phrase
