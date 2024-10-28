import socket
import sys

# 创建 socket 对象
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

# 等待客户端连接
while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()
    print("连接地址: ", addr)

    # 发送数据给客户端
    msg = "欢迎访问！"
    clientsocket.send(msg.encode('utf-8'))

    # 关闭客户端连接
    clientsocket.close()   
 
 