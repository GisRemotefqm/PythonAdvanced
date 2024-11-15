import threading
import time


def demo(name, age):
    for i in range(4):
        print("我的名字是%s" % name)
        print("年龄是%s" % age)
        time.sleep(1)


def cat(name, sex):
    for i in range(4):
        print("这是%s猫" % name)
        print("是%s猫" % sex)
        time.sleep(1)


if __name__ == "__main__":

    xiaoming_thread = threading.Thread(target=demo, args=("xiaoming", 14))
    xiaohua = threading.Thread(target=cat, kwargs={"name" : "xiaohua","sex" : "nv"})

    # 线程守护: 子线程守护主线程
    # 如果主线程结束了，子线程也会结束
    xiaohua.setDaemon(True)
    xiaoming_thread.setDaemon(True)

    xiaoming_thread.start()
    xiaohua.start()
    time.sleep(2)
    print("在执行")

    # 主线程主动结束
    exit()
