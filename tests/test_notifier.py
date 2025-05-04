import unittest
from datetime import timedelta
from agent.notifier import Notifier

class MockNotificationService:
    def schedule_notification(self, message, user, send_time):
        return True  # Simulate successful notification scheduling

class TestNotifier(unittest.TestCase):
    def setUp(self):
        self.notifier = Notifier(notification_service=MockNotificationService())

    def test_send_reminder(self):
        message = "This is a reminder."
        user = "test_user"
        time_before_event = timedelta(minutes=15)

        success = self.notifier.send_reminder(message, user, time_before_event)
        self.assertTrue(success)