# 线程实例 - 1 ---------------------------

import _thread  #thread 模块已被废弃
import time

# 为线程定义一个函数
def print_time(threadName, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print("threadName:%s :%s" % (threadName, time.ctime(time.time())))


# 创建两个线程
try:
    _thread.start_new_thread(print_time, ("thread-1", 2))
    _thread.start_new_thread(print_time, ("thread-2", 4))
except:
    print("error: 无法启动线程")

# while 1:
#     pass


# 线程实例 - 2 ---------------------------

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(i)

# 创建线程
thread = threading.Thread(target = print_numbers)

# 启动线程
# thread.start()

# 等待线程结束
# thread.join()


# 线程实例 - 3 ---------------------------

import threading 
import time 

exitFlag = 0

class MyThread(threading.Thread):
    def __init__(self, threadId, name, delay):
        threading.Thread.__init__(self)
        self.name = name
        self.dalay = delay 

    def run(self):
        print("开始线程：" + self.name)
        print_time(self.name, self.dalay, 5)
        print("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("threadName:%s : %s" % (threadName, time.ctime(time.time())))
        counter -= 1


# 创建新线程
thread1 = MyThread(1, "thread-1", 1)
thread2 = MyThread(2, "thread-2", 2)

# 开启新线程
thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("退出主线程")