# Pros: This function is the simplest and most straightforward. It uses Python's built-in title method, which capitalizes the first letter of each word in a string.  Cons: The title method also lowercases all other characters in the word, which may not be desired if the word contains uppercase letters other than the first one.
def titleize1(phrase):
    """Return phrase in title case (each word capitalized).

    >>> titleize1('this is awesome')
    'This Is Awesome'

    >>> titleize1('oNLy cAPITALIZe fIRSt')
    'Only Capitalize First'
    """
    return phrase.title()


# Pros: This function uses a list comprehension to capitalize each word in the phrase. This is a more explicit way of doing what titleize1 does, and it allows for more control over the capitalization process.  Cons: It's slightly more complex than titleize1 due to the use of a list comprehension and the split and join methods.
def titleize2(phrase):
    """Return phrase in title case (each word capitalized).

    >>> titleize2('this is awesome')
    'This Is Awesome'

    >>> titleize2('oNLy cAPITALIZe fIRSt')
    'Only Capitalize First'
    """
    return " ".join(word.capitalize() for word in phrase.split())


# Pros: This function uses a for loop to iterate over the words in the phrase and capitalize them. This is a more manual approach that allows for more control and potential optimizations.  Cons: It's more complex than the other two functions due to the use of a loop and the split and join methods. It also modifies the words list in place, which may not be desired in some cases.
def titleize3(phrase):
    """Return phrase in title case (each word capitalized).

    >>> titleize3('this is awesome')
    'This Is Awesome'

    >>> titleize3('oNLy cAPITALIZe fIRSt')
    'Only Capitalize First'
    """
    words = phrase.split()
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    return " ".join(words)
