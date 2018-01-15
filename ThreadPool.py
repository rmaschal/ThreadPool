import time

from threading import Thread, Condition, Event
from interface import implements, Interface
from TaskQueue import *
from Task import *

class ExecutorThread(Thread):
    def __init__(self, thread_id, condition_var, task_queue, stop_event):
        super(ExecutorThread, self).__init__()
        self.thread_id = thread_id
        self.cv_ = condition_var
        self.tq_ = task_queue
        self.stop_event = stop_event

    def run(self):
        while not self.stop_event.is_set():
            self.cv_.acquire()
            
            while self.tq_.is_empty() and not self.stop_event.is_set():
                self.cv_.wait()
            
            task = self.tq_.pop()
            self.cv_.release()
            
            if task:
                task.executeTask()

    def start(self):
        self.is_running = True
        super(ExecutorThread, self).start()

class ThreadPool:
    def __init__(self, num_threads):
        self.num_threads = num_threads
        self.threads = []
        self.tq_ = TaskQueue()
        self.cv_ = Condition()
        self.stop_event = Event()

    def submit_task(self, task):
        self.cv_.acquire()
        self.tq_.append(task)
        self.cv_.notify()
        self.cv_.release()

    def initialize(self):
        for i in range(self.num_threads):
            thread = ExecutorThread(i, self.cv_, self.tq_, self.stop_event)
            self.threads.append(thread)

        for thread in self.threads:
            thread.start()

    def stop_threads(self):
        # wait for tasks to be completed
        while not self.tq_.is_empty():
            time.sleep(1)
           
        self.stop_event.set()

        # wake up threads to die
        self.cv_.acquire()
        self.cv_.notifyAll()
        self.cv_.release()

        for thread in self.threads:
            thread.join()
