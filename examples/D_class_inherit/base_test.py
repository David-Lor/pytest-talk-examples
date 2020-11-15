"""D - BASE TEST
Define a class with setup & teardown methods that will be inherited from test classes"""


class BaseTest:
    @classmethod
    def setup_class(cls):
        print("A) Setup class")

    @classmethod
    def teardown_class(cls):
        print("E) Teardown class")

    def setup_method(self):
        print("B) Setup method")

    def teardown_method(self):
        print("D) Teardown method")
