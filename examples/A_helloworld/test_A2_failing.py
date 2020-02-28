"""A2 - TEST with functions in module level, with a failing test
"""

import pytest


def test_failing():
    assert 2 == 3


def test_failing_not_raising():
    """We expect this test to raise ZeroDivisionError, but will fail because it does not raise it (and the assert passes)
    """
    with pytest.raises(ZeroDivisionError):
        assert 2 / 2 == 1
