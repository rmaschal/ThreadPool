from threading import *

class Queue:
    def __init__(self):
        self.q_ = []

    def push(self, elt):
        q_.push(elt)

    def front(self):

    def pop_front(self):

class TaskQueue(Queue):
    def __init__(self):

class ExecutorThread(Thread):
    def __init__(self, thread_id):
        self.thread_id = thread_id
        self.is_running = False

    def run(self):

    def stop(self):

class ThreadPool:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.threads = []
        self.tq_ = TaskQueue()

    def submit_task(self, task):
        self.tq_.push(task)

    def initialize(self):
        for i in range(num_threads):
            thread = ExecutorThread(i)
            self.threads.push(thread)

        for thread in threads:
            thread.start()

    def stop_threads():
        for thread in threads:
            thread.stop()

        for thread in threads:
            thread.join()
