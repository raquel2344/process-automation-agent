from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

class GoogleCalendarAPI:
    """
    Integration with the Google Calendar API for scheduling and calendar management.
    """

    def __init__(self):
        # Updated path to the Google service account credentials
        credentials_path = "/Users/raquel/desktop/google-credentials.json"
        
        # Load service account credentials
        credentials = Credentials.from_service_account_file(credentials_path)
        
        # Initialize the Google Calendar API service
        self.service = build("calendar", "v3", credentials=credentials)

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
