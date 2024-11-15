import threading
import time

class MyThread(threading.Thread):

    def run(self):
        for i in range(5):
            print("打印i = %s, %s" % (i, self.name))
            time.sleep(1)


if __name__ == "__main__":
    my_thread = MyThread()
    my_thread.start()
