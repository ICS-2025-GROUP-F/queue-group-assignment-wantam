import time

class PrintJob:
    def __init__(self, user_id, job_id, priority, max_wait_time = 10, age_threshold = 3):
        self.user_id = user_id
        self.job_id = job_id
        self.priority = priority
        self.age = 0
        self.max_wait_time = max_wait_time
        self.age_threshold = age_threshold
        self.created_at = time.time()

    def __repr__(self):
        return f"Job({self.user_id}, {self.job_id}, P={self.priority}, Age={self.age})"

class PrintQueueManager:
    def __init__(self):
        self.queue=[]
        self.time_tick = 0

    def enqueue_job(self, user_id, job_id, priority):
        job = PrintJob(user_id, job_id, priority)
        self.queue.append(job)
        self._sort_queue()

    def tick(self):
        self.time_tick += 1
        print(f"Tick: {self.time_tick}")

        for job in self.queue:
            job.age += 1

            if job.age % job.age_threshold == 0:
                job.priority += 1
                print(f"Aged: {job.job_id} (new priority: {job.priority})")

        initial_len = len(self.queue)
        self.queue = [job for job in self.queue if job.age <= job.max_wait_time]
        expired_count = initial_len - len(self.queue)
        if expired_count:
            print(f"Removed {expired_count} expired job(s)")

            self._sort_queue()

    def _sort_queue(self):
        self.queue.sort(key = lambda job: (-job.priority, job.age))

    def show_status(self):
        print("Queue Snapshot: ")
        for job in self.queue:
            print(f"   {job}")

if __name__=="__main__":
    pq = PrintQueueManager()
    pq.enqueue_job("001", "EE", 1)
    pq.enqueue_job("002", "VET", 2)

    for _ in range(12):
        pq.tick()
        pq.show_status()
        time.sleep(0.5)