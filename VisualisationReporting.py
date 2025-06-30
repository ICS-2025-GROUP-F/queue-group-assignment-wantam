import time

def get_queue_snapshot(self) -> list[str]:

    snapshot = []

    if self.is_empty():
        snapshot.append("Queue is empty.")
        return snapshot

    current_time = time.time()
    jobs = self.get_all_jobs()

    for job in jobs:
        waiting_time = int(current_time - job['submission_time'])
        snapshot.append(
            f"Job ID: {job['job_id']}, User: {job['user_id']}, "
            f"Aged Priority: {job['aged_priority']}, Waiting Time: {waiting_time}s"
        )

    return snapshot


def print_queue_snapshot(self):
    
    print("\n=== QUEUE SNAPSHOT ===")
    for line in self.get_queue_snapshot():
        print(line)
    print("=" * 24)
