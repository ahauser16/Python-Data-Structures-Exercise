#Function 1: Using a for loop
#Pros: This function is straightforward and easy to understand. It uses a for loop to iterate over the indices of the matrix.
#Cons: This function uses a loop, which could be slower than a more vectorized approach for large matrices.
#
def sum_up_diagonals1(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals1(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals1(m2)
        30
    """
    total = 0
    n = len(matrix)
    for i in range(n):
        total += matrix[i][i] + matrix[i][n-i-1]
    return total
    
    
    
    
#Function 2: Using list comprehension
#Pros: This function is very concise. It uses list comprehension to sum the diagonals in a single line of code.
#Cons: This function might be a bit harder to understand for people who are not familiar with list comprehension.
#
def sum_up_diagonals2(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals2(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals2(m2)
        30
    """
    n = len(matrix)
    return sum(matrix[i][i] + matrix[i][n-i-1] for i in range(n))
    
    
    
    
#Function 3: Using numpy
#Pros: This function uses numpy, which is a powerful library for numerical computing. The np.trace function makes it easy to sum the diagonals of a matrix.
#Cons: This function requires numpy, which is an additional dependency. It also converts the matrix to a numpy array, which could use more memory than necessary for large matrices.
#
import numpy as np
def sum_up_diagonals3(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals3(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals3(m2)
        30
    """
    arr = np.array(matrix)
    return np.trace(arr) + np.trace(np.fliplr(arr))