from Core_queue_management import PrintQueueManager

#Creating an instance of the queue manager
pq_manager = PrintQueueManager()

# Adding jobs
pq_manager.enqueue_job("User1", "JobA", priority=2)
pq_manager.enqueue_job("User2", "JobB", priority=1)

# Simulate time passing
pq_manager.tick()
pq_manager.tick()

# Adding another job
pq_manager.enqueue_job("User3", "JobC", priority=3)

# Show final status of the queue
pq_manager.print_queue_snapshot
