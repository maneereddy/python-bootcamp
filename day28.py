import threading
import time
def print_epoch(nameofThread,delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count+=1
        print(nameofThread,"------",time.time())
class Mythread(threading.Thread):
    def __init__(self,name,delay):
        threading.Thread.__init__(self)
        self.name = name
        self.delay = delay

    def run(self):
        print("start thread")
        print_epoch(self.name,self.delay)
        print("end thread")

t1 = Mythread("thread-1",1)
t2 = Mythread("thread-2",2)
t1.start()
t2.start()
print(t1.getName())
print(t2.getName())
print(threading.activeCount())
print(threading.currentThread())
print(threading.enumerate())
