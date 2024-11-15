import socket
from application import app
import sys

class HttpServer:

    def __init__(self, port):
        # 1.创建套接字
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 2.设置地址重用
        #                     当前套接字            设置地址重用
        self.tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)

        # 3.绑定端口
        self.tcp_socket.bind(("", port))

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
            # 9.发送响应报文
            data = app.applications(html_data)
            new_client_socket.send(data.encode())
        new_client_socket.close()
        self.tcp_socket.close()


def main():
    # 获取控制台中的参数列表
    params = sys.argv
    if len(params) != 2:
        print("启动失败，参数格式错误! 正确格式: xxx.py xxx xxx")
        return
    if not params[1].isdigit():
        print("启动失败，端口号不是纯数字")
        return
    port = int(params[1])
    hs = HttpServer(port)
    hs.start()




if __name__ == "__main":

    main()
