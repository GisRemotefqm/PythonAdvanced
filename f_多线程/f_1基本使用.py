import time
import threading


def sing():
    print("我在唱歌")
    time.sleep(0.5)


def song():
    print("我在跳舞")
    time.sleep(0.5)


if __name__ == "__main__":

    print(len(threading.enumerate()))
    # 创建子线程
    # 规则
    #    threading.Thread(target = 函数名)

    for i in range(5):

        t1 = threading.Thread(target=sing)
        t1.start()
        t2 = threading.Thread(target=song)
        t2.start()
        # 获取活跃的线程列表
        print(len(threading.enumerate()))
        time.sleep(0.5)


