# Google Calendar Integration

## Overview
The Google Calendar API allows the `process-automation-agent` to manage scheduling and calendar events seamlessly.

## Features
1. **Meeting Scheduling**:
   - Creates, updates, and deletes calendar events.

2. **Reminders**:
   - Sends notifications for upcoming events.

3. **Recurring Events**:
   - Supports scheduling recurring meetings.

## Example API Call
```python
from googleapiclient.discovery import build

service = build("calendar", "v3", developerKey="GOOGLE_CALENDAR_API_KEY")

event = {
    "summary": "Team Meeting",
    "start": {"dateTime": "2025-05-03T10:00:00Z"},
    "end": {"dateTime": "2025-05-03T11:00:00Z"},
}

created_event = service.events().insert(calendarId="primary", body=event).execute()
print(f"Event created: {created_event['htmlLink']}")
```

## Error Handling
- Invalid API keys or permissions throw an error.
- Ensure the calendar ID is correct.