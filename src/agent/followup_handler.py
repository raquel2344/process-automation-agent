class FollowUpHandler:
    def create_follow_up_task(self, task_id, task_details, due_date):
        print(f"Creating follow-up task: {task_id}, {task_details}, {due_date}")
        # Simulated response
        return {"task_id": task_id, "status": "created"}
