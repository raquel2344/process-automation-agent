class Notifier:
    def __init__(self, notification_service):
        self.notification_service = notification_service

    def send_reminder(self, message, user, time_before_event):
        print(f"Sending reminder to {user}: {message}")
        # Simulated success
        return True
