#!/usr/bin/python3
"""a method that calculates the fewest number of operations
needed to result in exactly n H characters in a file with only
a single character"""


def minOperations(n):
    """
    a method that calculates the fewest number of operations
    needed to result in exactly n H characters in a file with only
    a single character H assuming your text editor can only perform
    two operations: Copy all, Paste.
    args: n - number of characters
    return:
            the fewest number of operations needed to result in exactly n
    """
    if n <= 1:
        return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minOperations(n // i) + i
    return n
