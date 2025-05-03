from datetime import datetime, timedelta

class Notifier:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def send_reminder(self, message, user, time_before_event):
        """
        Sends a reminder to the user.

        Args:
          message (str): Reminder message.
          user (str): User to send the reminder to.
          time_before_event (timedelta): Time before the event to send the reminder.

        Returns:
          bool: True if the reminder was sent successfully, False otherwise.
        """
        send_time = datetime.now() + time_before_event
        return self.notification_service.schedule_notification(message, user, send_time)
