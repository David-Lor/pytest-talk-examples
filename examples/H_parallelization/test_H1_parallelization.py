"""H1 - Run multiple tests in parallel using pytest-xdist
https://github.com/pytest-dev/pytest-xdist
"""

import pytest
from time import sleep


@pytest.mark.parametrize("time", [3, 3, 1, 2])
def test_sleep(time):
    """Parametrize 4 tests that will sleep for the given ammount of seconds.
    When running 4 parallel tests, being 3 the maximum input (sleep time),
    all tests should run in no more than ~3 seconds.
    """
    sleep(time)
