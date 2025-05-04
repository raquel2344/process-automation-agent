from flask import Flask, render_template, request, jsonify
from agent.scheduler import Scheduler
from agent.documentation_handler import DocumentationHandler

app = Flask(__name__)

# Initialize components
scheduler = Scheduler()
documentation_handler = DocumentationHandler()

@app.route("/")
def index():
    """
    Renders the main web interface.
    """
    return render_template("index.html")

@app.route("/api/schedule", methods=["POST"])
def schedule_meeting():
    """
    API endpoint to schedule a meeting.
    """
    data = request.get_json()
    title = data.get("title")
    start_time = data.get("start_time")
    end_time = data.get("end_time")
    attendees = data.get("attendees", [])

    # Schedule the meeting using the Scheduler component
    meeting = scheduler.schedule_meeting(title, start_time, end_time, attendees)
    return jsonify(meeting)

@app.route("/api/document", methods=["POST"])
def generate_documentation():
    """
    API endpoint to generate meeting documentation.
    """
    data = request.get_json()
    title = data.get("title")
    attendees = data.get("attendees")
    topics_discussed = data.get("topics_discussed")
    action_items = data.get("action_items")

    # Generate meeting notes using the DocumentationHandler component
    notes = documentation_handler.generate_meeting_notes(
        title, attendees, topics_discussed, action_items
    )
    return jsonify(notes)

if __name__ == "__main__":
    app.run(debug=True)