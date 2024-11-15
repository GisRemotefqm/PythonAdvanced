# 进程是资源分配的最小单位，也是进程的容器
# 进程可以完成多任务，比如一台电脑能够同时运行多个QQ
# 线程可以完成多个任务，比如一个QQ中有多个聊天窗口

# 创建进程

import multiprocessing
import time


def demo():

    for i in range(10):
        print("doing this work")
        time.sleep(1)

def main():
    process = multiprocessing.Process(target=demo)
    process.start()

if __name__ == "__main__":


    main()
