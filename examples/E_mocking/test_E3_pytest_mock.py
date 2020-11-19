"""E3 - Test mocking functions with pytest-mock "mocker" fixture.
https://pypi.org/project/pytest-mock/"""

from . import calculator_client


def test_monkeypatch(mocker):
    """mocker fixture includes the same methods as mock.patch from the unittest built-in lib
    (https://docs.python.org/3/library/unittest.mock.html#patch).
    Using it as a fixture avoids having to use as context managers or decorators
    (https://github.com/pytest-dev/pytest-mock/#why-bother-with-a-plugin).
    mocker.patch can monkeypatch the given object."""
    return_value = 0

    def _mocked_divide(a, b):
        return return_value

    # the absolute module path is required, although doing relative import
    mocker.patch("E_mocking.calculator_client.divide", _mocked_divide)

    assert calculator_client.divide(10, 0) == return_value


def test_spy(mocker):
    """mocker.spy method can assert if a mocked method/function was called, with which parameters and what returns"""
    spy_calculator = mocker.spy(calculator_client, "divide")
    assert calculator_client.divide(10, 5) == 2

    spy_calculator.assert_called_once_with(10, 5)
    assert spy_calculator.spy_return == 2


def test_monkeypatch_and_spy(mocker):
    """mocker.patch and mocker.spy can be combined on the same calls"""
    return_value = 1

    def _mocked_divide(a, b):
        return return_value

    mocker.patch("E_mocking.calculator_client.divide", _mocked_divide)
    spy_calculator = mocker.spy(calculator_client, "divide")
    assert calculator_client.divide(10, 5) == return_value

    spy_calculator.assert_called_once_with(10, 5)
    assert spy_calculator.spy_return == return_value
