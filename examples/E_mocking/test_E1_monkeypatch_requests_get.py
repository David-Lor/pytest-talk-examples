"""E1 - Test monkeypatching requests.get() method manually
"""

import pytest
from requests import Response, HTTPError
from .ipify_client import get_ip

MOCKED_IP = "0.0.0.0"
"""The value the mocked API will return"""


class MockedResponse(Response):
    """The requests.Response class does not allow setting the attribute "text",
    so we create a custom inheriting class that returns the attribute "_text" when reading "text",
    by overriding the __getattribute__ magic method.
    """
    def __init__(self, text, status_code=200):
        super().__init__()
        self._text = text
        self.status_code = status_code

    def __getattribute__(self, item):
        if item == "text":
            return self._text
        else:
            return super().__getattribute__(item)


def _mocked_get_200(*args, **kwargs) -> Response:
    """We will monkeypatch the get() method from the installed requests library.
    ipify_client.get_ip() will use this mocked function instead of the original method.
    """
    return MockedResponse(text=MOCKED_IP, status_code=200)


def _mocked_get_404(*args, **kwargs) -> Response:
    """This function returns 404, thus ipify_client.get_ip() will return RequestError
    """
    return MockedResponse(text=MOCKED_IP, status_code=404)


def test_mocked_get_200(monkeypatch):
    monkeypatch.setattr("requests.get", _mocked_get_200)

    assert get_ip() == MOCKED_IP


def test_mocked_get_404(monkeypatch):
    monkeypatch.setattr("requests.get", _mocked_get_404)

    with pytest.raises(HTTPError) as error:
        get_ip()

    assert error.value.response.status_code == 404
