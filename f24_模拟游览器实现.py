import socket
# 1.创建套接字
tcp_service_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2.建立连接
tcp_service_socket.connect(("www.baidu.com", 80))
# 3.拼接请求协议
# 请求行
requst_line = "Get /HTTP/1.1\r\n"
# 请求头
request_header = "Host:www.baidu.com\r\n"
# 空行
blank = "\r\n"
# 主体

# 拼接
request_data = requst_line + request_header + blank
# 4.发送请求协议
tcp_service_socket.send(request_data.encode())
# 5.接收服务器响应内容
recv_data = tcp_service_socket.recv(4096)
recv_text = recv_data.decode()
# 6.保存内容
print(recv_data.decode())
loc = recv_data.find("\r\n\r\n")
html_data = recv_text(loc + 4)
print(html_data)
# 将网页写入文件
with open("index.html", "w") as file:
    file.write(html_data)
# 7.关闭连接
tcp_service_socket.close()