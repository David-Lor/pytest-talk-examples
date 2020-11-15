"""C2 - Test with Yield Fixtures
Yield fixtures use the "yield" statement to return something to the test function,
but they keep running after the test (similarly to context managers).
https://pytest.readthedocs.io/en/2.9.1/yieldfixture.html
https://docs.pytest.org/en/latest/yieldfixture.html"""

import random
import pytest


@pytest.fixture
def random_number():
    """This fixture will return a random number"""
    print("A) Fixture starts")
    number = random.randint(0, 1000)
    yield number
    print("D) Fixture ends")


def test_random_number_fixture_yield(random_number):
    print("B) Test starts")
    assert type(random_number) == int
    print("C) Test ends with number", random_number)


def test_random_number_fixture_fails(random_number):
    """Even if a test fails, the fixture runs the code after the yield statement"""
    print("B) Test starts")
    assert type(random_number) == str
    print("C) Test ends (it should not reach this point!)")
