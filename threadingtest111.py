# import os

# print('Process (%s) start...' % os.getpid())
# # Only works on Unix/Linux/Mac:
# pid = os.fork()
# if pid == 0:
#     print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
#     print('I (%s) just created a child process (%s).' % (os.getpid(), pid))



# import time, threading

# # 假定这是你的银行存款:
# balance = 0

# def change_it(n):
#     print('change',threading.current_thread().name)
#     # 先存后取，结果应该为0:
#     global balance
#     balance = balance + n
#     balance = balance - n

# def run_thread(n):
#     print('run',threading.current_thread().name)
#     for i in range(10):
#         change_it(n)

# t1 = threading.Thread(target=run_thread, args=(5,))
# t2 = threading.Thread(target=run_thread, args=(8,))
# print(threading.current_thread().name)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print(balance)



# import threading
# import time
# #定义线程需要做的内容，写在函数里面
# def target():
#     print('当前的线程%s 在运行' % threading.current_thread().name)
#     time.sleep(1)
#     print('当前的线程 %s 结束' % threading.current_thread().name)

# print('当前的线程 %s 在运行' % threading.current_thread().name)
# t = threading.Thread(target=target,args = [])
 
# t.start()  #线程启动
# t.join()
# print('当前的线程 %s 结束' % threading.current_thread().name)

import time,threading

def run():
    time.sleep(2)
    print('当前线程的名字是： ', threading.current_thread().name)
    time.sleep(2)


if __name__ == '__main__':
    start_time = time.time()
    print('这是主线程：', threading.current_thread().name)
    thread_list = []

    for i in range(5):
        t = threading.Thread(target=run)
        thread_list.append(t)

    for t in thread_list:
        t.setDaemon(True)
        t.start()
        # t.join(1)

    print('主线程结束了！' , threading.current_thread().name)
    print('一共用时：', time.time()-start_time)
