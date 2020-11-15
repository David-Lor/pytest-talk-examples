"""F2 - Test function that will run with a set of defined parameters,
but some of the given parameters will fail.
https://docs.pytest.org/en/latest/parametrize.html#parametrize"""

import pytest


@pytest.mark.parametrize("a, b, expected", [
    (2, 2, 4),
    (1, 1, 7),
    (20, 1, 21),
    (-5, -5, 10)
])
def test_sum(a, b, expected):
    result = a + b
    assert result == expected
