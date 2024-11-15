import multiprocessing
import time


# 全局变量在进程中并不能共享全局变量的
# 子进程会复制主进程的资源到内部运行





global_num = 10

def demo(a, b):
    global global_num
    for i in range(10):
        print("doing work\n")
        global_num += 1
        print("demo---%s" % global_num)
        time.sleep(0.5)


def demo_2(a, b):
    global global_num
    for i in range(10):
        # global_num += 1
        print("demo_2---%s" % global_num)
        time.sleep(0.5)


def main():
    # 传递参数同线程
    process = multiprocessing.Process(target=demo, name="work", args=(1, 3))
    process.start()
    process = multiprocessing.Process(target=demo_2, name="work_2", args=(1, 3))
    process.start()

    time.sleep(5)
    print("mian", global_num)

if __name__ == "__main__":

    main()