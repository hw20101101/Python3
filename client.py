# import socket
# import sys

# # 创建 socket 对象
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # 获取本地主机名
# host = socket.gethostname()

# # 设置端口号
# port = 9999

# # 连接服务，指定主机和端口
# s.connect((host, port))

# # 接收小于 1024 字节的数据
# msg = s.recv(1024)

# s.close()

# print(msg.decode('utf-8'))


import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999
s.connect((host, port))
name = "cc"
s.send(name.encode("utf-8"))


def receive_handle(sock, addr):
    while True:
        data = sock.recv(1024)
        print(data.decode("utf-8"))

# 开启线程监听接收消息
receive_thread = threading.Thread(target=receive_handle, args=(s, '1'))
receive_thread.start()

while True:
    re_data = input()
    s.send(re_data.encode("utf-8"))