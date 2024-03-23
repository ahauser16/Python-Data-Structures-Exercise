# Pros: This function is straightforward and easy to understand. It uses list comprehension, which is a compact way to create a list from another list. Cons: It concatenates strings with the + operator, which can be inefficient for large strings.
def extract_full_names1(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names1(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    return [person['first'] + ' ' + person['last'] for person in people]



#Pros: This function uses the map function, which provides a high-level, efficient way to apply a function to each element in a list. It only iterates over people once. Cons: It's more complex than the first function and may be harder to understand for someone not familiar with the map function and lambda expressions.
def extract_full_names2(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names2(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    return list(map(lambda person: person['first'] + ' ' + person['last'], people))
    
    
    
    
#Pros: This function uses list comprehension, which is a compact way to create a list from another list. It also uses f-strings, which are a more efficient and readable way to concatenate strings. Cons: It's slightly more complex than the first function due to the use of f-strings. However, f-strings are generally considered more Pythonic and are recommended for string formatting.    
def extract_full_names3(people):
    """Return list of names, extracting from first+last keys in people dicts.

    - people: list of dictionaries, each with 'first' and 'last' keys for
              first and last names

    Returns list of space-separated first and last names.

        >>> names = [
        ...     {'first': 'Ada', 'last': 'Lovelace'},
        ...     {'first': 'Grace', 'last': 'Hopper'},
        ... ]

        >>> extract_full_names3(names)
        ['Ada Lovelace', 'Grace Hopper']
    """
    return [f"{person['first']} {person['last']}" for person in people]