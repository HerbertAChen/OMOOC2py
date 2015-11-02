### easynote UDP网络版

#### 功能及使用
极简交互式笔记的网络版本
* 服务端
    - 运行 server\udp_server.py
    - 接收客户端输入的笔记，保存到 mynotes.txt
* 客户端
    - 运行 client\udp_client.py
    - 一次输入一行笔记
    - 输入 list 列出所有笔记
    - 输入 exit, quit 或 q 退出

#### 截图

![easynote-udp](snapshot-3wex0.png)

#### 技术要点

* socket 模块的简单应用
    - 创建，bind, sendto, recvfrom
    - socket address 的格式：('127.0.0.1', 51714)
* 调用 Easynote.py 里的 NewNote() 及 GetNotes() 函数