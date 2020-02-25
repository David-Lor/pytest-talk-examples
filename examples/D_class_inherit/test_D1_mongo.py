"""D1 - Test MongoDB inheriting from BaseTest class
"""

from .base_test import BaseTest


class TestMongo(BaseTest):
    def test_read_empty_collection(self):
        result = self.collection.find({})
        assert list(result) == []

    def test_insert_read_many(self):
        data_to_insert = [
            {"number": 100},
            {"number": 200},
            {"number": 300}
        ]
        self.collection.insert_many(data_to_insert)

        for read_document in self.collection.find({}):
            assert sum(
                1 for existing_document in data_to_insert
                if existing_document["number"] == read_document["number"]
            ) == 1


class TestMongoOtherCollection(BaseTest):
    """On this test class, we want to use a different collection to read/write documents from/into.
    The teardown method from the BaseTest will use the new collection instead of the BaseTest collection.
    We specify two equal tests that count how many documents exist on the collection, showing how the BaseTest
    teardown method uses the new collection name.
    """
    data_to_insert = [
        {"number": 1},
        {"number": 2},
        {"number": 3}
    ]

    @classmethod
    def setup_class(cls):
        super().setup_class()
        # Replace the collection from the BaseTest with the new collection
        cls.collection = cls.client["test_database"]["other_test_collection"]

    def test_collection_name(self):
        assert self.collection.name == "other_test_collection"

    def test_insert_read_many_1(self):
        self.collection.insert_many(self.data_to_insert)
        count_documents = self.collection.count_documents({})
        assert count_documents == len(self.data_to_insert)

    def test_insert_read_many_2(self):
        self.collection.insert_many(self.data_to_insert)
        count_documents = self.collection.count_documents({})
        assert count_documents == len(self.data_to_insert)
