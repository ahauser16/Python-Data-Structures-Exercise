# Pros: This function is straightforward and easy to understand. It uses Python's built-in string method capitalize to capitalize the first letter of the first word in phrase. Cons: It also converts the rest of the string to lowercase, which may not be desired if the input string contains uppercase letters that should be preserved.


def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

    >>> capitalize('python')
    'Python'

    >>> capitalize('only first word')
    'Only first word'
    """
    return phrase.capitalize()


# Pros: This function also preserves the case of the rest of the string. It uses list comprehension and the enumerate function to capitalize the first letter. Cons: It's more complex than the other two functions and may be harder to understand for someone not familiar with list comprehension and enumerate. It also creates a new list in memory, which can be inefficient for large inputs.

# return: This is a keyword in Python used to exit a function and return a value.

# phrase[0].upper() + phrase[1:]: This is the expression that gets returned if the condition in the if clause is true. phrase[0].upper() takes the first character of the string phrase and converts it to uppercase using the upper method. phrase[1:] is a slice that gets all characters from phrase starting from index 1 (the second character) to the end. The + operator concatenates these two parts together.

# if phrase: This is the condition of the if clause. It checks if phrase is not an empty string. In Python, an empty string is considered False in a boolean context, while a non-empty string is considered True.

# else "": This is the else clause of the conditional expression. If the condition is not met (i.e., phrase is an empty string), the function returns an empty string.

def capitalize2(phrase):
    """Capitalize first letter of first word of phrase.

    >>> capitalize2('python')
    'Python'

    >>> capitalize2('only first word')
    'Only first word'
    """
    return phrase[0].upper() + phrase[1:] if phrase else ""


#Pros: This function also preserves the case of the rest of the string. It uses list comprehension and the enumerate function to capitalize the first letter. Cons: It's more complex than the other two functions and may be harder to understand for someone not familiar with list comprehension and enumerate. It also creates a new list in memory, which can be inefficient for large inputs.

# return: This is a keyword in Python used to exit a function and return a value.

# "".join(...): This is a method call to the join method of a string object. It concatenates all the strings in the given iterable (in this case, a list comprehension), using the string it was called on (in this case, an empty string) as a separator.

# [char.upper() if i == 0 else char for i, char in enumerate(phrase)]: This is a list comprehension, which is a compact way to create a list in Python.

## char.upper() if i == 0 else char: This is a conditional expression (or ternary operator). It evaluates to char.upper() (the uppercase version of char) if i is 0 (i.e., if char is the first character of phrase), and char otherwise.

## for i, char in enumerate(phrase): This is a for loop that iterates over phrase. enumerate(phrase) returns a sequence of tuples, where the first element of each tuple is the index of the character and the second element is the character itself. i and char are variables that get assigned the values of each tuple in turn.

def capitalize3(phrase):
    """Capitalize first letter of first word of phrase.

    >>> capitalize3('python')
    'Python'

    >>> capitalize3('only first word')
    'Only first word'
    """
    return "".join([char.upper() if i == 0 else char for i, char in enumerate(phrase)])
