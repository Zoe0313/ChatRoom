"""
TCP套接字客户端
重点代码
"""
import socket

# 创建tcp套接字
# 只有相同类型的套接字才能连接
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 发起连接
server_addr = ("127.0.0.1", 8888)
sockfd.connect(server_addr)

# 发送消息
while True:
    data = input("input:")
    if data == '':
        break

    # 发送消息
    try:
        print("send data:",data.encode())
        sockfd.send(data.encode())
    except BrokenPipeError:
        print("server broken pipe")
        break
    # 接收消息
    receive = sockfd.recv(1024)
    print("from server data:")
    print(receive.decode())

# 关闭套接字
sockfd.close()
