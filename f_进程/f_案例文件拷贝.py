import multiprocessing
import os
import time
"""
1，定义变量，保存源文件夹，目标文件夹所在路径
2，在目标路径创建指定文件夹
3. 获取源文件夹中的所有的文件
4， 遍历列表，得到所有的文件名
5，定义函数，进行文件拷贝
"""

def main():
    # 源文件夹
    source_dir = "./test"
    # 目标文件夹
    dest_dir = "C:/Users/fuqiming/Desktop/test"

    try:
        os.mkdir(dest_dir)
    except Exception as e:
        print("文件夹已存在")

    file_list = os.listdir(source_dir)
    print(file_list)

    # 创建进程池
    pool = multiprocessing.Pool(2)

    queue = multiprocessing.Manager().Queue(5)


    for file_name in file_list:

        pool.apply_async(copy_work, (source_dir, dest_dir, file_name))
    pool.close()
    pool.join()

def copy_work(source_dir, dest_dir, file_name):
    """
    :param source_dir:源文件路径
    :param dest_dir:目标路径
    :param file_name:文件名
    :return:
    """
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name
    print(source_path)
    print(dest_path)

    with open(source_path, "rb") as source_file:

        with open(dest_path, "wb") as dest_file:

            while True:

                # 读源文件
                file_data = source_file.read(1024)

                # 不为空写入目标文件
                if file_data != "":
                    dest_file.write(file_data)




if __name__ == "__main__":
    main()