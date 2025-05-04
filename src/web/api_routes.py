from flask import Blueprint, jsonify, request
from agent.notifier import Notifier
from agent.followup_handler import FollowUpHandler

api_routes = Blueprint("api_routes", __name__)

# Initialize components
notifier = Notifier(notification_service=None)  # Replace `None` with actual notification service
followup_handler = FollowUpHandler()

@api_routes.route("/api/notify", methods=["POST"])
def send_notification():
    """
    API endpoint to send a notification.
    """
    data = request.get_json()
    message = data.get("message")
    user = data.get("user")
    time_before_event = data.get("time_before_event")

    # Send notification using the Notifier component
    success = notifier.send_reminder(message, user, time_before_event)
    return jsonify({"success": success})

@api_routes.route("/api/followup", methods=["POST"])
def create_followup():
    """
    API endpoint to create a follow-up task.
    """
    data = request.get_json()
    task_id = data.get("task_id")
    task_details = data.get("task_details")
    due_date = data.get("due_date")

    # Create follow-up task using the FollowUpHandler component
    followup_task = followup_handler.create_follow_up_task(task_id, task_details, due_date)
    return jsonify(followup_task)