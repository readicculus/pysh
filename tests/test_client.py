import os
import unittest

from pysh import Client, Parameters
from pysh.api.client import Endpoint
from pysh.api.schema import ApiMethod

TEST_API_KEY = "<KEY>"
TEST_ATTRIBUTE = "attribute"
TEST_API_URL = "https://dummyapi.net"
TEST_API_VERSION = "v1"


class TestClient(unittest.TestCase):
    def test_initialize_client_with_apikey_succeeds(self):
        client = Client(TEST_API_KEY)
        self.assertEqual(client._api_key, TEST_API_KEY)

    def test_initialize_client_with_environ_succeeds(self):
        os.environ["PHISH_API_KEY"] = TEST_API_KEY
        client = Client()
        self.assertEqual(client._api_key, TEST_API_KEY)

    def test_parameters_only_returns_noneNone_parameters_succeeds(self):
        p = Parameters(order_by=TEST_ATTRIBUTE)
        r = p.get_params()
        self.assertEqual(r, {"order_by": TEST_ATTRIBUTE})

    def test_parameters_returns_all_parameters_succeeds(self):
        p = Parameters(
            order_by=TEST_ATTRIBUTE,
            direction="asc",
            limit="1",
            no_header="true",
            callback="callback",
        )
        r = p.get_params()
        self.assertEqual(
            r,
            {
                "order_by": TEST_ATTRIBUTE,
                "direction": "asc",
                "limit": "1",
                "no_header": "true",
                "callback": "callback",
            },
        )

    def test_endpoint_format_defaults_to_json_succeeds(self):
        e = Endpoint(TEST_API_URL, TEST_API_VERSION)
        r = e.build_endpoint(ApiMethod.SONGS)
        expected = f"{TEST_API_URL}/{TEST_API_VERSION}/songs.json"
        self.assertEqual(r, expected)

    def test_endpoint_validation_requires_value_if_column_fails(self):
        e = Endpoint(TEST_API_URL, TEST_API_VERSION)
        with self.assertRaises(ValueError):
            e.build_endpoint(ApiMethod.SONGS, column="test")

    def test_endpoint_validation_requires_column_if_value_fails(self):
        e = Endpoint(TEST_API_URL, TEST_API_VERSION)
        with self.assertRaises(ValueError):
            e.build_endpoint(ApiMethod.SONGS, value="test")

    def test_endpoint_column_does_not_exist_fails(self):
        e = Endpoint(TEST_API_URL, TEST_API_VERSION)
        with self.assertRaises(ValueError) as context:
            e.build_endpoint(ApiMethod.SONGS, column="badcol", value="test")
        self.assertTrue(
            "badcol is not a valid filter column. Api Method songs has the following attributes"
            in str(context.exception)
        )
