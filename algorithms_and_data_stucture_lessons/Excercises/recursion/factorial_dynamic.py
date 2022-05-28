""" The factorial code in a dynamic approach """

memory = {0: 1, 1: 1}


def factorial(n):
    """Calculates the factorial using dynamic programming.

    Args:
        n: Natural number is an input for the algorithm.
    Returns:
        factorial of numbers n.
    """
    global memory
    if n in memory:
        return memory[n]
    else:
        memory[n] = n * factorial(n - 1)
        return memory[n]


"""
    The most important difference compared to the usual recursive algorithm
    is the appearance of a structure that remembers the results of previous calls,
    here called the memory.

    If the user calls the function factorial (10),
    the result will be computed and then written into the memory dictionary.
    
    On the next call to factorial (11) (instead of calculating everything from beginning)
    the result of the equation will be returned 11*, so that the function will end quicker.
"""
