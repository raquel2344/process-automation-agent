from flask import Flask, render_template, request, jsonify
from integrations.google_calendar import GoogleCalendarAPI
from integrations.openai_api import OpenAIAPI
from agent.followup_handler import FollowUpHandler
from agent.documentation_handler import DocumentationHandler
from agent.notifier import Notifier
from datetime import datetime, timedelta
import os

app = Flask(__name__)

# Initialize modules
google_calendar_api = GoogleCalendarAPI()
openai_api = OpenAIAPI(api_key=os.getenv("OPENAI_API_KEY"))
followup_handler = FollowUpHandler()
documentation_handler = DocumentationHandler()
notifier = Notifier(notification_service=None)  # Add a notification service as required

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/schedule", methods=["POST"])
def schedule_meeting():
    data = request.form
    title = data.get("title")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    attendees = data.get("attendees").split(",")
    
    try:
        # Schedule meeting using Google Calendar API
        event = {
            "summary": title,
            "start": {"dateTime": start_time, "timeZone": "UTC"},
            "end": {"dateTime": end_time, "timeZone": "UTC"},
            "attendees": [{"email": email.strip()} for email in attendees],
        }
        created_event = google_calendar_api.create_event(event)
        return jsonify({"message": "Meeting scheduled successfully!", "event": created_event})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/reminder", methods=["POST"])
def send_reminder():
    data = request.form
    message = data.get("message")
    user = data.get("user")
    time_before_event = int(data.get("time_before_event"))

    try:
        success = notifier.send_reminder(
            message=message,
            user=user,
            time_before_event=timedelta(minutes=time_before_event),
        )
        return jsonify({"message": "Reminder sent!" if success else "Failed to send reminder."})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/document", methods=["POST"])
def prepare_documentation():
    data = request.form
    title = data.get("title")
    attendees = data.get("attendees").split(",")
    topics_discussed = data.get("topics_discussed").split(",")
    action_items = data.get("action_items").split(",")

    try:
        notes = documentation_handler.generate_meeting_notes(
            title=title,
            attendees=attendees,
            topics_discussed=topics_discussed,
            action_items=action_items,
        )
        return jsonify({"message": "Documentation prepared successfully!", "notes": notes})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route("/followup", methods=["POST"])
def create_followup():
    data = request.form
    task_id = data.get("task_id")
    task_details = data.get("task_details")
    due_date = data.get("due_date")

    try:
        followup_task = followup_handler.create_follow_up_task(
            task_id=task_id,
            task_details=task_details,
            due_date=datetime.strptime(due_date, "%Y-%m-%d"),
        )
        return jsonify({"message": "Follow-up task created successfully!", "task": followup_task})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
