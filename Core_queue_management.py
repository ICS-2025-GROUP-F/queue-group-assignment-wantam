import time
from typing import Optional, Dict, Any, List


class PrintQueueManager:
    def __init__(self, capacity: int = 15):
        """
        Initialize the Print Queue Manager with a circular queue.
        """
        self.capacity = capacity
        self.queue = [None] * capacity  # Circular queue array
        self.front = 0  # Index of the front element
        self.rear = -1  # Index of the rear element
        self.size = 0  # Current number of jobs in queue

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def enqueue_job(self, user_id: str, job_id: str, priority: int = 1) -> bool:
        """
        Add a new job to the queue.
        """

        if self.is_full():
            print(f"ERROR: Queue is full! Cannot add job {job_id} from user {user_id}")
            return False

        # Create job metadata dictionary
        job_data = {
            'user_id': user_id,
            'job_id': job_id,
            'priority': priority,
            'submission_time': time.time(),  # Current timestamp
            'waiting_time': 0,  # Will be updated by time management module
            'aged_priority': priority  # Will be updated by priority aging module
        }

        # Add job to circular queue
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = job_data
        self.size += 1

        print(f"SUCCESS: Job {job_id} from user {user_id} added to queue (Priority: {priority})")
        return True

    def dequeue_job(self) -> Optional[Dict[str, Any]]:
        """
        Remove and return the next job from the queue.

        Returns:
            dict: Job metadata dictionary if queue not empty, None otherwise
        """
        if self.is_empty():
            print("ERROR: Queue is empty! No jobs to dequeue")
            return None

        # Get job from front of queue
        job_data = self.queue[self.front]
        self.queue[self.front] = None  # Clear the slot
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        print(f"SUCCESS: Job {job_data['job_id']} from user {job_data['user_id']} dequeued")
        return job_data

    def peek_next_job(self) -> Optional[Dict[str, Any]]:
        """
        Look at the next job without removing it.

        Returns:
            dict: Job metadata dictionary if queue not empty, None otherwise
        """
        if self.is_empty():
            return None
        return self.queue[self.front]

    def get_queue_size(self) -> int:
        """Get the current number of jobs in the queue."""
        return self.size

    def get_available_space(self) -> int:
        """Get the number of available spaces in the queue."""
        return self.capacity - self.size

    def get_all_jobs(self) -> List[Dict[str, Any]]:
        """
        Get all jobs in the queue in their current order.

        Returns:
            list: List of job metadata dictionaries
        """
        if self.is_empty():
            return []

        jobs = []
        current_index = self.front

        for _ in range(self.size):
            jobs.append(self.queue[current_index])
            current_index = (current_index + 1) % self.capacity

        return jobs

    def show_status(self) -> None:
        """
        Display the current status of the queue.
        """
        print(f"\n=== QUEUE STATUS ===")
        print(f"Capacity: {self.capacity}")
        print(f"Current Size: {self.size}")
        print(f"Available Space: {self.get_available_space()}")
        print(f"Queue Empty: {self.is_empty()}")
        print(f"Queue Full: {self.is_full()}")

        if not self.is_empty():
            print(f"\nJobs in queue (front to rear):")
            jobs = self.get_all_jobs()
            for i, job in enumerate(jobs):
                print(f"  {i + 1}. Job {job['job_id']} (User: {job['user_id']}, Priority: {job['priority']})")
        else:
            print("No jobs in queue")
        print("=" * 20)

        #whatevs

