# Using Python's built-in list methods append(), pop(), insert():
# This is the most straightforward and Pythonic way to manipulate a list. It uses Python's built-in list methods append(), pop(), and insert(). This method is very efficient as these operations are O(1) for adding/removing from the end and O(n) for adding/removing from the beginning.


def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """
    if command == "remove":
        if location == "end":
            return lst.pop()
        elif location == "beginning":
            return lst.pop(0)
    elif command == "add":
        if location == "end":
            lst.append(value)
            return lst
        elif location == "beginning":
            lst.insert(0, value)
            return lst


# Using a dictionary to map commands and locations to functions:
# This method uses a dictionary to map tuples of commands and locations to functions. It then looks up the function based on the command and location and calls it. This method is less intuitive than the first one, but it can be more efficient if there are many commands and locations, as it only requires one lookup in the dictionary.


def list_manipulation2(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation2(lst, 'remove', 'end')
        3

        >>> list_manipulation2(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation2(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation2(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation2(lst, 'foo', 'end') is None
        True

        >>> list_manipulation2(lst, 'add', 'dunno') is None
        True
    """
    funcs = {
        ("remove", "end"): lambda: lst.pop(),
        ("remove", "beginning"): lambda: lst.pop(0),
        ("add", "end"): lambda: lst.append(value) or lst,
        ("add", "beginning"): lambda: lst.insert(0, value) or lst,
    }
    func = funcs.get((command, location))
    return func() if func else None


# Using a loop and conditionals to check each command and location:
# This method uses a loop and conditionals to check each command and location. It is the least efficient of the three methods as it requires iterating through the commands and locations, but it can be useful in situations where the commands and locations are dynamic or need to be calculated at runtime.


def list_manipulation3(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation3(lst, 'remove', 'end')
        3

        >>> list_manipulation3(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation3(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation3(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation3(lst, 'foo', 'end') is None
        True

        >>> list_manipulation3(lst, 'add', 'dunno') is None
        True
    """
    commands = ["remove", "add"]
    locations = ["end", "beginning"]
    for cmd in commands:
        for loc in locations:
            if command == cmd and location == loc:
                if cmd == "remove":
                    return lst.pop() if loc == "end" else lst.pop(0)
                elif cmd == "add":
                    if loc == "end":
                        lst.append(value)
                        return lst
                    elif loc == "beginning":
                        lst.insert(0, value)
                        return lst
