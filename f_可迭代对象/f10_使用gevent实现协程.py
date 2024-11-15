# gevent实现协程
# gevent可以自动识别程序中的耗时操作，在耗时操作时可以自动切换到其他任务


import gevent
from gevent import monkey
import time

def work_1():
    while True:
        print("work1正在工作...")
        yield "work1"
        # 默认情况下time.sleep不被识别为耗时操作
        # 使用monkey模块可以打补丁让time.sleep可以被识别为耗时操作
        monkey.patch_all()
        time.sleep(0.5)
        # 使用时gevent才算耗时操作
        gevent.time(0.5)

def work_2():
    while True:
        print("work2正在工作...")
        yield "work2"
        time.sleep(0.5)


if __name__ == "__main__":
    # spawn()的使用
    # gevent.spawn(function, a, b, c)
    w1 = gevent.spawn(work_1)
    w2 = gevent.spawn(work_2)


    w1.join()
    w2.join()