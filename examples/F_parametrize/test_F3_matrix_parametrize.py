"""F3 - Test stacking multiple pytest.mark.parametrize decorators to create a matrix of parameters
https://docs.pytest.org/en/latest/parametrize.html#parametrize
"""

import pytest


@pytest.mark.parametrize("str1", ["That's impossible", "Ironic", "Are you threating me?"])
@pytest.mark.parametrize("str2", ["Perhaps the archives are incomplete", "I am the senate!"])
def test_join_strings(str1, str2):
    """6 tests will run (parameters of decorator 1 * parameters of decorator 2)"""
    assert "\n".join([str1, str2]) == f"{str1}\n{str2}"
