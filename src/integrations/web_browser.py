import requests
from bs4 import BeautifulSoup

class WebBrowser:
    """
    A simple web browser for data collection and web scraping.
    """

    def fetch_page(self, url):
        """
        Fetches the HTML content of a web page.
        
        Args:
          url (str): The URL of the web page.

        Returns:
          str: The HTML content of the page.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            return f"Error: {str(e)}"

    def parse_html(self, html_content, element, class_name=None):
        """
        Parses HTML content to extract specific elements.
        
        Args:
          html_content (str): The HTML content.
          element (str): The HTML element to extract (e.g., 'div', 'p').
          class_name (str, optional): The class name to filter elements.

        Returns:
          list: A list of extracted elements.
        """
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            if class_name:
                return soup.find_all(element, class_=class_name)
            return soup.find_all(element)
        except Exception as e:
            return f"Error: {str(e)}"