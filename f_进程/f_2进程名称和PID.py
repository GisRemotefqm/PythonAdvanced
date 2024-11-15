import multiprocessing
import os
import time


def demo():
    for i in range(10):
        print("this work in dong")
        time.sleep(3)
        print(multiprocessing.current_process())
        print(multiprocessing.current_process().pid)
        print(os.getpid())

        # 获取子进程的父ID  parent id
        print(os.getppid())

def main():

    process = multiprocessing.Process(target=demo)
    process.start()


if __name__ == "__main__":
    # 获取当前进程名称
    print(multiprocessing.current_process())

    # 设置进程名称
    # multiprocessing.Process(name=xxx)

    # 获取当前进程ID
    print(multiprocessing.current_process().pid)

    # 使用os模块获取进程ID
    print(os.getpid())




    main()