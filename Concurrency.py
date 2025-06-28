import threading

# Global lock
lock = threading.Lock()

def _post_init_concurrency_():
    """
    Optional setup method to initialize any concurrency tools like locks.
    """
    global lock
    lock = threading.Lock()

def enqueue_job(user_id: str, job_id: str, priority: int = 1) -> bool:
    """
    Simulated enqueue logic (replace with actual logic).
    """
    print(f"Enqueued: user={user_id}, job={job_id}, priority={priority}")
    return True

def thread_safe_enqueue_job(user_id: str, job_id: str, priority: int = 1) -> bool:
    """
    Wrap enqueue_job in a thread lock to ensure thread-safe execution.
    """
    with lock:
        return enqueue_job(user_id, job_id, priority)

def handle_simultaneous_submissions(jobs: list[tuple[str, str, int]]) -> None:
    """
    Accepts a list of (user_id, job_id, priority) tuples and submits them using threads.
    """
    threads = []
    for user_id, job_id, priority in jobs:
        thread = threading.Thread(target=thread_safe_enqueue_job, args=(user_id, job_id, priority))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
