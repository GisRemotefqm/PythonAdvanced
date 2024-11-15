from collections import Iterable
# 可迭代对象使用isinstance()检测

# 列表 元组 字符串 字典 range()都可遍历即可以迭代

name_list = [1, 3, 5]
result = isinstance((name_list), Iterable)
print(result)


class demo():

    def __iter__(self):
        pass

s = demo()

# 类默认不可迭代，但对象所属的类包含了__iter__方法，那就是可迭代对象
# 可迭代对象的本质是对象所属的类中包含了__iter__方法
result = isinstance((s), Iterable)

print(result)