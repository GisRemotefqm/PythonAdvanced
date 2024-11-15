import socket
# 1.创建套接字
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2.设置地址重用
#                     当前套接字            设置地址重用
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

# 3.绑定端口
tcp_socket.bind(("", 8080))

# 4.设置监听，让套接字由主动变为被动接收
tcp_socket.listen(128)
# 5.接受客户端连接
while True:
    new_client_socket, client_ip_sport = tcp_socket.accept()
    # 6.接受客户端协议
    text_data = new_client_socket.recv(4096)
    html_data = text_data.decode()
    print(html_data)
    # 7.判断协议是否正确
    if not text_data:
        print("客户端已经断开" + client_ip_sport)
        

    # 8.拼接响应报文
    response_line = "HTTP/1.1 200 ok\r\n"
    response_header = "Servers:pythonfqm\r\n"
    response_blank = "\r\n"
    response_body = "HelloWorld"
    data = response_line + response_header + response_blank + response_body


    # 9.发送响应报文
    new_client_socket.send(data.encode())
# 10.关闭连接