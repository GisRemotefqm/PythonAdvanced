import threading
import time


def demo(name, age):
    print("我的名字是%s" % name)
    print("年龄是%s" % age)
    time.sleep(1)


def cat(name, sex):
    print("这是%s猫" % name)
    print("是%s猫" % sex)
    time.sleep(1)


if __name__ != "__main":

    for i in range(5):
        # 线程中传递参数有三种方法
        # 1. threading.Tread(..., args = (...))
        # 2. threading.Tread(..., kwargs = {...})
        # 3. threading.Tread(..., args = (), kwargs = {})
        person = threading.Thread(target=demo, args=("小明", 17))
        hua_cat = threading.Thread(target=cat, kwargs={"name": "小花",
                                                       "sex": "女"})
        person.start()
        hua_cat.start()


    # 线程执行的顺序是由cpu决定的

