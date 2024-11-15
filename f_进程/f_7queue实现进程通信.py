import multiprocessing
import time

global_num = 1

def write_demo(queue):

    global global_num
    while True:
        if queue.full():
            break
        global_num += 1
        queue.put(global_num)
        print("写入", global_num)
        time.sleep(0.5)

def read_demo(queue):

    while True:
        if queue.qsize() == False:
            break
        value = queue.get()
        print(value)
        time.sleep(0.5)

def main():
    # 1. 创建队列
    queue = multiprocessing.Queue(5)

    # 2. 创建进程
    write_process = multiprocessing.Process(target=write_demo, args=(queue, ))
    read_process = multiprocessing.Process(target=read_demo, args=(queue, ))
    write_process.start()

    # 3. 要先写入在读
    # 所以要优先让write写入再执行read的进程
    write_process.join()

    # 再读
    read_process.start()


if __name__ == "__main__":
    main()
