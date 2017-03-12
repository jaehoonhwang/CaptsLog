import pytest


def square(x):
    return x ** 2


def test_square():
    """Summary line.

    Extended description of function.

    Args:
        arg1 (int): Description of arg1
        arg2 (str): Description of arg2

    Returns:
        bool: Description of return value

    """
    x = [1, 2, 3, 4, 5]
    x_square = [1, 4, 9, 16, 25]

    for ind, y in enumerate(x):
        assert x_square[ind] == square(y)
