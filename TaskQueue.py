from Task import Task

class TaskQueue:
    def __init__(self):
        self.q_ = []

    def push(self, task: Task):
        self.q_.push(task)

    def is_empty(self):
        return len(self.q_) == 0

    def front(self):
        if(self.is_empty()):
            return None

        return self.q_[0]

    def pop(self):
        if(self.is_empty()):
            return None

        return self.q_.pop(0)
