
import tkinter as tk
from datetime import datetime, timedelta


class PrintQueueManager:
    def __init__(self):
        self.queue = [
            {'user_id': 'U1', 'job_id': 'J1', 'priority': 1, 'submitted_at': datetime.now() - timedelta(seconds=10)},
            {'user_id': 'U2', 'job_id': 'J2', 'priority': 2, 'submitted_at': datetime.now() - timedelta(seconds=25)},
        ]
        self.expiry_seconds = 30

    def get_queue_snapshot(self):
        snapshot = []
        now = datetime.now()
        for job in self.queue:
            waiting_time = int((now - job['submitted_at']).total_seconds())
            if waiting_time < self.expiry_seconds:
                snapshot.append(f"Job ID: {job['job_id']}, User: {job['user_id']}, "
                                f"Priority: {job['priority']}, Waiting Time: {waiting_time}s")
        return snapshot


class QueueGUI:
    def __init__(self, manager):
        self.manager = manager

        self.root = tk.Tk()
        self.root.title("Print Queue Status")

        self.title_label = tk.Label(self.root, text="Print Queue Snapshot", font=("Arial", 16))
        self.title_label.pack(pady=10)

        self.queue_display = tk.Text(self.root, height=10, width=70, font=("Courier", 12))
        self.queue_display.pack(pady=10)

        self.refresh_button = tk.Button(self.root, text="Refresh Queue", command=self.refresh)
        self.refresh_button.pack(pady=5)

        self.refresh()  # Initial display

    def refresh(self):
        self.queue_display.delete("1.0", tk.END)
        snapshot = self.manager.get_queue_snapshot()
        if not snapshot:
            self.queue_display.insert(tk.END, "Queue is empty or all jobs have expired.")
        else:
            for line in snapshot:
                self.queue_display.insert(tk.END, line + "\n")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    manager = PrintQueueManager()
    gui = QueueGUI(manager)
    gui.run()
