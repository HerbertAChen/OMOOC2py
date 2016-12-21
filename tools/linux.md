### linux 初体验

linux 于我一直是个神秘的存在。直到开智py课程的大作业阶段，蹭了小赖申请的阿里云主机，第一次尝了鲜。课程结束后，我感到需要补一下 linux 的基础知识，于是学习了 udacity 上这个微型公开课 - [linux command line basics](https://www.udacity.com/course/linux-command-line-basics--ud595)，这才算 linux 扫了下盲，小结如下：

#### 虚拟机安装

使用 Windows 系统的同学，若想尝试一把 linux，可以选择安装双系统，Jeremiahzhang 同学的 gitbook 教程里[记录了折腾经验](https://jeremiahzhang.gitbooks.io/omooc2py/content/0MOOC/01_02_ubuntu.html)；如果不想那么折腾，也可以尝试下虚拟机。

比较流行的一些虚拟机软件包括，开源免费的 virtualbox，以及收费的 vmware、parellel desktop 等。如果不是重度使用的话，virtualbox 提供的 linux 体验大概也足够了。上面提到的 udacity 那门课里详细介绍了[安装方法](https://www.udacity.com/course/viewer#!/c-ud595/l-4597278561/m-4713348570)，我在这里不再赘述，只简单总结一下过程中的要点：

1. 可以用 git 自带的 git bash 作为登录 linux 虚拟机的 shell
2. 安装 virtualbox，这是供虚拟机运行用的
3. 另外需要安装 vagrant，作用是进行虚拟机配置，以及允许主机和虚拟机之间的文件传递，上面链接里给出了可供下载的配置文件。
4. `vagrant up` 命令用于启动虚拟机，第一次运行该命令时会自动下载 linux OS 镜像文件； `vagrant ssh` 命令用于登录虚拟机。

#### shell commands

[第1课第8节](https://www.udacity.com/course/viewer#!/c-ud595/l-4597278561/m-4696869610)中解说了困扰我挺久的问题：terminal 与 shell 的区别是什么？简单来说，terminal 仅仅提供了一个输入输出的界面，而 shell 在背后负责获取 input，解析和执行命令，并向 terminal 输出结果。

新学到的几个 shell 命令：
* echo：相当于 shell 里的 print 命令
* rm -r: 可用于删除文件夹，-r 表示 recursive
* man：获取有关有个命令的帮助
* less：是一个分页浏览文本的工具，我们在用 man 命令查看帮助信息时，实际就是在使用 less 浏览。less 下的一些便捷操作：
    * D/space 下一页，U 上一页
    * < 首行，\> 尾行，输入行数直接跳转
    * / 搜索（区分大小写，支持正则），n 下一处，N 上一处

另外，bash 下一些很方便的快捷键：
* Ctrl + A/E：定位到行首/行末
* Ctrl + U/K：删除光标前/后的文字
* Ctrl + L：清屏，比 clear 方便
* Ctrl + R：逆向搜索历史记录，连续按为搜索下一个
* 更多的可看 [这个页面](http://www.howtogeek.com/howto/ubuntu/keyboard-shortcuts-for-bash-command-shell-for-ubuntu-debian-suse-redhat-linux-etc/)

#### linux filesystem

文件系统这块，linux 与 windows 至少有两点明显的区别：

1. 不像 windows 下每个硬盘分区都有一个根目录（C:\\, D:\\, ...），linux 下只有一个根目录
2. 路径中的斜杠，linux 是正斜杠，与 url 中的相同，而 windows 下为反斜杠。


再记录一些零碎的点：
* . 开头的大多为配置文件，ls 命令默认不输出， 可用 ls -a 输出
* 文件名中包含空格或特殊符号 !$\#()[]%& 时，需要引号扩住，或用反斜杠转义
* 相对路径的用法： . 表示当前目录，可以用 `../../xxx` 这样的方法访问亲戚
* 文件名的 glob 匹配，例如：
    * *.{jpg,JPG}
    * [a-zA-Z]?? 匹配以字母开头的三字符文件名

#### 进一步学习可参考的资料

[udacity - Configuring Linux Web Servers](https://www.udacity.com/course/configuring-linux-web-servers--ud299)
* 与 linux 服务器配置有关的基础知识

[像黑客一样使用 linux 命令行](http://talk.linuxtoy.org/using-cli/#1)
* 从小赖教程里发现的幻灯，很酷很强大的命令行使用方法
