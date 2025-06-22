import threading
import time
# I required the upper part in order to test if my concurrency control will work.It implements the enqueue_job function.
class PrintQueueManager:
    def __init__(self,capacity=10):
        self.capacity = capacity
        self.queue=[]
        self.lock=threading.Lock()


    def enqueue_job(self,user_id,job_id,priority):
        with self.lock:
            if len(self.queue)>= self.capacity:
                print(f"The queue is full.We cannot enqueue job {job_id} by {user_id}. ")


            job={ 'user_id': user_id , 'job_id': job_id, 'priority': priority, 'waiting_time': 0,}

            self.queue.append(job)
            print(f"Enqueued job {job_id} by {user_id} with a priority {priority}.")


#This function is used to handle concurrency through the use of threads
    def handle_simultaneous_submissions(self,jobs):
        #This is an empty list...keeps track of new threads

        threads=[]
        #
        for job in jobs:
          user_id,job_id,priority=job
          #args-arguments
          thread=threading.Thread(target=self.enqueue_job,args=(user_id,job_id,priority))
          threads.append(thread)#This adds the new thread to the list called threads[]..
          thread.start()#This enables execution of the function enqueue_job which is the target

        for thread in threads:
            #join() waits for all the threads to start then after it continues
            thread.join()


    def status(self):
        with self.lock:
            print("\n__Queue status__")
            for job in self.queue:
                print(f"JobId: {job['job_id']}, User: {job['user_id']},  Priority: {job['priority']},  Waiting Time: {job['waiting_time']}")
                print("____________\n")

#This is used to test if it actually works
if __name__ == "__main__":
    pq_manager = PrintQueueManager(capacity=5)

    # Simulate 3 users submitting jobs at the same time
    simultaneous_jobs = [ ("A", "Job 1", 3), ("B", "Job 2", 1),("C", "Job 3", 2),("D", "Job 4", 1),("E", "Job 5", 4),("F", "Job 6", 2)]  # This one may not enter if capacity exceeded]
#Keep in my job6 is not to show beacause we set the capacity as 5
    pq_manager.handle_simultaneous_submissions(simultaneous_jobs)
    pq_manager.status()

