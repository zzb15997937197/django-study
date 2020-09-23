'''
  多线程学习
  1. 使用线程可以将把占据长时间的程序放到后台去处理。
  2. 用户界面更加吸引人，比如说用户点击了某个按钮后，可以开启多个线程去处理那个任务，可以弹出一个进度条来显示处理的进度。
  3. 多线程可以使程序执行速度更快，从而能够加快处理程序，减少内存资源的占用。

'''

'''
定义一个线程
'''
import threading


class Mythread(threading.Thread):

    def __init__(self, thread_id, name, counter):
        # 需要通过threading.Thread.__init__(self)方法来初始化线程类
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print("当前线程名称为:", self.name)


thread1 = Mythread(1, "Thread-1", 1)
thread2 = Mythread(2, "Thread-2", 2)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("退出主线程!")
