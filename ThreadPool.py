from threading import *
from interface import implements, Interface
from TaskQueue import *
from Task import *

class ExecutorThread(Thread):
    def __init__(self, thread_id, condition_var, task_queue):
        self.thread_id = thread_id
        self.is_running = False
        self.cv_ = condition_var
        self.tq_ = task_queue

    def run(self):
        while is_running:
            self.cv_.acquire()
            
            while self.tw_.is_empty():
                self.cv_.wait()
            
            task = self.tq_.pop()
            self.cv_.release()
            
            task.executeTask()

    def start(self):
        is_running = True
        super(ExecutorThread, self).start()

    def stop(self):
        is_running = False

class ThreadPool:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.threads = []
        self.tq_ = TaskQueue()
        self.cv_ = threading.Condtion()

    def submit_task(self, task: Task):
        self.cv_.acquire()
        self.tq_.push(task)
        self.cv_.notify()
        self.cv_.release()

    def initialize(self):
        for i in range(num_threads):
            thread = ExecutorThread(i, self.cv_)
            self.threads.push(thread)

        for thread in threads:
            thread.start()

    def stop_threads():
        for thread in threads:
            thread.stop()

        for thread in threads:
            thread.join()
