# IO多路复用select实现多客户端通信

1. 将关注的IO放入对应的监控类别列表

2. 通过select函数进行监控

3. 遍历select返回值列表,确定就绪IO事件

4. 处理发生的IO事件

#### 注意：
* wlist中如果存在IO事件,则select立即返回给ws
* 处理IO过程中不要出现死循环占有服务端的情况
* IO多路复用消耗资源较少,效率较高
