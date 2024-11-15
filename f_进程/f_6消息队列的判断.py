import multiprocessing
import time


def main():
    queue = multiprocessing.Queue(3)

    queue.put([1, 2, 3])
    queue.put((1, ))
    queue.put(123)

    # 判断队列是否已满
    value = queue.full()
    print(value)

    # 得到消息个数
    print(queue.qsize())

    # 判断队列是否为空
    # 用赋值语句的时候queue中不为空也可能会是True
    isEmpty = queue.empty()
    print(isEmpty)

if __name__ == "__main__":
    main()