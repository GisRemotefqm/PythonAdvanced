# socket 支持TCP/IP的网络通信的基本单元
# 大多数通信都是由socket完成的如qq，email

import socket
# 第一个参数是地址簇，是使用IPV4还是IPV6
# 第二个参数是类型 是TCP还是UDP
# AF_INET是IPV4，AF_INET6是IPV6
# socket.SOCK_DGRAM是udp传输方式
# socket.SOCK_STREAM是tcp传输方式

# 创建连接
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)



# 关闭连接
udp_socket.close()
