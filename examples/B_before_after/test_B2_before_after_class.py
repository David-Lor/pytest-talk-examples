"""B2 - Test Before & After at Class level
Functions that run before & after all tests on the class, and before & after each test on the class.
Run with: "pytest -v -s ..." to show print output
"""


def setup_module(module):
    print("A) Setup module. Should run BEFORE any test")


def teardown_module(module):
    print("F) Teardown module. Should run AFTER all tests")


# noinspection PyMethodMayBeStatic,PyMethodParameters
class TestBeforeAfterClass:
    my_variable: str

    @classmethod
    def setup_class(cls):
        print("B) Setup module. Should run BEFORE any test of this class")
        cls.my_variable = "OK!"

    @classmethod
    def teardown_class(cls):
        print("E) Teardown module. Should run AFTER all tests of this class")

    def setup_method(method):
        print("C) Setup method. Should run BEFORE each test")

    def teardown_method(method):
        print("D) Teardown method. Should run AFTER each test")

    def test_my_variable_value(self):
        assert self.my_variable == "OK!"

    def test_my_variable_type(self):
        assert type(self.my_variable) == str
