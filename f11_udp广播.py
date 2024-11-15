import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.bind(("", 8888))

# udp_socket.setsockopt(套接字，属性，属性值)
# SOL_SOCKET是当前套接字
# socket.SO_BROADCAST是广播属性
#设置广播权限
udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)


udp_socket.sendto("你好".encode("gbk"), ("10.240.255.255", 8080))


udp_socket.close()