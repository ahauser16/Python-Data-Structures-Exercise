# hint: when you read lines of files, there will be a "newline"
# (end-of-line character) at the end of each line, and you want to
# strip that off before you print it. Do some research on that!


# Function 1: Using a for loop
# Pros: This function is straightforward and easy to understand. It uses a for loop to iterate over the lines in the file.
# Cons: This function uses a loop, which could be slower than a more vectorized approach for large files.
#
def read_file_list1(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list1("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """
    with open(filename, "r") as file:
        for line in file:
            print("- " + line.strip())


# Function 2: Using list comprehension
# Pros: This function is very concise. It uses list comprehension to process the lines in the file in a single line of code.
# Cons: This function might be a bit harder to understand for people who are not familiar with list comprehension.
#
def read_file_list2(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list2("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """
    with open(filename, "r") as file:
        print("\n".join("- " + line.strip() for line in file))


# Function 3: Using map
# Pros: This function uses map, which is a powerful function that applies a function to every item in a list (or any iterable). This can be more efficient than a for loop or list comprehension for large files.
# Cons: This function uses a lambda function, which might be less familiar to some people. It also uses map, which can be slower than list comprehension for small files.
#
def read_file_list3(filename):
    """Read file and print out each line separately with a "-" before it.

    For example, if we have a file, `dogs`, containing:
        Fido
        Whiskey
        Dr. Sniffle

    This should work:

        >>> read_file_list3("dogs")
        - Fido
        - Whiskey
        - Dr. Sniffle

    It will raise an error if the file cannot be found.
    """
    with open(filename, "r") as file:
        print("\n".join(map(lambda line: "- " + line.strip(), file)))
