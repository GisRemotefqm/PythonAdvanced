# 浅拷贝：并没有产生新的空间，如果拷贝对象，源对象和copy对象都指向同一个内存空间，只拷贝父对象，不会拷贝对象的内部的子对象

# 使用copy.copy()

# 深拷贝：会产生新的空间，源对象和copy对象都只想不同的内存空间
# 使用copy.deepcopy()


import copy

list_name = ["zhangsan", "lisi", "wangwu"]

# 浅拷贝
list_name1 = copy.copy(list_name)
list_name3 = list_name
list_name3.append("xiaoming")
print("list_name:", list_name, id(list_name))
print("list_name1:", list_name1, id(list_name1))
print("list_name3:", list_name3, id(list_name3))
print("list_name:", list_name, id(list_name))
# 对于可变类型的变量,浅拷贝也会产生新的空间，而且会保证其独立性



print("-"*50)


# 深拷贝
list_name2 = copy.deepcopy(list_name)
print("list_name:", list_name, id(list_name))
print("list_name1:", list_name1, id(list_name1))
print("list_name2:", list_name2, id(list_name2))

# 也会产生新的空间

