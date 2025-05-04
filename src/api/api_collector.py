class APICollector:
    """
    Discovers and collects available APIs for integration.
    """

    def __init__(self):
        self.available_apis = {}

    def register_api(self, name, details):
        """
        Registers a new API.

        Args:
          name (str): Name of the API.
          details (dict): Details about the API (e.g., endpoint, key).

        Returns:
          bool: True if the API is registered successfully, False otherwise.
        """
        if name not in self.available_apis:
            self.available_apis[name] = details
            return True
        return False

    def list_apis(self):
        """
        Lists all registered APIs.

        Returns:
          dict: A dictionary of all registered APIs.
        """
        return self.available_apis
