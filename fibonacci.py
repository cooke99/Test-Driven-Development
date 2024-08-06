def fibonacci(n: int) -> int:
    """
    Return nth element of fibonacci sequence.
    """
    if not n:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)