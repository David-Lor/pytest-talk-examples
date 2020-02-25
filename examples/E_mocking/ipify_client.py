"""ipify client
Request the ipify API (https://www.ipify.org/), that returns our current public IP, using requests.get()
"""

import requests


def get_ip() -> str:
    response = requests.get("https://api.ipify.org/?format=raw")
    response.raise_for_status()
    return response.text.strip()
