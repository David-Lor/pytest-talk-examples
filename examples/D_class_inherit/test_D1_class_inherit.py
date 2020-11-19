"""D1 - Test class-defined test inheriting from BaseTest"""

from .base_test import BaseTest


class TestMain(BaseTest):
    def test_class_1(self):
        print("C) Inside test class method")

    def test_class_2(self):
        print("C) Inside test class method")
