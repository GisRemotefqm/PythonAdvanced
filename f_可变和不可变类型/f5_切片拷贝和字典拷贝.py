import copy



def test():

    list_name = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    list2 = list_name[:]
    # 地址发生变化是深拷贝
    print("list=", list_name, id(list_name))
    print("list2=", list2, id(list2))


    dict_nm = {"name": "lisi",
               "age": 12,
               "sex": "ajdf",
               "list":[1, 2]}
    # 字典只有浅拷贝，但会创建新的内存空间，但如果字典內部有列表的可变类型，内部的值依然会根据原来进行改变
    #
    dict_2 = copy.copy(dict_nm)
    print("dict_nm =", dict_nm, id(dict_nm))
    dict_nm["age"] = 100
    dict_nm["list"][0] = 100
    print("dict_nm =", dict_nm, id(dict_nm))
    print("dict_2 =", dict_2, id(dict_2))



if __name__ == "__main__":

    test()