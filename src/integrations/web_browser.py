from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

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
                return [str(tag) for tag in soup.find_all(element, class_=class_name)]
            return [str(tag) for tag in soup.find_all(element)]
        except Exception as e:
            return f"Error: {str(e)}"

# Initialize WebBrowser instance
web_browser = WebBrowser()

@app.route("/fetch", methods=["GET"])
def fetch_page():
    """
    API endpoint to fetch the HTML content of a web page.
    """
    url = request.args.get("url")
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    html_content = web_browser.fetch_page(url)
    return jsonify({"html": html_content})

@app.route("/parse", methods=["POST"])
def parse_html():
    """
    API endpoint to parse HTML content and extract specific elements.
    """
    data = request.json
    html_content = data.get("html_content")
    element = data.get("element")
    class_name = data.get("class_name")

    if not html_content or not element:
        return jsonify({"error": "Both 'html_content' and 'element' are required"}), 400

    parsed_elements = web_browser.parse_html(html_content, element, class_name)
    return jsonify({"elements": parsed_elements})

if __name__ == "__main__":
    app.run(debug=True)
