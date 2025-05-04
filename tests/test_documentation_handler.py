import unittest
from agent.documentation_handler import DocumentationHandler

class TestDocumentationHandler(unittest.TestCase):
    def setUp(self):
        self.handler = DocumentationHandler()

    def test_generate_meeting_notes(self):
        title = "Project Kickoff"
        attendees = ["Alice", "Bob"]
        topics_discussed = ["Introduction", "Project Goals"]
        action_items = ["Assign tasks", "Set deadlines"]

        notes = self.handler.generate_meeting_notes(title, attendees, topics_discussed, action_items)
        self.assertEqual(notes["title"], title)
        self.assertEqual(len(notes["attendees"]), len(attendees))
        self.assertEqual(len(notes["topics_discussed"]), len(topics_discussed))