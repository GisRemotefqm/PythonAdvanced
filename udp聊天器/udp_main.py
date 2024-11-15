import socket

def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(("", 8888))
    while True:
        print("*"*50)
        print("\t\t\t\tudp聊天器\t\t")
        print("1.发送信息\t\t2.接收信息\t\t3.退出")
        num = int(input("请输入功能:"))

        if num == 1:
            print("进入第一个功能")
            send_msg(udp_socket)

        elif num == 2:
            print("进入第二个功能")
            recv_msg(udp_socket)
        elif num == 3:
            break
        else:
            print("输入的内容错误请重新输入")
    udp_socket.close()

def send_msg(udp_socket):
    """发送信息的函数"""
    ip_add = input("请输入对方ip地址：")
    port = input("请输入对方接收的端口号：")
    text = input("请输入要发送的内容：")
    udp_socket.sendto(text.encode("gbk"), (ip_add, int(port)))


def recv_msg(udp_socket):
    """接收数据的函数
    udp_socket:param 套接字
    """

    text_data, ip = udp_socket.recvfrom(1024)
    print(text_data.decode("gbk"))
    print(ip)


if __name__ == "__main__":
    main()
