"""async tools
Perform HTTP requests to the API in https://reqres.in/, using httpx.AsyncClient.
Used by test G1
"""

import random
import httpx


async def get_async(sleep_time=None):
    if sleep_time is None:
        sleep_time = random.randint(0, 2)

    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://reqres.in/api/users?delay={sleep_time}")
        response.raise_for_status()
        return response
