"""F1 - Test function that will run with a set of defined parameters
https://docs.pytest.org/en/latest/parametrize.html#parametrize
"""

import pytest


@pytest.mark.parametrize("a,b,expected", [
    (2, 2, 4),
    (10, 10, 20),
    (-5, 5, 0),
    (0, 0, 0)
])
def test_sum(a, b, expected):
    result = a + b
    assert result == expected


@pytest.mark.parametrize("a,b,expected", [
    (2, 2, 4),
    (5, 5, 10),
    pytest.param(1, 1, 7, marks=pytest.mark.xfail)  # expect 1+1=7 to fail
])
def test_sum_expect_failing(a, b, expected):
    """The last given set of parameters will fail, and we expect it to fail
    """
    result = a + b
    assert result == expected
