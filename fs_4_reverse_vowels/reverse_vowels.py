# Function 1: Using two pointers
# Pros: This function is efficient. It uses two pointers to scan s from both ends towards the middle.
# Cons: This function is longer and more complex than the other functions. It also uses a while loop, which might be less familiar to some people.
#
def reverse_vowels1(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels1("Hello!")
    'Holle!'

    >>> reverse_vowels1("Tomatoes")
    'Temotaos'

    >>> reverse_vowels1("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels1("aeiou")
    'uoiea'

    reverse_vowels1("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAEIOU"
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] not in vowels:
            i += 1
        elif s[j] not in vowels:
            j -= 1
        else:
            s[i], s[j] = s[j], s[i]
            i, j = i + 1, j - 1
    return "".join(s)


# Function 2: Using a stack
# Pros: This function is concise. It uses a stack to store the vowels in s and a generator expression to construct the result.
# Cons: This function uses additional memory to store the stack. It also scans s twice: once to fill the stack and once to construct the result.
#
def reverse_vowels2(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels2("Hello!")
    'Holle!'

    >>> reverse_vowels2("Tomatoes")
    'Temotaos'

    >>> reverse_vowels2("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels2("aeiou")
    'uoiea'

    reverse_vowels2("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiouAEIOU"
    stack = [c for c in s if c in vowels]
    return "".join(c if c not in vowels else stack.pop() for c in s)





# Function 3: Using re.sub
#Pros: This function uses regular expressions, which is a powerful tool for string manipulation.
#Cons: This function uses the re module, which might be less familiar to some people. It also uses re.findall and re.sub, which could be slower than the other methods for large strings.
#
import re
def reverse_vowels1(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels1("Hello!")
    'Holle!'

    >>> reverse_vowels1("Tomatoes")
    'Temotaos'

    >>> reverse_vowels1("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels1("aeiou")
    'uoiea'

    reverse_vowels1("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = re.findall('[aeiouAEIOU]', s)
    return re.sub('[aeiouAEIOU]', lambda m: vowels.pop(), s)
