from agent.scheduler import Scheduler
from agent.notifier import Notifier
from agent.followup_handler import FollowUpHandler
from agent.documentation_handler import DocumentationHandler
from integrations.google_calendar import GoogleCalendarAPI
from integrations.openai_api import OpenAIAPI

import os
from datetime import datetime, timedelta

# Load OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize integrations
google_calendar_api = GoogleCalendarAPI()  # No arguments needed now
openai_api = OpenAIAPI(api_key=OPENAI_API_KEY)

# Initialize core components
scheduler = Scheduler()
notifier = Notifier(notification_service=None)  # Replace `None` with an actual notification service implementation
followup_handler = FollowUpHandler()
documentation_handler = DocumentationHandler()

def main():
    print("Welcome to the Process Automation Agent!")
    print("Available commands: schedule, notify, followup, document, exit")

    while True:
        command = input("Enter a command: ").strip().lower()

        if command == "schedule":
            title = input("Enter meeting title: ")
            start_time = datetime.strptime(input("Enter start time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            end_time = datetime.strptime(input("Enter end time (YYYY-MM-DD HH:MM): "), "%Y-%m-%d %H:%M")
            attendees = input("Enter attendees (comma-separated emails): ").split(",")

            meeting = scheduler.schedule_meeting(
                title=title,
                start_time=start_time,
                end_time=end_time,
                attendees=attendees,
            )
            print("Meeting scheduled:", meeting)

        elif command == "notify":
            message = input("Enter reminder message: ")
            user = input("Enter user to notify: ")
            time_before_event = int(input("Enter time before event (in minutes): "))
            success = notifier.send_reminder(
                message=message,
                user=user,
                time_before_event=timedelta(minutes=time_before_event),
            )
            print("Notification sent!" if success else "Failed to send notification.")

        elif command == "followup":
            task_id = input("Enter task ID: ")
            task_details = input("Enter task details: ")
            due_date = datetime.strptime(input("Enter due date (YYYY-MM-DD): "), "%Y-%m-%d")
            followup_task = followup_handler.create_follow_up_task(
                task_id=task_id,
                task_details=task_details,
                due_date=due_date,
            )
            print("Follow-up task created:", followup_task)

        elif command == "document":
            title = input("Enter meeting title: ")
            attendees = input("Enter attendees (comma-separated): ").split(",")
            topics_discussed = input("Enter topics discussed (comma-separated): ").split(",")
            action_items = input("Enter action items (comma-separated): ").split(",")

            notes = documentation_handler.generate_meeting_notes(
                title=title,
                attendees=attendees,
                topics_discussed=topics_discussed,
                action_items=action_items,
            )
            print("Meeting notes generated:", notes)

        elif command == "exit":
            print("Exiting the Process Automation Agent. Goodbye!")
            break

        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
