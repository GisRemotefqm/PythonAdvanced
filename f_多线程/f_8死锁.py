import threading
import time

def demo(index):
    """
    :argument
    根据下标获取值
    :return:
    """

    dat_list = [1, 2, 4, 5, 6, 9]
    if index >= len(dat_list):
        print(index)
        return
    else:
        list_lock.acquire()
        print(dat_list[index])
        list_lock.release()

if __name__ == "__main__":
    list_lock = threading.Lock()

    for i in range(10):

        t1 = threading.Thread(target=demo, args=(i, ))
        t1.start()
