class demo:

    def __init__(self, num):
        self.num = num
        self.size = 10

    @property
    # 特殊的装饰器，可以像使用属性一样使用方法，并且必须只有一个self参数
    def start(self):
        return (self.num - 1) * self.size + 1


    
    @property
    def end(self):
        return self.num * self.size




if __name__ == "__main__":

    d = demo(10)
    print(d.start)
    print(d.end)

