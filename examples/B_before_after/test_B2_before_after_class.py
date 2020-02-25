"""B2 - Test Before & After at Class level
Functions that run before & after all tests on the class, and before & after each test on the class.
Run with: "pytest -v -s ..." to show print output
"""


# noinspection PyMethodMayBeStatic,PyMethodParameters
class TestBeforeAfterClass:
    my_variable: str

    @classmethod
    def setup_class(cls):
        print("A) Setup module. Should run BEFORE any test")
        cls.my_variable = "OK!"

    @classmethod
    def teardown_class(cls):
        print("D) Teardown module. Should run AFTER all tests")

    def setup_method(method):
        print("B) Setup method. Should run BEFORE each test")

    def teardown_method(method):
        print("C) Teardown method. Should run AFTER each test")

    def test_my_variable_value(self):
        assert self.my_variable == "OK!"

    def test_my_variable_type(self):
        assert type(self.my_variable) == str
