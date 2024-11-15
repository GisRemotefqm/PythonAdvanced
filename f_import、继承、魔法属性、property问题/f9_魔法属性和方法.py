class demo:
    """
     1. __doc__获取类、方法的描述，
     通过类名.__doc__获取;
     对象名.方法名.__doc__

     2. __module__获取当前模块；对象名.__module__

     3.__class__获取所属类; 对象名.__class__

     4. __init__是初始化方法

     5. 删除对象是会执行__del__方法

     6. __call__当创建完对象后触发

     7. __str__打印对象时触发

     8. __dict__获取对象或类的信息
    """
    num = 100
    def price(self):
        """
        用来描述价格
        """
        print("价格")

    def __del__(self):

        print("正在删除")


    def __call__(self, *args, **kwargs):

        print("__call__方法调用")

    def __str__(self):

        return "woshishui"


    def __init__(self):
        self.count = 11



    def __getitem__(self, item):
        print("key = ", item)

    def __setitem__(self, key, value):
        print("key = %s, value = %s" %(key, value))

    def __delitem__(self, key):
        print("%s被删除了" % key)


if __name__ == "__main__":

    d = demo()
    print(demo.__doc__)
    print(d.price.__doc__)
    print(demo.__module__)
    print(d.__class__)
    # 此时call方法会被调用
    d()
    print(d)
    print(d.__dict__)
    print(demo.__dict__)

    # 调用__getitem__方法
    d['see assgo']
    # 调用setitem__方法
    d['see assgo'] = 456
    # 删除某个值时调用__delitem__方法
    del d['see assgo']