# 生成器是一个特殊的迭代器（保存位置+返回下一个值）

list = [1, 2, 3, 4]

# 列表推导式

tuidao_list = [x*2 for x in range(10)]


# 生成器创建一

data_list = (x*2 for x in range(10))


# 生成器创建二

# 使用yield创建生成器，m是个生成器对象
def test():
    yield 10

m = test()


