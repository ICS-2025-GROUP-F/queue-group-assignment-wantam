import time

def apply_priority_aging(self, aging_interval: int = 3):
    current_time = time.time()
    for job in self.get_all_jobs():
        job['waiting_time'] = int(current_time - job['submission_time'])

        # Apply aging logic
        if job['waiting_time'] >= aging_interval:
            old_priority = job['aged_priority']
            job['aged_priority'] += 1
            print(f"[AGING] Job {job['job_id']} aged: Priority {old_priority} → {job['aged_priority']}")