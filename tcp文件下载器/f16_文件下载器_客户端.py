import socket

# 1.创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.建立连接
tcp_socket.connect(("127.0.0.1", 8080))

# 3.接收输入的文件名
text_name = input("请输入要下载的文件名：")

# 4.将文件名发送给服务端
tcp_socket.send(text_name.encode("gbk"))

# 5.创建文件并保存
with open("G:/python/" + text_name, "wb") as file:
    while True:
        file_data = tcp_socket.recv(1024)
        if file_data is None:
            print("没了停止")
            break
        print("正在下载")
        file.write(file_data)
# 6.接收数据，保存到本地

# 7.关闭套接字
tcp_socket.close()
