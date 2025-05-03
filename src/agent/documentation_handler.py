from datetime import datetime

class DocumentationHandler:
    def __init__(self):
        self.documents = []

    def generate_meeting_notes(self, title, attendees, topics_discussed, action_items):
        """
        Generates meeting notes.

        Args:
          title (str): Title of the meeting.
          attendees (list): List of attendees.
          topics_discussed (list): Topics discussed in the meeting.
          action_items (list): Action items from the meeting.

        Returns:
          dict: Generated meeting notes.
        """
        notes = {
            "title": title,
            "date": datetime.now().strftime("%Y-%m-%d"),
            "attendees": attendees,
            "topics_discussed": topics_discussed,
            "action_items": action_items,
        }
        self.documents.append(notes)
        return notes
