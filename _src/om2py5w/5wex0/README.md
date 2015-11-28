### Easynote SAE版 v1 功能及说明

极简交互式笔记的公网版本, 兼容命令行交互方式，并提供本地命令行管理工具
* 浏览器交互
    - 访问 http://1.sunote.sinaapp.com/
* 客户端命令行交互
    - 运行 [client_cli.py](client_cli.py)
        - 需安装模块：[requests](http://docs.python-requests.org/en/latest/), [bs4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - 添加笔记：输入文字并回车
    - 查看笔记：输入 `list` 或 `l`
    - 退出程序：输入 `quit` 或 `q`
* 命令行管理工具
    - 运行 [admin/admin_cli.py](admin/admin_cli.py)
        - 需安装模块：[requests](http://docs.python-requests.org/en/latest/), [bs4](http://www.crummy.com/software/BeautifulSoup/bs4/doc/)
    - 除包含客户端命令行的功能外，还可：
        + 查看笔记数量：输入 `num`
        + 清空全部笔记：输入 `clear`
        + 导出文本文件：输入 `exp`