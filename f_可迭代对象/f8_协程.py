# 协程可以暂停执行函数，就像生成器一样
# 协程的意义，对于多线程应用，cpu通过切片的方式来切换线程执行
# 线程切换需要耗时，协程则只使用一个线程，在一个线程中规定某个代码块执行顺序
# 即不开辟新线程执行多任务

# 应用场景：当程序中存在大量不需要cpu操作时（IO）
import time


def work_1():
    while True:
        print("work1正在工作...")
        yield "work1"
        time.sleep(0.5)


def work_2():
    while True:
        print("work2正在工作...")
        yield "work2"
        time.sleep(0.5)


if __name__ == "__main__":
    w1 = work_1()
    w2 = work_2()

    while True:
        next(w1)
        next(w2)