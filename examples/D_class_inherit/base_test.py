"""D - BASE TEST
Define a class with setup & teardown methods that will be inherited from test classes
"""

from pymongo import MongoClient
from pymongo.collection import Collection


class BaseTest:
    """The BaseTest will connect to a MongoDB collection, that can be accessed with "self" from the test methods
    """

    client: MongoClient
    collection: Collection

    @classmethod
    def setup_class(cls):
        cls.client = MongoClient("mongodb://127.0.0.1:27017")
        cls.collection = cls.client["test_database"]["test_collection"]

    def teardown_method(self):
        # Delete all existing data on the collection after each test
        self.collection.delete_many({})
