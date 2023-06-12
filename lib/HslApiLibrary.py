import os
import requests
from robot.utils import DotDict
from robot.api import Error

HSL_API_URL = 'https://api.digitransit.fi/routing/v1/routers/hsl/index/graphql'


class HslApiLibrary:

    def __init__(self, url: str = HSL_API_URL) -> None:
        self.url = url
        self._create_session()

    def _create_session(self) -> None:
        self.session = requests.Session()
        apiKey = os.environ.get('HSL_API_KEY')
        if apiKey is None:
            raise Error('HSL_API_KEY environment variable is not set')
        self.session.headers.update({'digitransit-subscription-key': apiKey})

    def _check_response_status(self, response: requests.Response, expected_status: int = None) -> None:
        """ Check that response status code is either 2xx or expected_status"""
        if expected_status is None:
            response.raise_for_status()
            return

        if response.status_code != expected_status:
            message = f"Expected status code to be {expected_status} but was {response.status_code}"
            raise requests.HTTPError(message, response=response)

    def query(self, query: str, expected_status: int = None) -> DotDict:
        response = self.session.post(self.url, json={"query": f"{{{query}}}"})
        self._check_response_status(response, expected_status)
        return DotDict(response.json())
