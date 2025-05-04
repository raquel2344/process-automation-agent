import requests

class APIManager:
    """
    Manages third-party API calls.
    """

    def __init__(self):
        self.session = requests.Session()

    def make_request(self, method, url, params=None, data=None, headers=None):
        """
        Makes an API request.

        Args:
          method (str): HTTP method (e.g., 'GET', 'POST').
          url (str): API endpoint URL.
          params (dict): Query parameters.
          data (dict): Payload for POST requests.
          headers (dict): Additional headers.

        Returns:
          Response: The response object from the API call.
        """
        try:
            response = self.session.request(
                method=method, url=url, params=params, json=data, headers=headers
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}
