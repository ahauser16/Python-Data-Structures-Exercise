# Pros: This function is straightforward and easy to understand. It uses set intersection to find common hobbies, which is efficient. Cons: It converts the lists of hobbies to sets, which can be inefficient for large lists.
def friend_date1(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date1(elmo, sauron)
        False

        >>> friend_date1(sauron, gandalf)
        True
    """
    return bool(set(a[2]) & set(b[2]))

    # Pros: This function uses the built-in any function and a generator expression, which is a compact way to check if any hobbies are in common. It stops as soon as it finds a common hobby, which can be more efficient than the first function for large lists with a common hobby near the start. Cons: It's slightly more complex than the first function and may be slower for large lists without a common hobby, due to the overhead of the in operator.


def friend_date2(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date2(elmo, sauron)
        False

        >>> friend_date2(sauron, gandalf)
        True
    """
    return any(hobby in b[2] for hobby in a[2])


# Pros: This function uses list comprehension, which is a compact way to find common hobbies. It also explicitly returns a boolean value, which can make the code clearer. Cons: It creates a new list of common hobbies, which can be inefficient for large lists. It also checks all hobbies, even if a common hobby is found early.
def friend_date3(a, b):
    """Given two friends, do they have any hobbies in common?

    - a: friend #1, a tuple of (name, age, list-of-hobbies)
    - b: same, for friend #2

    Returns True if they have any hobbies in common, False is not.

        >>> elmo = ('Elmo', 5, ['hugging', 'being nice'])
        >>> sauron = ('Sauron', 5000, ['killing hobbits', 'chess'])
        >>> gandalf = ('Gandalf', 10000, ['waving wands', 'chess'])

        >>> friend_date3(elmo, sauron)
        False

        >>> friend_date3(sauron, gandalf)
        True
    """
    common_hobbies = [hobby for hobby in a[2] if hobby in b[2]]
    return len(common_hobbies) > 0
