#!/usr/bin/python3
import sys


def factorial(n):
    """
    Calculate the factorial of a non-negative integer recursively.

    The factorial of n (written n!) is the product of all positive
    integers less than or equal to n. By definition, 0! is 1.

    Parameters:
        n (int): The non-negative integer to calculate the factorial of.

    Returns:
        int: The factorial of n.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


f = factorial(int(sys.argv[1]))
print(f)