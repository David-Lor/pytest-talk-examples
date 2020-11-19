"""A1 - TEST with functions in module level, and testing exceptions"""

import pytest


def test_sum():
    assert 2 + 2 == 4


def test_divide():
    assert 4 / 2 == 2


@pytest.mark.skip("Don't want to run this right now!")
def test_skip():
    """This test is marked as "skip" and will not run (but shown on results)"""
    assert 2 / 0 == 0


def this_test_will_not_run():
    """All test modules (filenames) and methods (function names) must start with 'test_'"""
    assert True is False
