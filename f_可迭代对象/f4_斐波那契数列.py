class fibnacci():

    def __init__(self, num):
        self.num = num
        # 记录位置
        self.current = 0

        # 定义斐波那契数列的第一列和第二列
        self.a = 1
        self.b = 1

    def __iter__(self):

        return self

    def __next__(self):
        # 判断类书是否超过生成的总列数
        if self.current < self.num:
            data = self.a

            self.a, self.b = self.b, self.a + self.b

            # 当前列数加一
            self.current += 1
            return data

        else:
        # 如果超出范围则报错
            raise StopIteration




if __name__ == "__main__":

    fbnc = fibnacci(9)
    value = next(fbnc)
    print(value)

    for value in fbnc:
        print(value)
