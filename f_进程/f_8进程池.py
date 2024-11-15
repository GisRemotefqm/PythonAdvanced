import multiprocessing


# 进程池是用来管理进程的
# 若进程池中有3个进程，但有四个要执行，第四个就会使用已经用完的进程
# 同步方式是顺序执行
# 异步执行是同时执行
import time


def demo():
    """
    文件拷贝
    :return:
    """

    print("正在拷贝...", multiprocessing.current_process)
    time.sleep(0.5)

def main():

    # 1.创建进程池
    pool = multiprocessing.Pool(2)

    for i in range(10):
        # 2.线程池的使用
        # pool.apply(function_name(), (a, b, c))
        # pool.apply(demo)     # 同步

        # 使用apply_async需要注意：
        # pool.close()表示不再接收新的任务
        # 主进程不再等待进程池执行结束在退出，需要进程池jion()
        pool.apply_async(demo)  # 异步
    pool.close()
    pool.join()


if __name__ == "__main__":

    main()