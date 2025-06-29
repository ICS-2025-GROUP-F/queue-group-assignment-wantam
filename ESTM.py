import time


def tick(self, aging_interval: int = 3, expiry_limit: int = 30):

    self.current_time += 1
    print(f"\n[TICK] System time advanced to {self.current_time}")

    ##  Updates waiting_time for all jobs
    current_real_time = time.time()
    for job in self.get_all_jobs():
        job['waiting_time'] = int(current_real_time - job['submission_time'])

    self.apply_priority_aging(aging_interval = aging_interval) ## handles increasing priority based on wait time
    self.remove_expired_jobs(expiry_limit = expiry_limit) ## Removes jobs that have waited too long

    self.show_status()