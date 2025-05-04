import unittest
from datetime import datetime
from agent.followup_handler import FollowUpHandler

class TestFollowUpHandler(unittest.TestCase):
    def setUp(self):
        self.handler = FollowUpHandler()

    def test_create_follow_up_task(self):
        task_id = "task123"
        task_details = "Follow-up with client"
        due_date = datetime(2025, 5, 6)

        task = self.handler.create_follow_up_task(task_id, task_details, due_date)
        self.assertEqual(task["details"], task_details)
        self.assertEqual(task["status"], "pending")

    def test_mark_task_complete(self):
        task_id = "task123"
        self.handler.create_follow_up_task(task_id, "Sample Task", datetime(2025, 5, 6))
        updated_task = self.handler.mark_task_complete(task_id)
        self.assertEqual(updated_task["status"], "completed")