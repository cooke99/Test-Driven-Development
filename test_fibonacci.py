#!/c/Users/Development/AppData/Local/Programs/Python/Python312/python.exe
import pytest

from fibonacci import fibonacci

def test_fibonacci() -> None:
    inputs = [0, 1, 2, 3, 4, 5, 6]
    expected = [0, 1, 1, 2, 3, 5, 8]

    for idx, val in enumerate(inputs):
        assert expected[idx] == fibonacci(val)


if __name__ == "__main__":
    pytest.main()