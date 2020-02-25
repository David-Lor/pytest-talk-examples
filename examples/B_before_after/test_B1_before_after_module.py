"""B1 - Test Before & After at Module level
Functions that run before & after all tests on the module, and before & after each test on the module.
Run with: "pytest -v -s ..." to show print output
"""

my_variable = None


def setup_module(module):
    global my_variable
    print("A) Setup module. Should run BEFORE any test")
    my_variable = True


def teardown_module(module):
    print("D) Teardown module. Should run AFTER all tests")


def setup_function(function):
    print("B) Setup function. Should run BEFORE each test")


def teardown_function(function):
    print("C) Teardown function. Should run AFTER each test")


def test_my_variable_is_not_none():
    assert my_variable is not None


def test_sum():
    assert 2 + 2 == 4
