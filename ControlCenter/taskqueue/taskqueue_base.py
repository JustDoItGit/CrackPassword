import threading
class taskQueue_base(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def addtask(self, task):
        self.queue.put(task)

    def run(self):
        pass
