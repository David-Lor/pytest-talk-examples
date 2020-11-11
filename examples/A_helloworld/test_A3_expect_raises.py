"""A3 - TEST functions using pytest.raises
"""

import pytest


def test_expect_zerodivisionerror_raised():  # passes
    with pytest.raises(ZeroDivisionError):
        2 / 0


def test_expect_zerodivisionerror_not_raised():  # fails
    with pytest.raises(ZeroDivisionError):
        2 / 1


def test_expect_zerodivisionerror_raised_other():  # fails
    with pytest.raises(ZeroDivisionError):
        2 / "not a number"


def test_expect_typeerror_raised():  # passes
    with pytest.raises(TypeError):
        2 / "not a number"
