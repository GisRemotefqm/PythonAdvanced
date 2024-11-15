# greenlet模块需要安装

import greenlet from greenlet
import time

"""
1. 导入模块
2. 创建greenlet对象
3. 手动swit对象
"""
def work_1():
    while True:
        print("work1正在工作...")
        # yield "work1"
        time.sleep(0.5)

        # 切换到任务2
        g2.switch()

def work_2():
    while True:
        print("work2正在工作...")
        # yield "work2"

        time.sleep(0.5)
        g1.switch()

if __name__ == "__main__":
    g1 = greenlet(work_1)
    g2 = greenlet(work_2)

    # 执行第一个任务
    g1.switch()