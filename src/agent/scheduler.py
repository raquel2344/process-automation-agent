import datetime
from google_calendar import GoogleCalendarAPI

class Scheduler:
    def __init__(self):
        self.calendar_api = GoogleCalendarAPI()

    def schedule_meeting(self, title, start_time, end_time, attendees=[]):
        """
        Schedules a meeting using Google Calendar API.
        
        Args:
          title (str): Title of the meeting.
          start_time (datetime): Start time of the meeting.
          end_time (datetime): End time of the meeting.
          attendees (list): List of attendees' emails.

        Returns:
          dict: Details of the scheduled meeting.
        """
        event = {
            "summary": title,
            "start": {"dateTime": start_time.isoformat()},
            "end": {"dateTime": end_time.isoformat()},
            "attendees": [{"email": email} for email in attendees],
        }
        return self.calendar_api.create_event(event)
