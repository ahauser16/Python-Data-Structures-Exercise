# Pros: This function is straightforward and easy to understand. It uses a dictionary comprehension to create a frequency map of vowels in phrase. This is efficient and idiomatic Python.  Cons: It calls phrase.count(v) for each vowel, which can be inefficient for large inputs. This is because count is an O(n) operation, and it's being called once for each vowel.
def vowel_count1(phrase):
    """Return frequency map of vowels, case-insensitive.

    >>> vowel_count1('rithm school')
    {'i': 1, 'o': 2}

    >>> vowel_count1('HOW ARE YOU? i am great!')
    {'a': 3, 'e': 2, 'i': 1, 'o': 2, 'u': 1}
    """
    vowels = "aeiou"
    phrase = phrase.lower()
    return {v: phrase.count(v) for v in vowels if v in phrase}

#Pros: This function is similar to the first one, but it only calls phrase.count(v) if v is in phrase. This can be more efficient for large inputs where some vowels may not be present.  Cons: It's slightly more complex than the first function due to the use of an additional variable and a for loop.
def vowel_count2(phrase):
    """Return frequency map of vowels, case-insensitive.

    >>> vowel_count2('rithm school')
    {'i': 1, 'o': 2}

    >>> vowel_count2('HOW ARE YOU? i am great!')
    {'a': 3, 'e': 2, 'i': 1, 'o': 2, 'u': 1}
    """
    vowels = "aeiou"
    phrase = phrase.lower()
    count = {}
    for v in vowels:
        if v in phrase:
            count[v] = phrase.count(v)
    return count

#Pros: This function uses a manual approach to create a frequency map of vowels in phrase, which allows for more control and potential optimizations. It only iterates over phrase once, and it only increments the count of a vowel when it encounters it. This can be more efficient for large inputs.  Cons: It's more complex than the other two functions due to the use of a loop and conditional statement. It also does not take advantage of Python's high-level features like dictionary comprehensions.
def vowel_count3(phrase):
    """Return frequency map of vowels, case-insensitive.

    >>> vowel_count3('rithm school')
    {'i': 1, 'o': 2}

    >>> vowel_count3('HOW ARE YOU? i am great!')
    {'a': 3, 'e': 2, 'i': 1, 'o': 2, 'u': 1}
    """
    vowels = "aeiou"
    phrase = phrase.lower()
    count = {v: 0 for v in vowels}
    for char in phrase:
        if char in count:
            count[char] += 1
    return {k: v for k, v in count.items() if v > 0}
