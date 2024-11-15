import copy


def test():
    # 浅copy只赋值最表层的数据
    a = [1, 2]
    b = ["a", "b"]
    c = [a, b]
    print("a= ", a, id(a))

    print("b= ", b, id(b))

    print("c= ", c, id(c))

    print("c[0]", c[0], id(c[0]))

    d = copy.copy(c)
    print("d= ", d, id(d))

    print("d[0] = ", d[0], id(d[0]))
    a.append(99)
    print("d= ", d, id(d))

    print("-" * 50)

    # 深拷贝底层数据也会创建新的内存空间
    d = copy.deepcopy(c)

    print("d[0] = ", d[0], id(d[0]))


if __name__ == "__main__":

    test()