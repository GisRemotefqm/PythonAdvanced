class demo:

    def __init__(self):
        self.price = 11
        self.discount = 0

    def set_price(self, price):
        self.price = price
        print("价格是", price)

    def get_price(self):

        return self.price

    def del_price(self):
        print("删除了!!!!")

    # 类属性
    # property(参数，参数，参数，参数)
    BAR = property(get_price, set_price, del_price, "一个类属性")
    # 当使用d.BAR是会自动调用第一个参数
    # 当d.BAR = 100时使用调用第二个参数
    # 当使用del d.BAR时会调用第三个参数
    # 当demo.BAR.__doc__,自动获取第四个参数的内容

if __name__ == "__main__":
    d = demo()

    print(d.BAR)
    d.BAR = 100
    print(d.BAR)
    del d.BAR
    print(demo.BAR.__doc__)
