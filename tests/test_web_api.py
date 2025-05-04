import unittest
from flask import Flask
from web.app import app

class TestWebAPI(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_index_page(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Process Automation Agent", response.data)

    def test_schedule_meeting_api(self):
        payload = {
            "title": "Team Meeting",
            "start_time": "2025-05-05T10:00:00",
            "end_time": "2025-05-05T11:00:00",
            "attendees": ["test1@example.com", "test2@example.com"]
        }
        response = self.app.post("/api/schedule", json=payload)
        self.assertEqual(response.status_code, 200)
        self.assertIn("summary", response.get_json())