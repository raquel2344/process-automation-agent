from googleapiclient.discovery import build
from google.oauth2.service_account import Credentials

class GoogleCalendarAPI:
    def create_event(self, event):
        print(f"Creating event: {event}")
        # Simulated response
        return {
            "id": "12345",
            "summary": event["summary"],
            "status": "confirmed",
            "start": event["start"],
            "end": event["end"]
        }
