class FollowUpHandler:
    def create_follow_up_task(self, task_id, task_details, due_date):
        print(f"Creating follow-up task: {task_id}, {task_details}, {due_date}")
        # Simulated response
        return {"task_id": task_id, "status": "created"}

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
