# 迭代器就是通过迭代对象获取数据，并每次都可返回下一条数据
# 如：list—>迭代器—>获取数据
# list—>iter(可迭代对象)—>next()获取下一个元素

data = [2, 3, 4]

data_iter = iter(data)
value = next(data_iter)
print(value)