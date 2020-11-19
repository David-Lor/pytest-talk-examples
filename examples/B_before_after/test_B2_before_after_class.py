"""B2 - Test Before & After at Class level
Functions that run before & after all tests on the class, and before & after each test on the class.
Run with: "pytest -v -s ..." to show print output"""


def setup_module():
    print("A) Setup module. Should run BEFORE any test")


def teardown_module():
    print("F) Teardown module. Should run AFTER all tests")


class TestBeforeAfterClass:
    my_variable: str

    @classmethod
    def setup_class(cls):
        print("B) Setup class. Should run BEFORE any of the tests in this class")
        cls.my_variable = "OK!"

    @classmethod
    def teardown_class(cls):
        print("E) Teardown class. Should run AFTER all tests of this class")

    def setup_method(self):
        print("C) Setup method. Should run BEFORE each test in this class")

    def teardown_method(self):
        print("D) Teardown method. Should run AFTER each test of this class")

    def test_my_variable_value(self):
        assert self.my_variable == "OK!"

    def test_my_variable_type(self):
        assert type(self.my_variable) == str
