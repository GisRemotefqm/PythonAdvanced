import socket
class HttpServer:
    def __init__(self):
        # 1.创建套接字
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.设置地址重用
        #                     当前套接字            设置地址重用
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        # 3.绑定端口
        self.tcp_socket.bind(("", 8080))

        # 4.设置监听，让套接字由主动变为被动接收
        self.tcp_socket.listen(128)
    def start(self):
        # 5.接受客户端连接
        while True:
            new_client_socket, client_ip_sport = self.tcp_socket.accept()
            # 6.接受客户端协议
            text_data = new_client_socket.recv(4096)
            html_data = text_data.decode()
            print(html_data)
            # 7.判断协议是否正确
            if not text_data:
                print("客户端已经断开" + client_ip_sport)
                break
            # 隔距客户端游览器请求的资源路径，返回请求资源
            # 解码，得到请求报文的字符串
            # 查找第一个/r/n，然后截取字符串（第一行中get后http前）
            loc = html_data.find("\r\n")
            request_line = html_data[:loc]
            print("请求行是%s" % request_line)
            line_list = request_line.split(" ")
            print("请求行是%s" % line_list)
            file_path = line_list[1]
            print("资源路径是fqmhtml%s" % file_path)
            # 8.拼接响应报文
            response_line = "HTTP/1.1 200 ok\r\n"
            response_header = "Servers:pythonfqm\r\n"
            response_blank = "\r\n"

            # 返回固定页面
            try:
                with open("fqmhtml" + file_path, "r") as file:
                    response_body = file.read()
            except Exception as e:
                # 修改响应行
                response_line = "HTTP/ 1.1 404 Not Found\r\n"
                response_body = response_body
            data = response_line + response_header + response_blank
            data = data + response_body
            # 9.发送响应报文
            new_client_socket.send(data.encode())
        new_client_socket.close()
        self.tcp_socket.close()


def main():
    hs = HttpServer
    hs.start()


if __name__ == "__main":

    main()




