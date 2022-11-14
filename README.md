# Python_concurrency_example
Just one-thread concurrency emulation

1) Add Task instances with Callable object inside to Dispatcher
2) Init Callable obj logic inside Task while Dispatcher runs
3) While Task is alive Dispathcer appends and pops this Task to queue
4) Stop adding Task to queue when catch StopIteration error (logical final for Task object)
5) Wait for 0-length of queue inside Dispatcher to catch IndexError and finish work
