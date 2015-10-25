# Sublime Text 3 个人教程

* For Windows

## 前言

Sublime Text 3 （以下简称 ST3）是一款灵活、强大且美观的文本编辑器。
* 文本编辑操作极其便捷，支持[众多快捷键][hotkeys]
* 软件从头到脚都可定制
* 丰富的 package 资源，可以提供各种强大的扩展功能 
* 把“文本”的精神发挥到了极致，连各种配置界面都是文本化的

软件的安装无需多说。如此“神器”，想要玩转，肯定需要时日。本文仅覆盖部分较常用的功能，尚需在持续使用过程中继续完善。

[hotkeys]:http://docs.sublimetext.info/en/latest/reference/keyboard_shortcuts_win.html

## 基本功能
参考：
* 软件的["官方"文档](http://www.sublimetext.com/docs/3/)略显简陋
* 不过里边好心推荐了这个更为详尽的["非官方"文档](http://docs.sublimetext.info/en/latest/index.html)。

### 文本编辑

* 列选
    - 键盘或鼠标均可
    - `Ctrl` 增选，`Alt` 减选
* 选择重复文本
    - `Ctrl + D` 下一个， `Alt + F3` 全选
    - 可批量修改变量名等
* 其他快捷选文本方式
    - Select subwords (`Alt + Shift + <arrow>`)
    - Expand selection to brackets (`Ctrl + Shift + M`)
    - Expand selection to indentation (`Ctrl + Shift + J`)
    - Expand selection to scope (`Ctrl + Shift + Space`)
* 自动补全
    - 默认回车或Tab均可自动补全
    - 若把 default setting 里的 autocomplete on tab 改为 True，则为仅用 Tab 补全，可避免回车补全与换行冲突。
* 查找替换
  * 支持正则表达式

### 文件导航

* goto anything
    - ST3 的亮点，可在同项目的文件内快速导航
    - 支持3种运算符
        + `@symbol` ( Ctrl+R )
            * py 代码中：可快速跳转到函数定义
            * md 文档中：可快速跳转到标题，就像目录一样，好用！
        + `:line_number` ( Ctrl+L ): 快速跳转到行号
    - 对选定的文件，可以用右方向键或回车键打开
* 项目(projects)
    - 按项目组织文件的好处之一：可以方便地使用 Goto 导航
    - `Ctrl + Alt + P` 可切换不同项目

### 其他细节
* `Shift + F11` 进入全屏沉浸模式，一个极简的文本书写环境
* 状态栏最右侧：指定文本类型
* File\Reopen with encoding：改变文本编码方式
* ``Ctrl + ` ``：显示自带的 python console，可进行基本的交互，但不建议用于开发

## 功能扩展包
### package 安装

借助 [Package Control](https://packagecontrol.io/about) 工具，可以方便地安装和管理 packages。Package Control 本身的安装也很简单，只需把[这里](https://packagecontrol.io/installation)的代码粘贴到 ST3 的 console 里执行即可。

用 Package Control 安装 package：
1. `Ctrl + shift + P` 选择命令："Package Control: Installing packages"
2. 输入 package 名称，选定后回车即开始安装

### markdown 支持

我使用如下两个与 Markdown 有关的 package：
* 编辑：MarkdownEditing
    - 很神奇的编辑界面，兼具了纯文本的轻便性与 markdown 渲染效果的格式感
    - 素雅的黑白灰色调
    - 也有很多人推荐另一款：Monokai Extended（搭配 Markdown Extended），五颜六色的文字，是另一种风格
* 预览：Markdown Preview
    - 可在浏览器中预览
    - 修改保存后，在浏览器中刷新即可——准“实时”预览

ST3 配上这两款 package，书写 markdown 文档的体验相当好，秒杀之前在用的 MarkdownPad。后者又笨又丑，还不能免费选用 Github 口味；而其主打的实时分屏预览功能，对一个熟练的使用者而言，非但没有必要，反而会牵扯注意力。

### More Packages
Package Control 网站上可以搜到海量的优秀 package，请尽情探索吧！

## 进展
151025 细节修订（列选，goto）
151020 创建文档