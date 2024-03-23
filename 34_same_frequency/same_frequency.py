# Function 1: Using collections.Counter
# Pros: This function is very concise and easy to understand. The collections.Counter class makes it easy to count the frequency of elements in a collection.
# Cons: This function converts the numbers to strings, which could be a bit slower than working with the numbers directly.
#
from collections import Counter
def same_frequency1(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency1(551122, 221515)
    True

    >>> same_frequency1(321142, 3212215)
    False

    >>> same_frequency1(1212, 2211)
    True
    """
    return Counter(str(num1)) == Counter(str(num2))


# Function 2: Using dictionaries
# Pros: This function works directly with the numbers and does not require any additional libraries.
# Cons: This function is a bit longer and more complex than the first one. It also converts the numbers to strings.
#
def same_frequency2(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency1(551122, 221515)
    True

    >>> same_frequency1(321142, 3212215)
    False

    >>> same_frequency1(1212, 2211)
    True
    """
    def get_freq(n):
        freq = {}
        for digit in str(n):
            freq[digit] = freq.get(digit, 0) + 1
        return freq

    return get_freq(num1) == get_freq(num2)


# Function 3: Using sorted strings
# Pros: This function is very concise and easy to understand. It simply sorts the digits in num1 and num2 and compares these sorted lists.
# Cons: This function converts the numbers to strings and sorts these strings, which could be slower than the other methods for large numbers. Also, sorting is not necessary to solve this problem, so this function does more work than necessary.
#
def same_frequency3(num1, num2):
    """Do these nums have same frequencies of digits?

    >>> same_frequency3(551122, 221515)
    True

    >>> same_frequency3(321142, 3212215)
    False

    >>> same_frequency3(1212, 2211)
    True
    """
    return sorted(str(num1)) == sorted(str(num2))