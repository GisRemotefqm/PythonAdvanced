import multiprocessing
import time

global_num = 1
def read_demo(queue):
    while True:
        if queue.qsize() == False:
            break
        value = queue.get()
        print(value)
        time.sleep(0.5)

def write_demo(queue):
    global global_num
    while True:
        if queue.full():
            break
        global_num += 1
        queue.put(global_num)
        print("写入", global_num)
        time.sleep(0.5)

def main():
    # 1. 创建队列
    queue = multiprocessing.Manager().Queue(5)

    # 2. 创建进程
    pool = multiprocessing.Pool(2)


    # 同步方式
    pool.apply(write_demo, (queue, ))
    pool.apply(read_demo, (queue,))

    # 异步方式
    # apply_async()方法返回值ApplyResult对象可以返回一个wait()方法
    # wait()方法类似join(),表示当前进程执行完毕后续进程才能启动

    result = pool.apply_async(write_demo, (queue, ))
    result.wait()
    pool.apply_async(read_demo, (queue, ))

    # close()表示不再接受新的任务
    pool.close()
    # 主进程等待进程池执行结束再退出
    pool.join()

if __name__ == "__main__":

    main()