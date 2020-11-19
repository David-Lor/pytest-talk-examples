"""G1 - testing async code (calling async functions/methods)
https://github.com/pytest-dev/pytest-asyncio"""

import pytest
from .async_tools import get_async


@pytest.mark.asyncio
async def test_async_code():
    """Having an async test function (coroutine)"""
    response = await get_async()
    assert response.status_code == 200


def test_event_loop(event_loop):
    """Having a non-async test function, calling loop.run_until_complete
    with the "event_loop" fixture
    https://github.com/pytest-dev/pytest-asyncio#event_loop"""
    response = event_loop.run_until_complete(get_async())
    assert response.status_code == 200
