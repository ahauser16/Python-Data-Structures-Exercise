# Using Python's built-in count() method:
# This is the most straightforward and Pythonic way to count the occurrences of a letter in a string. It uses Python's built-in count() method, which returns the number of times a substring appears in a string. This method is very efficient as count() is O(n), where n is the length of the string.


def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

    >>> single_letter_count('Hello World', 'h')
    1

    >>> single_letter_count('Hello World', 'z')
    0

    >>> single_letter_count("Hello World", 'l')
    3
    """
    return word.lower().count(letter.lower())


# Using a loop to iterate through the string:
# This method uses a loop to iterate through all the characters in the string and increments count each time it finds the letter. This method is less efficient than the first one because it requires iterating through the entire string, which is O(n), but it can be useful if you need to do something with each character as you iterate through it.


def single_letter_count2(word, letter):
    """How many times does letter appear in word (case-insensitively)?

    >>> single_letter_count2('Hello World', 'h')
    1

    >>> single_letter_count2('Hello World', 'z')
    0

    >>> single_letter_count2("Hello World", 'l')
    3
    """
    count = 0
    for char in word.lower():
        if char == letter.lower():
            count += 1
    return count


# Using a list comprehension and the len() function:
# This method uses a list comprehension to create a list of all the characters in the string that are equal to the letter, and then uses the len() function to count the number of elements in the list. This method is less efficient than the first two because it requires creating a new list, which is O(n), and then counting the elements in the list, which is also O(n). However, it can be useful in situations where you need to create a list of the characters that match the letter.


def single_letter_count3(word, letter):
    """How many times does letter appear in word (case-insensitively)?

    >>> single_letter_count3('Hello World', 'h')
    1

    >>> single_letter_count3('Hello World', 'z')
    0

    >>> single_letter_count3("Hello World", 'l')
    3
    """
    return len([char for char in word.lower() if char == letter.lower()])
