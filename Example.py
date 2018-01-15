from interface import implements
from Task import *
from ThreadPool import *
from threading import Lock


class ExampleTask(implements(Task)):
    def __init__(self, num, print_lock):
        self.num = num
        self.print_lock = print_lock
    
    def executeTask(self):
        self.print_lock.acquire()
        print("Executing task # " + str(self.num))
        self.print_lock.release()

if __name__ == "__main__":
    pool = ThreadPool(5)
    pool.initialize()
    print_lock = Lock()

    for i in range(50):
        task = ExampleTask(i, print_lock)
        pool.submit_task(task)

    pool.stop_threads()
