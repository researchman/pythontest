import threading;
import time;

def thread_func(name,delay):
    count = 0;
    while count < 5:
        time.sleep(delay);
        count += 1;
        print("%s: %s" % ( name, time.ctime(time.time()) ));

try:
    td1 = threading._start_new_thread(thread_func,("thread_1",2));
    td2 = threading._start_new_thread(thread_func,("thread_2",4));
except:
    print("thread error.");

while 1:
    pass