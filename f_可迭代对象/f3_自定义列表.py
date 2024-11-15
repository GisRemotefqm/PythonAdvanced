class MyList():
    def __init__(self):
        self.mylist = []

    def __iter__(self):

        iterator = MyListIterator(self.mylist)
        # 返回迭代器
        return iterator
        # 获取下一个元素的方法__next__()


    def addItem(self, data):
        self.mylist.append(data)

# 自定义迭代器类
class MyListIterator():
    def __init__(self,mylist):
        self.mylist = mylist
        self.current_index = 0
    def __iter__(self):

        pass

    def __next__(self):

        # 要判断当前下标是否越界
        if self.current_index < len(self.mylist):
        # 根据下标获取元素
            data = self.mylist[self.current_index]
        # 下标位置加一
            self.current_index += 1
            return data
        # 如果越界直接抛出异常
        else:
            raise StopIteration



if __name__ == "__main__":
    mylist = MyList()
    mylist.addItem("zhangsan")
    mylist.addItem("lisi")
    mylist.addItem("wangwu")
    for name in mylist:

        print(name)