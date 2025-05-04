import unittest
from datetime import datetime
from agent.scheduler import Scheduler

class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.scheduler = Scheduler()

    def test_schedule_meeting(self):
        title = "Team Meeting"
        start_time = datetime(2025, 5, 5, 10, 0)
        end_time = datetime(2025, 5, 5, 11, 0)
        attendees = ["test1@example.com", "test2@example.com"]
        meeting = self.scheduler.schedule_meeting(title, start_time, end_time, attendees)
        
        self.assertIn("summary", meeting)
        self.assertEqual(meeting["summary"], title)
        self.assertEqual(len(meeting["attendees"]), len(attendees))