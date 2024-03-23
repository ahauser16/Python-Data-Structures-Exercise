# Function 1: Using a for loop
# Pros: This function is straightforward and easy to understand. It uses a for loop to iterate over the characters in word.
# Cons: This function uses a loop, which could be slower than a more vectorized approach for large words.
#
def is_odd_string1(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:

        >>> is_odd_string1('a')
        True

        >>> is_odd_string1('A')
        True

    These sum to 4, which is not odd:

        >>> is_odd_string1('aaaa')
        False

        >>> is_odd_string1('AAaa')
        False

    Longer example:

        >>> is_odd_string1('amazing')
        True
    """
    total = 0
    for char in word:
        total += ord(char.lower()) - ord("a") + 1
    return total % 2 == 1


# Function 2: Using list comprehension
# Pros: This function is very concise. It uses list comprehension to sum the character positions in a single line of code.
# Cons: This function might be a bit harder to understand for people who are not familiar with list comprehension.
#
def is_odd_string2(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:

        >>> is_odd_string2('a')
        True

        >>> is_odd_string2('A')
        True

    These sum to 4, which is not odd:

        >>> is_odd_string2('aaaa')
        False

        >>> is_odd_string2('AAaa')
        False

    Longer example:

        >>> is_odd_string2('amazing')
        True
    """
    return sum(ord(char.lower()) - ord("a") + 1 for char in word) % 2 == 1


# Function 3: Using map
# Pros: This function uses map, which is a powerful function that applies a function to every item in a list (or any iterable). This can be more efficient than a for loop or list comprehension for large words.
# Cons: This function uses a lambda function, which might be less familiar to some people. It also uses map, which can be slower than list comprehension for small words.
#
def is_odd_string3(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:

        >>> is_odd_string3('a')
        True

        >>> is_odd_string3('A')
        True

    These sum to 4, which is not odd:

        >>> is_odd_string3('aaaa')
        False

        >>> is_odd_string3('AAaa')
        False

    Longer example:

        >>> is_odd_string3('amazing')
        True
    """
    return sum(map(lambda char: ord(char.lower()) - ord("a") + 1, word)) % 2 == 1
