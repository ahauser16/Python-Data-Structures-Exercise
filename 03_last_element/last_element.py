def last_element(lst):
    """Return last item in list (None if list is empty.
    
        >>> last_element([1, 2, 3])
        3
        
        >>> last_element([]) is None
        True
    """
    return lst[-1] if lst else None

# def last_element(lst):
#     """Return last item in list (None if list is empty).
#     """
#     return lst[len(lst)-1] if lst else None

# This method also uses indexing, but it first calculates the length of the list with the len() function. This is less efficient than the first method because len() is O(n), where n is the length of the list.

# def last_element(lst):
#     """Return last item in list (None if list is empty).
#     """
#     last_item = None
#     for item in lst:
#         last_item = item
#     return last_item

# This method uses a loop to iterate through all the elements in the list and keeps updating last_item with the current item. At the end of the loop, last_item will be the last item in the list. This method is the least efficient of the three because it requires iterating through the entire list, which is O(n). However, it can be useful in situations where you need to do something with each item in the list as you iterate through it.