import copy

a = ("zhangsan", )
b = [1, 2, 3]
c = (a, b)

# 浅拷贝
# 浅拷贝的都不会创建新的空间
d = copy.copy(c)
print("a=", a, id(a))
print("b=", b, id(b))
print("c=", c, id(c))
print("d=", d, id(d))
b.append(4)
print("c[0]", c[0], id(c[0]))
print("c[1]", c[1], id(c[1]))

print("-"*50)

# 深拷贝
# 深拷贝时最表层会创建新的内存空间，内层不会
d = copy.deepcopy(c)
print("a=", a, id(a))
print("b=", b, id(b))
print("c=", c, id(c))
print("d=", d, id(d))
b.append(5)
print("c[0]", c[0], id(c[0]))
print("c[1]", c[1], id(c[1]))