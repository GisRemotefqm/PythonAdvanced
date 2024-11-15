import threading

import time

# 多线程会导致资源竞争的问题
# work1,work2同时修改同一个值，一个抢先改完另一个来不及改
#

flag = 1

def work():

    # 要声明全局变量
    global flag
    for i in range(5000000):
        flag += 1
       # print("work,%s" % flag)
       # time.sleep(0.5)

def work_2():
    global flag
    for i in range(5000000):
        flag = flag +1
       # print("work_2,%s" % flag)



if __name__ =="__main__":

    thread_work = threading.Thread(target=work)
    thread_work_2 = threading.Thread(target=work_2)

    thread_work.start()
    # 优先让tread_work优先执行
    thread_work.join()
    thread_work_2.start()
    while True:
        if len(threading.enumerate()) == 1:
            print("主线程", flag)
            break

