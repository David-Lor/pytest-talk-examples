"""E2 - Test using responses library to mock HTTP calls
https://github.com/getsentry/responses
"""

import pytest
import responses
from requests import HTTPError
from .ipify_client import get_ip

MOCKED_IP = "0.0.0.0"
"""The value the mocked API will return"""


@responses.activate
def test_mocked_http_call_with_responses_200():
    responses.add(
        method=responses.GET,
        url="https://api.ipify.org/?format=raw",
        body=MOCKED_IP,
        status=200
    )

    assert get_ip() == MOCKED_IP


@responses.activate
def test_mocked_http_call_with_responses_404():
    responses.add(
        method=responses.GET,
        url="https://api.ipify.org/?format=raw",
        body="KO",
        status=404
    )

    with pytest.raises(HTTPError) as error:
        error: HTTPError
        get_ip()
        assert error.response.status_code == 404
