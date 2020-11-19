"""C1 - Test with Fixtures
Fixtures are functions that run before the test where used, and can return something,
injected on the test as a function parameter.
https://docs.pytest.org/en/latest/fixture.html"""

import random
import pytest


@pytest.fixture
def random_number():
    """This fixture will return a random number"""
    print("A) Fixture runs")
    return random.randint(0, 1000)


def test_random_number_fixture(random_number):
    print("B) Test starts")
    assert type(random_number) == int
    print("C) Test ends with number", random_number)
