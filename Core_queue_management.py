import time
from typing import Optional, Dict, Any, List

from priority_aging_system import apply_priority_aging
from PrintQueueManager import remove_expired_jobs
from Concurrency import _post_init_concurrency_, thread_safe_enqueue_job, handle_simultaneous_submissions
from ESTM import tick
from VisualisationReporting import get_queue_snapshot, print_queue_snapshot


class PrintQueueManager:
    def __init__(self, capacity: int = 15):
        self.capacity = capacity
        self.queue = [None] * capacity  # Circular queue
        self.front = 0
        self.rear = -1
        self.size = 0
        self.current_time = 0  # For use by tick and other time-based methods

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def enqueue_job(self, user_id: str, job_id: str, priority: int = 1) -> bool:
        if self.is_full():
            print(f"[FULL] Queue is full! Cannot add job {job_id} from user {user_id}")
            return False

        job_data = {
            'user_id': user_id,
            'job_id': job_id,
            'priority': priority,
            'submission_time': time.time(),
            'waiting_time': 0,
            'aged_priority': priority
        }

        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = job_data
        self.size += 1

        print(f"[ENQUEUE] Job {job_id} from user {user_id} added (Priority: {priority})")
        return True

    def dequeue_job(self) -> Optional[Dict[str, Any]]:
        if self.is_empty():
            print("[EMPTY] No jobs to dequeue")
            return None

        job_data = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        print(f"[DEQUEUE] Job {job_data['job_id']} from user {job_data['user_id']} removed")
        return job_data

    def peek_next_job(self) -> Optional[Dict[str, Any]]:
        if self.is_empty():
            return None
        return self.queue[self.front]

    def get_queue_size(self) -> int:
        return self.size

    def get_available_space(self) -> int:
        return self.capacity - self.size

    def get_all_jobs(self) -> List[Dict[str, Any]]:
        jobs = []
        index = self.front
        for _ in range(self.size):
            jobs.append(self.queue[index])
            index = (index + 1) % self.capacity
        return jobs

    def show_status(self) -> None:
        print("\n=== QUEUE STATUS ===")
        print(f"Capacity: {self.capacity}")
        print(f"Current Size: {self.size}")
        print(f"Available Space: {self.get_available_space()}")
        print(f"Queue Empty: {self.is_empty()}")
        print(f"Queue Full: {self.is_full()}")

        if not self.is_empty():
            print(f"\nJobs in queue (front to rear):")
            for i, job in enumerate(self.get_all_jobs(), start=1):
                print(f"  {i}. Job {job['job_id']} (User: {job['user_id']}, Priority: {job['aged_priority']}, Wait: {job['waiting_time']}s)")
        else:
            print("No jobs in queue")
        print("=" * 20)


#Attatching methods imported from other classes so they can be used in the Implemmentation file
apply_priority_aging = apply_priority_aging
remove_expired_jobs = remove_expired_jobs
_post_init_concurrency_ = _post_init_concurrency_
thread_safe_enqueue_job = thread_safe_enqueue_job
handle_simultaneous_submissions = handle_simultaneous_submissions
tick = tick
get_queue_snapshot = get_queue_snapshot
print_queue_snapshot = print_queue_snapshot