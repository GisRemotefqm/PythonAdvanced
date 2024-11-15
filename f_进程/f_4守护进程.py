import multiprocessing
import time


def demo():
    for i in range(10):
        print("hahaha")
        time.sleep(2)

def main():
    process = multiprocessing.Process(target=demo, name="demo")

    # 设置守护主进程
    process.daemon = True
    process.start()

    # 终止子线程
    process.terminate()

    time.sleep(5)
    print("....exit")


if __name__ == "__main__":
    main()
