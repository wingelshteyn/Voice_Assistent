# import the time module
import time
import queue

# define the countdown func.
def countdown(q, t):
    time.sleep(t)
    q.put_nowait(True)
