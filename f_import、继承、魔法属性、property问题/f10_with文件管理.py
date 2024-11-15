from contextlib import contextmanager


class FileRW(object):

    def __init__(self, file, rw):
        self.file = file
        self.rw = rw

    def __enter__(self):
        print("打开文件并返回")
        # 打开文件
        self.file_name = open(self.file, self.rw)
        # 返回文件资源
        return self.file_name

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("关闭文件")
        self.file_name.close()




# 使用装饰器实现上下文管理器

class FileRW_2:

    @contextmanager
    def myopen(self, file_name, rw):

        self.file_name = file_name
        self.rw = rw
        file = open(self.file_name, self.rw)

        yield file

        file.close()



if __name__ == "__main__":

    with FileRW("1.txt", "r") as file:
        data = file.read()
        print(data)

    file_rw = FileRW_2()

    with file_rw.myopen("1.txt", "r") as file:
        data = file.read()
        print(data)



