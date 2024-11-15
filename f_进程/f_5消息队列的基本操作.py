# 进程间可能需要通信，使用queue的put() 和get()
import multiprocessing
import queue
import time

def main():

    # 1.创建队列
    queue = multiprocessing.Queue(5)
    # 2.放值
    queue.put("hello")
    queue.put([1, 2, 3])
    queue.put((4, 5, 6))
    queue.put({"a": 1, "b": 2})

    # 不等待前面的资源释放，不会等待直接报错
    queue.put_nowait(2)
    # 3.取值
    data = queue.get()

    # get() 当队列已经空了，程序进入阻塞状态，等到新值进入再获取值
    print(data)

    # 当队列已经空了，不会等待直接报错
    queue.get_nowait()



if __name__ == "__main__":

    main()
