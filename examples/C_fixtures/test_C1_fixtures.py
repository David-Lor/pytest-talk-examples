"""C1 - Test with Fixtures
Fixtures are functions that run before the test where used, and return something
https://docs.pytest.org/en/latest/fixture.html
"""

import random
import pytest
from pymongo import MongoClient
from pymongo.collection import Collection


@pytest.fixture
def mongo_collection():
    """This fixture will create a MongoClient instance and return a collection where we can write/read documents
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    return client["test_database"]["test_collection"]


def test_insert_read_delete(mongo_collection: Collection):
    number = random.randint(0, 1000000)
    data = {"random_number": number}

    result = mongo_collection.insert_one(data)

    read = mongo_collection.find_one({"_id": result.inserted_id})
    assert read["random_number"] == number
