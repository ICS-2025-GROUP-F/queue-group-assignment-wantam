import threading

def _post_init_concurrency_(self):
        """
        Optional setup method to be called after _init_ to enable locking.
        """
        self.lock = threading.Lock()

def thread_safe_enqueue_job(self, user_id: str, job_id: str, priority: int = 1) -> bool:
        """
        Wrap enqueue_job in a thread lock to ensure thread-safe execution.
        """
        with self.lock:
            return self.enqueue_job(user_id, job_id, priority)

def handle_simultaneous_submissions(self, jobs: list[tuple[str, str, int]]) -> None:
        """
        Accepts a list of (user_id, job_id, priority) tuples and submits them using threads.
        """
        threads = []
        for user_id, job_id, priority in jobs:
            thread = threading.Thread(target=self.thread_safe_enqueue_job, args=(user_id, job_id, priority))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()