class PrintQueueManager:
    def __init__(self):
        self.queue = []
        self.aging_interval = 3  # After this many ticks, job gains priority

    def apply_priority_aging(self):
        """
        Increases priority of waiting jobs, resets wait time,
        then sorts by priority and wait time.
        """
        for job in self.queue:
            job["waiting_time"] += 1

            if job["waiting_time"] >= self.aging_interval:
                job["priority"] += 1
                job["waiting_time"] = 0  # Reset after aging

        # Sorts using greedy logic: best job (high priority, longest wait) comes first
        self.queue.sort(key=lambda job: (-job["priority"], -job["waiting_time"]))
