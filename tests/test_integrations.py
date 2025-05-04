import unittest
from integrations.openai_api import OpenAIAPI
from integrations.google_calendar import GoogleCalendarAPI

class MockGoogleCalendarAPI:
    def create_event(self, event):
        return {"id": "1234", "summary": event["summary"]}

class TestIntegrations(unittest.TestCase):
    def setUp(self):
        self.openai_api = OpenAIAPI(api_key="mock_api_key")
        self.google_calendar_api = MockGoogleCalendarAPI()

    def test_openai_generate_response(self):
        response = self.openai_api.generate_response(prompt="Hello, how are you?", max_tokens=10)
        self.assertIsInstance(response, str)

    def test_google_calendar_create_event(self):
        event = {"summary": "Test Event"}
        created_event = self.google_calendar_api.create_event(event)
        self.assertEqual(created_event["summary"], event["summary"])