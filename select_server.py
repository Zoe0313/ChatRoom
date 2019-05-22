"""
IO多路复用select实现多客户端通信
重点代码

【1】将关注的IO放入对应的监控类别列表
【2】通过select函数进行监控
【3】遍历select返回值列表,确定就绪IO事件
【4】处理发生的IO事件

注意：
    wlist中如果存在IO事件,则select立即返回给ws
    处理IO过程中不要出现死循环占有服务端的情况
    IO多路复用消耗资源较少,效率较高
"""

import socket
import select

# 设置套接字为关注IO
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 8888))
s.listen(5)

# 设置关注的IO
rlist = [s]
wlist = []
xlist = []

while True:
    # 监控IO的发生
    rs, ws, xs = select.select(rlist, wlist, xlist)
    # 遍历三个返回值列表，判断那个IO发生
    for r in rs:
        if r is s:  # 如果套接字s准备就绪则处理客户端连接
            c, addr = r.accept()
            print("Connect from:", addr)
            rlist.append(c)  # 加入新的关注IO
        else:# 如果套接字c准备就绪则处理客户端消息
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data.decode())
            #主动处理这个IO
            wlist.append(r)
    for w in ws:
        w.send(b'OK')
        wlist.remove(w)
    for x in xs:
        pass
