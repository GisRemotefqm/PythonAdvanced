import socket

# 1.创建套接字
tcp_service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.绑定端口和ip
tcp_service_socket.bind("", 8080)

# 3.开启监听
# listen()作用设置为被动监听模式，不能再主动发送数据
# 128 是允许的最大连接数，再linux中这个数字无效，129个也可以
tcp_service_socket.listen(128)
# 4.等待客户端连接
# 开始接收客户端连接,会返回新的套接字与客户端连接，每新连一个都会创建一个新的套接字
new_client_socket, client_ip_sport = tcp_service_socket.accept()
# 5.接收数据
text = new_client_socket.recv(1024)
print(text.decode("gbk"))

# 6.关闭连接

# 这里表示不再和当前客户端进行连接
new_client_socket.close()

tcp_service_socket.close()
