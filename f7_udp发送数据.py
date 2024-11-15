# coding = utf-8
import socket

# 创建连接
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# sendto(发送数据的二进制格式，对方IP和端口号(“IP地址”,"端口号")，)
udp_socket.sendto("你好".encode(), ("127.0.0.1", 8080))

# 关闭连接
udp_socket.close()
