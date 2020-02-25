"""A1 - TEST with functions in module level, and testing exceptions
"""

import pytest


def test_sum():
    assert 2 + 2 == 4


def test_divide():
    assert 4 / 2 == 2


def test_divide_zero():
    """This test will fail if the code inside "with pytest.raises(...)" does not raise the given exception
    """
    with pytest.raises(ZeroDivisionError):
        assert 2 / 0 == 0


@pytest.mark.skip("Don't want to run this right now!")
def test_skip():
    """This test is marked as "skip" and will not run (but shown on results)
    """
    assert 2 / 0 == 0


def this_test_will_not_run():
    """All test modules (filenames) and methods (function names) must start with "test_"
    """
    assert True is False
