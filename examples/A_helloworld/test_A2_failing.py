"""A2 - TEST with functions in module level, with failing tests"""


def test_failing_zerodivisionerror():
    2 / 0


def test_failing_compare_true_is_false():
    assert True == False


def test_failing_compare_numbers_equality():
    assert 2 == 3


def test_failing_compare_lists():
    l1 = ["A", "B", "C"]
    l2 = ["A", "C", "B"]
    assert l1 == l2
