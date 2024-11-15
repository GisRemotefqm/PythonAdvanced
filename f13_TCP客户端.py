import socket

# 创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 建立连接
tcp_socket.connect(("127.0.0.1", 8888))

# 发送数据
tcp_socket.send("你好".encode("gbk"))

# 接收数据
recv_data, ip = tcp_socket.recvfrom(1024)
text = recv_data.decode("gbk")

# 关闭连接
tcp_socket.close()