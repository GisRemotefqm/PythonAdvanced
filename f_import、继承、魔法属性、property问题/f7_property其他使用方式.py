class demo:

    def __init__(self):
        self.start = 1000
        self.discount = 1

    @property
    def test(self):
        # 返回价格
        return self.start



    @test.setter
    # setter可以设置值
    def test(self, yuanjia):
        self.start = yuanjia
        return self.start


    @test.deleter
    # deleter可是删除属性中的值
    def test(self):
        print("删除")

if __name__ == "__main__":

    d = demo(122, 0.7)
    print(d.test)
    d.test2 = 100

    del d.test3

