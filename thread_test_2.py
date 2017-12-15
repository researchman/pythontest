import threading
import time;

exitFlag = 0;

class myThread(threading.Thread):
    def __init__(self,thread_id,name,counter):
        threading.Thread.__init__(self);
        self.thread_id = thread_id;
        self.name = name;
        self.counter = counter;
        pass

    def run(self):
        print("开始线程： " + self.name);
        print_time(self.name,self.counter,5);
        print("退出线程： " + self.name);
        pass

def print_time(thread_name,delay,counter):
    while counter:
        if exitFlag:
            thread_name.exit();
        time.sleep(delay);
        print("%s,%s"%(thread_name,time.ctime(time.time())));
        counter-=1;
    pass

#创建新线程
my1 = myThread(1,"Thread-1",1);
my2 = myThread(2,"Thread-2",2);

#开启新线程
my1.start();
my2.start();
my1.join();
my2.join();

print("退出主线程。");
