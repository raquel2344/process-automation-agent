# Usage

## Command Line Interface (CLI)
1. **Start the Application**:
   ```bash
   python src/main.py
   ```

2. **Available Commands**:
   - `schedule`: Schedule a meeting.
   - `notify`: Send a reminder or notification.
   - `followup`: Automate follow-up tasks.
   - `document`: Generate meeting documentation.

## Web Interface
1. **Access the Web UI**:
   - Launch the application and open a browser at `http://localhost:5000`.

2. **Features**:
   - Conversational interface for scheduling and automation.
   - Intuitive design for easy navigation.

## API Endpoints
1. **Schedule a Meeting**:
   - `POST /api/schedule`
   - Payload: `{ "title": "Meeting Title", "time": "2025-05-03T10:00:00Z" }`

2. **Send a Notification**:
   - `POST /api/notify`
   - Payload: `{ "message": "Reminder message", "user": "username" }`

3. **Generate Documentation**:
   - `GET /api/document`
   - Response: `{ "status": "success", "document": "Document content" }`