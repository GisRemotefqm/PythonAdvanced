import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_socket.bind(("", 8888))

udp_socket.sendto("你好".encode("gbk"), ("127.0.0.1", 8080))
# 解包
rec_data, ip_add = udp_socket.recvfrom(1024)
print(rec_data.decode("gbk"), ip_add)

udp_socket.close()
