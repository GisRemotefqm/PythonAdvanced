import socket

# 1.创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.绑定端口
tcp_socket.bind("", 8080)

# 3.开启监听
tcp_socket.listen(128)
while True:
    # 4.等待连接
    new_client_socket, client_ip_sport = tcp_socket.accept()
    while True:
        # 5.接收数据
        client_data = new_client_socket.recv(1024)
        if client_data is None:
            print("客户端没有发送数据")
            print("断开连接")
            break
        print(client_data.decode("gbk"))

    # 6.关闭连接
    new_client_socket.close()
tcp_socket.close()


# 单线程不可以同时收到多个客户端的信息
