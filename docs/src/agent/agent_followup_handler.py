class FollowUpHandler:
    def __init__(self):
        self.follow_up_logs = {}

    def create_follow_up_task(self, task_id, task_details, due_date):
        """
        Creates a follow-up task.

        Args:
          task_id (str): Unique ID for the task.
          task_details (str): Description of the follow-up task.
          due_date (datetime): Due date for the task.

        Returns:
          dict: Details of the created follow-up task.
        """
        self.follow_up_logs[task_id] = {
            "details": task_details,
            "due_date": due_date,
            "status": "pending",
        }
        return self.follow_up_logs[task_id]

    def mark_task_complete(self, task_id):
        """
        Marks a follow-up task as completed.

        Args:
          task_id (str): Unique ID for the task.

        Returns:
          dict: Updated task details.
        """
        if task_id in self.follow_up_logs:
            self.follow_up_logs[task_id]["status"] = "completed"
            return self.follow_up_logs[task_id]
        else:
            return {"error": "Task ID not found"}