from flask import Flask, render_template, request, jsonify
from integrations.google_calendar import GoogleCalendarAPI
from integrations.openai_api import OpenAIAPI
from agent.followup_handler import FollowUpHandler
from agent.documentation_handler import DocumentationHandler
from agent.notifier import Notifier
from datetime import datetime, timedelta
import os
import json

app = Flask(__name__)

# Initialize modules
google_calendar_api = GoogleCalendarAPI()
openai_api = OpenAIAPI(api_key=os.getenv("OPENAI_API_KEY"))
followup_handler = FollowUpHandler()
documentation_handler = DocumentationHandler()
notifier = Notifier(notification_service=None)  # Replace with an actual notification service if required

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/nlp", methods=["POST"])
def nlp_handler():
    """
    Handle natural language input from the user and execute the appropriate functionality.
    """
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input provided"}), 400

    try:
        # Use OpenAI API to parse the input
        response = openai_api.generate_response(
            prompt=f"Analyze the following command and return the intent and details:\n\n{user_input}",
            max_tokens=100,
        )

        # Parse the GPT response
        parsed_response = json.loads(response)  # Use json.loads instead of eval
        intent = parsed_response["intent"]
        details = parsed_response.get("details", {})

        # Execute the appropriate functionality based on the intent
        if intent == "schedule_meeting":
            event = {
                "summary": details["title"],
                "start": {"dateTime": details["start_time"], "timeZone": "UTC"},
                "end": {"dateTime": details["end_time"], "timeZone": "UTC"},
                "attendees": [{"email": email.strip()} for email in details["attendees"]],
            }
            created_event = google_calendar_api.create_event(event)
            return jsonify({"message": "Meeting scheduled successfully!", "event": created_event})

        elif intent == "send_reminder":
            success = notifier.send_reminder(
                message=details["message"],
                user=details["user"],
                time_before_event=timedelta(minutes=details.get("time_before_event", 10)),
            )
            return jsonify({"message": "Reminder sent!" if success else "Failed to send reminder."})

        elif intent == "prepare_documentation":
            notes = documentation_handler.generate_meeting_notes(
                title=details["title"],
                attendees=details["attendees"],
                topics_discussed=details["topics_discussed"],
                action_items=details["action_items"],
            )
            return jsonify({"message": "Documentation prepared successfully!", "notes": notes})

        elif intent == "create_followup":
            followup_task = followup_handler.create_follow_up_task(
                task_id=details["task_id"],
                task_details=details["task_details"],
                due_date=datetime
