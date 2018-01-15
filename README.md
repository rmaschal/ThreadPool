# Simple Python ThreadPool

The goal of this project is to build a simple thread pool in python

Some design ideas
1) Pass callback to ThreadPool object, all threads run callback 
1a) Then what is a task? What goes in the queue? Task data/execution logic decoupled

2) Pask Task object, which encapsulates all data and running logic
2a) Seems nice actually, data/execution logic coupled
2b) Can inherit from base Task class, which gives interface def to ThreadPool
