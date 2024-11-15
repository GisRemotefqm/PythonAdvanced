import socket

# 建立连接
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定端口  自己的主机ip地址(可以省略)，要使用的端口号
udp_socket.bind(("", 60950))

# 发送数据 编码
udp_socket.sendto("快快乐乐".encode(encoding="gbk"), ("127.0.0.1", 8080))


# 接收数据
data = udp_socket.recvfrom(1024)

# 接收到的二进制格式
print(data[0])

# 解码
text = data[0].decode(encoding="gbk")
print(text)

# 向我发送的电脑的ip地址
print(data[1])

# 关闭连接
udp_socket.close()