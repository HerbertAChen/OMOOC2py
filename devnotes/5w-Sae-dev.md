## Easynote SAE版 开发笔记
环境：
* Windows 10 | Powershell (in conEmu) | Active Python 2.7.8.10
* 文本编辑：Sublime text 3 | 浏览器：Chrome

### 开发准备
##### 了解 PaaS
Paas (Platform as a service) 一种云计算服务，为使用者提供一个开发、运行和管理 Web 应用的平台。除了 PaaS，我们还经常见到这两种 aas：
* Saas: 为使用者提供可用的软件(Software)，例如 Google Apps
* Iaas: 为使用者提供计算、数据存储等基础服务；相比 PaaS，IaaS 使用者需要更多地关心硬件、系统等问题。

国外一些知名的 PaaS 服务包括 google app engine，AWS Elastic Beanstalk，Microsoft Azure Web Sites 等等。在国内，除起步较早的新浪 SAE 之外，BAT 三巨头也均有 PaaS 服务。

##### 在 SAE 上创建应用

注册新浪云（可用微博帐号连接）后，进入 SAE 控制台，即可创建新应用。SAE 应用支持用 Git 或 SVN 部署。用 Git 部署的方法，官网交待的不够清楚，可以参考[此教程](http://bookshadow.com/weblog/2015/09/10/sae-git-introduction/)。

为在本地开发 SAE Python 应用，可参照官方文档配置[本地开发环境](http://www.sinacloud.com/doc/sae/python/tools.html#id2)（需安装 sae-python-dev 包），然后就可以在 localhost 8080 端口模拟 SAE Python 环境，不必每次修改代码都要 push 到远程库才能看到效果。

### 在 SAE 上部署极简笔记本应用
有了上周的极简笔记本 Web 版代码，工作已经完成了一半。要把已有的代码迁移到 SAE 上，主要需要做这两件事情：
* 参考 SAE 官网给的 bottle 框架指导，主代码文件应命名为 index.wsgi，其中，让 app 开始运行的语句，不再是 run()，而应是：
```
    import sae
    app = Bottle()
    sae.create_wsgi_app(app)
```
* 用 SAE 支持的数据存储服务改写原代码中的数据存取部分，比如可以用简单的类似字典的 KVDB。
    - KVDB 的基本用法参考[官方文档](http://www.sinacloud.com/doc/sae/python/kvdb.html#kvdb)

##### 关于数据存储
怎么把笔记内容和 kvdb 的 key/value 对应起来？

我的想法是，把（同一标签下的）所有笔记作为一个列表（确切地说，是一个字典的列表，每条笔记对应一个字典，有'content'、'time' 两个键），全部放到同一个 key 下面。这样做的好处是读取比较方便，但问题在于，value 的最大长度是 4M，无法存储海量的笔记。

##### 如何实现笔记逆序
在页面上按时间倒序输出笔记的体验要更好一些，如何实现呢？

首先想到的是，列表有获取反向序列的方法 reverse()。需要注意的是 reverse() 会把既有列表改写为它的反向列表，但 reverse 方法本身返回值是 None。试着用 reverse() 去实现倒序输出笔记，很快就遇到问题：第一次读取笔记时可以实现逆序，但接下来每次读取时又会把笔记列表反转一次，和写入笔记动作搭配起来，结果是顺序会完全乱套...

后来，在翻看《python 基础教程》时找到现成的答案，`list(reversed(x))` 即为列表 x 的逆序列表，即先用 reversed() 函数得到一个逆序的迭代器对象（请别问我什么叫迭代器，我也不懂..），再用 list() 函数将之转换为列表。

### HTML 模版和美化
参考 bootstrap 官网上两个简单的例子（[starter-template](http://getbootstrap.com/examples/starter-template/), [Sign-in page](http://getbootstrap.com/examples/signin/)），对页面做了一点美化。

过程中补充了一点 HTML 的基本知识，最有用的知识是 HTML box model 的四个层次：margin, border, padding, content

在上周 html 基本模版的基础上，新增了一个 info 模版，用于 /about 等页面。但有个问题尚待解决：info 模版和已有模版之间，重复部分很多（比如顶部导航条），如何简化呢？

### 命令行工具的开发
本周任务的需求包括两种命令行工具，一种供客户使用，一种供管理员使用。客户版的与上周完全相同，拷贝过来便是。
管理员版的功能需求：
* 获得当前笔记数量/访问数量等等基础数据
    - 笔记数量容易实现；访问数量至今尚不知如何获得
* 可以获得所有笔记备份的归档下载
    - 只需在读取笔记后写入文本文件
* 另外，删除笔记应该也是有用的功能

##### 待思考：后台管理功能的接口 
后台管理功能的接口如何设计？
* 目前采用的办法是，在主代码中为相应的管理功能提供一个 URL，并利用 @route() 绑定相应的操作，比如删除笔记等。
* 但这样做，网站的安全性如何保证呢？因为只要知道了这个 URL，任何人都可以实现相应的操作。
* 芝麻星卡片 "PaaS 101: CLI" 背面的两篇参考文章还未看，或许有帮助。

### 后续改进
* 笔记按标签分类
* 访问数量统计
* 非功能性接口改进？
* 认证功能?

### 附
* 链接
    - [App 网址](http://sunote.sinaapp.com/)
    - [代码目录](https://github.com/sunoonlee/OMOOC2py/tree/master/_src/om2py5w/5wex0)
* 进展
    * 151115 创建文档