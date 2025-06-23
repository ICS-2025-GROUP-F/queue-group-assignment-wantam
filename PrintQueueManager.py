

from datetime import datetime, timedelta

class PrintQueueManager:
    def __init__(self):
        self.queue = []  # List of dicts representing jobs
        self.expiry_seconds = 30  # Example: jobs expire after 30 seconds

    def remove_expired_jobs(self):
        current_time = datetime.now()
        updated_queue = []
        for job in self.queue:
            waiting_time = (current_time - job['submitted_at']).total_seconds()
            if waiting_time >= self.expiry_seconds:
                print(f"[EXPIRED] Job {job['job_id']} from User {job['user_id']} expired and removed.")
            else:
                updated_queue.append(job)
        self.queue = updated_queue
