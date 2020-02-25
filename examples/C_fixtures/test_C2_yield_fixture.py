"""C2 - Test with Yield Fixtures
Yield fixtures use the "yield" statement to return something to the test function,
but they keep running after the test.
https://pytest.readthedocs.io/en/2.9.1/yieldfixture.html
https://docs.pytest.org/en/latest/yieldfixture.html
"""

import random
import pytest
from pymongo import MongoClient
from pymongo.collection import Collection


@pytest.fixture
def mongo_collection():
    """This fixture will create a MongoClient instance and return a collection where we can write and read data.
    The collection is returned with yield statement to the test.
    After test run, all documents from the collection are deleted.
    """
    client = MongoClient("mongodb://127.0.0.1:27017")
    collection = client["test_database"]["test_collection"]

    print("Returning collection to the test")
    yield collection

    # Delete all documents on collection after test run
    collection.delete_many({})
    print("Deleted all documents in Mongo test collection!")


def test_insert_read_delete(mongo_collection: Collection):
    number = random.randint(0, 1000000)
    data = {"random_number": number}

    result = mongo_collection.insert_one(data)

    read = mongo_collection.find_one({"_id": result.inserted_id})
    assert read["random_number"] == number
