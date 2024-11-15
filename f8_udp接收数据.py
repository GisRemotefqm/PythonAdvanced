import socket

# 建立连接
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送数据 编码
udp_socket.sendto("你好".encode(encoding="gbk"), ("127.0.0.1", 8080))
# 接收数据
# udp_socket.recvfrom(接收数据的缓冲区)
# 只有当对方发送数据时才能继续向下执行，否则会一直等待
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