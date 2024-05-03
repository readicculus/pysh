import os
import unittest

from pysh import Client

TEST_API_KEY = "<KEY>"


class TestClient(unittest.TestCase):
    def test_initialize_client_with_apikey(self):
        client = Client(TEST_API_KEY)
        self.assertEqual(client._api_key, TEST_API_KEY)

    def test_initialize_client_with_environ(self):
        os.environ["PHISH_API_KEY"] = TEST_API_KEY
        client = Client()
        self.assertEqual(client._api_key, TEST_API_KEY)
