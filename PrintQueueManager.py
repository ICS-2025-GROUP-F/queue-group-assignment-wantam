import time

def remove_expired_jobs(self, expiry_limit: int = 30):

    current_time = time.time()
    new_queue = [None] * self.capacity
    new_front = 0
    new_rear = -1
    new_size = 0

    index = self.front
    for _ in range(self.size):
        job = self.queue[index]
        if job is not None:
            wait_time = current_time - job['submission_time']
            if wait_time >= expiry_limit:
                print(f"[EXPIRED] Job {job['job_id']} from user {job['user_id']} removed after {int(wait_time)}s")
            else:
                new_rear = (new_rear + 1) % self.capacity
                new_queue[new_rear] = job
                new_size += 1
        index = (index + 1) % self.capacity


    self.queue = new_queue
    self.front = new_front
    self.rear = new_rear
    self.size = new_size
