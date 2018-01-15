# Simple Python ThreadPool

The goal of this project is to build a simple thread pool in python

Some design ideas
1) Pass callback to ThreadPool object, all threads run callback 
1a) Then what is a task? What goes in the queue? Task data/execution logic decoupled

2) Pass Task object, which encapsulates all data and running logic
2a) Seems nice actually, data/execution logic coupled
2b) User defines class which implements Task interface
2c) A pool like this can accept heterogeneous tasks. Is that ok?

Questions: 
1) What is the best way to record completed tasks? 
1a) Specifically, how can we store the payload of a completed task?
