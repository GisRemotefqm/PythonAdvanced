import socket

# 1.创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 设置套接字地址可以重用
# socket.SO_REUSEADDR地址是否可以重用
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
# 2.绑定端口
tcp_socket.bind(("", 8080))
# 3.设置监听
tcp_socket.listen(128)

while True:
    # 4.接受客户端连接
    new_client_socket, client_ip_socket = tcp_socket.accept()

    # 5.接收输入的文件名
    file_name = new_client_socket.recv(1024)
    print("要下载的文件是%s" % file_name.decode("gbk"))
    # 6.将文件发送给客户端
    try:
        with open(file_name.decode("gbk"), "rb") as file:
            while True:
                file_data = file.read(1024)
                if file_data is None:
                    print("读完了停止")
                    break
                else:
                    print("在执行写入%s" % file_data)
                    new_client_socket.send(file_data)
    except Exception as e:
        print("下载失败！")
    else:
        print("下载成功")
    # 7.关闭套接字
    new_client_socket.close()
tcp_socket.close()