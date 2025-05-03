from googleapiclient.discovery import build

class GoogleCalendarAPI:
    """
    Integration with the Google Calendar API for scheduling and calendar management.
    """

    def __init__(self, api_key):
        self.service = build("calendar", "v3", developerKey=api_key)

    def create_event(self, event):
        """
        Creates a calendar event.

        Args:
          event (dict): Event details (summary, start, end, etc.).

        Returns:
          dict: Created event details.
        """
        try:
            created_event = self.service.events().insert(calendarId="primary", body=event).execute()
            return created_event
        except Exception as e:
            return {"error": str(e)}

    def list_events(self, max_results=10):
        """
        Lists upcoming calendar events.

        Args:
          max_results (int): Maximum number of events to retrieve.

        Returns:
          list: List of upcoming events.
        """
        try:
            events_result = self.service.events().list(
                calendarId="primary", maxResults=max_results, singleEvents=True, orderBy="startTime"
            ).execute()
            return events_result.get('items', [])
        except Exception as e:
            return {"error": str(e)}