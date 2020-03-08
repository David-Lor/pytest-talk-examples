"""F4 - Test parametrizing context managers to parametrize pytest.raises
https://docs.pytest.org/en/latest/example/parametrize.html#parametrizing-conditional-raising
"""

import contextlib
import pytest


@contextlib.contextmanager
def does_not_raise():
    """empty (noop) context manager
    """
    yield


@pytest.mark.parametrize(
    "x,y,expected_context_manager,expected_result",
    [
        (4, 2, does_not_raise(), 2),
        (10, 2, does_not_raise(), 5),
        (5, 0, pytest.raises(ZeroDivisionError), None),
        ("not a number", 5, pytest.raises(TypeError), None),
    ],
)
def test_divide(x, y, expected_context_manager, expected_result):
    with expected_context_manager:
        result = x / y
        assert result == expected_result
