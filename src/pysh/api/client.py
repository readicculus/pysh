from typing import Dict
import requests
import os

from .schema import ApiMethod, API_METHOD_SCHEMA

API_KEY_ENV_VAR = "PHISH_API_KEY"
API_URL = "https://api.phish.net"


def get_api_key():
    return os.environ.get(API_KEY_ENV_VAR)


class Parameters:
    def __init__(self, order_by=None, direction=None, limit=None, no_header=None, callback=None):
        self.params = {
            'order_by': order_by,
            'direction': direction,
            'limit': limit,
            'no_header': no_header,
            'callback': callback
        }

    def get_params(self) -> Dict:
        return {k: v for k, v in self.params.items() if v is not None}


class Endpoint:
    def __init__(self, base_url: str, endpoint_version: str):
        self.base_url = base_url
        self.version = endpoint_version

    def build_endpoint(self, method: ApiMethod, id: str = None, column: str = None, value: str = None,
                       fmt: str = "json", parameters=None) -> str:
        self._validate_request_schema(method, column=column, value=value, parameters=parameters)

        # Request Structure Docs: https://docs.phish.net/#requestStructure
        if id:
            # specific row in a method: /[version]/[method]/[ID].[format]
            return f"{self.base_url}/{self.version}/{method.value}/{id}.{fmt}"
        elif column and value:
            # all rows matching a query: /[version]/[method]/[column]/[value].[format]
            return f"{self.base_url}/{self.version}/{method.value}/{column}/{value}.{fmt}"
        else:
            # all data returned via a method: /[version]/[method].[format]
            return f"{self.base_url}/{self.version}/{method.value}.{fmt}"

    @staticmethod
    def _validate_request_schema(method: ApiMethod, column: str, value: str, parameters: Parameters) -> None:
        if column and not value:
            raise ValueError(f"If specifying a filter column the value must be provided and be non-empty.")
        if not column and value:
            raise ValueError(f"If specifying a filter value the column must be provided and be non-empty.")

        schema = API_METHOD_SCHEMA.get(method)
        attributes = [name.lower() for name in schema]

        if column and value:
            if column.lower() not in attributes:
                raise ValueError(f"{column.lower()} is not a valid filter column."
                                 f"Api Method {method.value} has the following attributes: {attributes}")
        if parameters and parameters.params['order_by']:
            if parameters.params['order_by'].lower() not in attributes:
                raise ValueError(f"{column.lower()} is not a valid order_by attribute."
                                 f"Api Method {method.value} has the following attributes: {attributes}")


class Client:
    def __init__(self, apikey=None):
        self._endpoint_builder = Endpoint(API_URL, "v5")
        self._api_key = apikey or get_api_key()

    def _make_request(self, endpoint, parameters: Parameters):
        params = {} if not parameters else parameters.get_params()
        params = dict({'apikey': self._api_key}, **params)
        response = requests.get(endpoint, params=params)
        if response.status_code != 200:
            error = 'HTTPError: {}'.format(response.status_code)
            return {'success': False, 'error': error}
        try:
            return response.json()['data']
        except ValueError as err:
            return {'success': False, 'error': err}

    def get_shows(self, id=None, column=None, value=None, fmt="json", parameters: Parameters = None):
        req_str = self._endpoint_builder.build_endpoint(ApiMethod.SHOWS, id=id, column=column, value=value,
                                                        fmt=fmt, parameters=parameters)
        return self._make_request(req_str, parameters)

    def get_venues(self, id=None, column=None, value=None, fmt="json", parameters: Parameters = None):
        req_str = self._endpoint_builder.build_endpoint(ApiMethod.VENUES, id=id, column=column, value=value,
                                                        fmt=fmt, parameters=parameters)
        return self._make_request(req_str, parameters)

    def get_songs(self, id=None, column=None, value=None, fmt="json", parameters: Parameters = None):
        req_str = self._endpoint_builder.build_endpoint(ApiMethod.SONGS, id=id, column=column, value=value,
                                                        fmt=fmt, parameters=parameters)
        return self._make_request(req_str, parameters)

    def get_songdata(self, id=None, column=None, value=None, fmt="json", parameters: Parameters = None):
        req_str = self._endpoint_builder.build_endpoint(ApiMethod.SONGDATA, id=id, column=column, value=value,
                                                        fmt=fmt, parameters=parameters)
        return self._make_request(req_str, parameters)

    def get_setlists(self, id=None, column=None, value=None, fmt="json", parameters: Parameters = None):
        req_str = self._endpoint_builder.build_endpoint(ApiMethod.SETLISTS, id=id, column=column, value=value,
                                                        fmt=fmt, parameters=parameters)
        return self._make_request(req_str, parameters)

    def get_artists(self, id=None, column=None, value=None, fmt="json", parameters: Parameters = None):
        req_str = self._endpoint_builder.build_endpoint(ApiMethod.ARTISTS, id=id, column=column, value=value,
                                                        fmt=fmt, parameters=parameters)
        return self._make_request(req_str, parameters)

    def get_jamcharts(self, id=None, column=None, value=None, fmt="json", parameters: Parameters = None):
        req_str = self._endpoint_builder.build_endpoint(ApiMethod.JAMCHARTS, id=id, column=column, value=value,
                                                        fmt=fmt, parameters=parameters)
        return self._make_request(req_str, parameters)
