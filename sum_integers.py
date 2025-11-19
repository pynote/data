def sum_integers(n):
    """
    Returns the sum of all integers from 1 to n.
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(sum_integers(10))
