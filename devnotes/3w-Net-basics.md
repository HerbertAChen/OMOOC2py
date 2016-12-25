## 网络编程 ：一些基本知识
主要针对3w任务用到的UDP协议

### 0 问题

C/S如何传输信息，什么是UDP、socket，如何用python实现？
>首先先明确如何进行网络开发?
什么是  UDP 协议?
用 Python 完成一对最简单的 UDP 服务器/客户端?

### 1 关于互联网协议
 
参考：
* 阮一峰：[互联网协议入门（一）](http://www.ruanyifeng.com/blog/2012/05/internet_protocol_suite_part_i.html)
* [互联网协议入门（二）](http://www.ruanyifeng.com/blog/2012/06/internet_protocol_suite_part_ii.html)
 
#### 五个层次
* 实体层
* 链接层
    - 以太网(Ethernet)协议
    - 以太网数据包叫做 帧（Frame），包含Head和data
        - Head 包含发送者、接受者、数据类型等信息，长度 18 字节
        - data 长度 46~1500 字节
    - MAC地址：12个16进制数，用来识别设备
    - 广播 broadcasting
* 网络层
    - 互联网由无数个子网络组成
    - 主机到主机的通信
    - IP协议：IP地址，子网掩码
    - IP数据包：总长度最大 65535 字节，常常分隔成多个以太网数据包
    - ARP协议：由IP地址获取MAC地址
* 传输层
    - 端口到端口的通信，每个端口对应一个程序
    - Unix系统就把主机+端口，叫做"套接字"（socket）
    - 在数据包中加入端口信息需要新的协议
        + UDP协议：最简单，加一个8字节的端口号信息
        + TCP协议：可以简单理解为，有确认机制的UDP协议
            * 能够确保数据不会遗失
            * 缺点是过程复杂、实现困难、消耗较多的资源
* 应用层
    - 规定应用程序的数据格式
 
![data](img/internet-data.png)

更多资料：
* [Introduction to the Internet Protocols](http://www.uic.edu/depts/accc/network/ftp/v452.html)
 
#### 用户角度的实现
* 上网设置
    - 四个参数：本机IP，子网掩码，网关IP，DNS IP
    - 静态IP
    - 动态IP：
        + DHCP协议
* 一个实例：访问网页
 
### 2 进一步了解 socket、UDP
2.1 [Socket Programming HOWTO](https://docs.python.org/2/howto/sockets.html)
* this doc only talks about: INET sockets, STREAM socket
* blocking and non-blocking sockets
* “client” socket vs. “server” socket
    * a “client” socket: an endpoint of a conversation
    * a “server” socket: more like a switchboard operator
    * The client application uses “client” sockets exclusively; the web server it’s talking to uses both “server” sockets and “client” sockets.
 
2.2 廖雪峰：[TCP 编程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832511628f1fe2c65534a46aa86b8e654b6d3567c000)，[UDP 编程](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868325264457324691c860044c5916ce11b305cb814000)
* 创建Socket时
    * AF_INET指定使用IPv4协议
    * SOCK_STREAM 指定为TCP协议
    * SOCK_DGRAM 指定为UDP协议
* 端口号
    * 80端口是Web服务的标准端口
    * 其他服务都有对应的标准端口号，例如SMTP服务是25端口，FTP服务是21端口
    * 端口号小于1024的是Internet标准服务的端口，端口号大于1024的，可以任意使用
* TCP连接创建的是双向通道
* 相对TCP，UDP则是面向无连接的协议
* 使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包
 
2.3 **结合[pydoc 17.2 - socket](https://docs.python.org/2/library/socket.html)，熟悉廖雪峰的[示例代码](https://github.com/michaelliao/learn-python/tree/master/socket)**
- bind 方法的参数应该是个元组
    - 敲示例代码时少输了一层括号，结果报错：`TypeError: bind() takes exactly one argument (2 given)`
- recvfrom 方法：
    + 参数：bufsize，即 The maximum amount of data to be received at once
        * 超过 bufsize 会怎样？动手试了一下，报错`socket.error: [Errno 10040]`
    + 返回值：(string, address)。这与sendto方法的参数相同。
- sendto 方法
- socket address 的格式：(host, port)
    + host: like 'daring.cwi.nl' or '100.50.200.5'
    + port: an integer

### 3 A Little More Info from 《python 基础教程》
CH14 网络编程
* 功能强大的 urllib和urllib2 模块：
    - 通过它们在网络上访问文件，就像访问本地电脑上的文件一样
* SocketServer 模块：实现更高级的服务器框架需求，如分叉和线程处理
* Twisted: 事件驱动的python网络框架
    - 可以很好地与GUI工具包协同工作
 