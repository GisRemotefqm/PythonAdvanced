import copy

# 简单不可变类型都是浅拷贝
# 不会产生 新的空间
tuple_name = ("zhangsan", )
print(tuple_name, id(tuple_name))


tuple_name1 = copy.copy(tuple_name)
print(tuple_name1, id(tuple_name1))

# 简单类型深拷贝
# 对于不可变类型深拷贝也不会产生新的空间
tuple_name2 = copy.deepcopy(tuple_name)
print(tuple_name2, id(tuple_name2))
