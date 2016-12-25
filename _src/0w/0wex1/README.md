## 0wex1 EasyNote 说明书 v1.0

### 主要功能

* 记录单行笔记
    - 自动记录当前时间
    - 支持标签输入
* 列出过往笔记
    - 列出全部笔记
    - 按标签筛选笔记
* 计划开发的功能
    - 按日期范围筛选笔记
    - 笔记删除
    - 笔记按日/月/标签等分组显示

### 程序介绍

#### 交互界面与命令说明
运行 `main.py` 后，进入程序交互界面:
```
## EasyNote v1.0 ##
Type "help" for more infomation.
$
```

用户可根据需要输入不同的命令. 关于命令的说明可输入 help 查看.
```
### 命令说明
* "new" -- 创建新笔记
* "exit" -- 退出
* "list [笔记集合]" -- 列出指定的笔记集合
* "del [笔记集合]" -- 删除指定的笔记集合
* 注：
    1. [笔记集合]可以是 "all" 或 "笔记编号(多个编号用逗号隔开)"
       或 "date:[yymmdd]-[yymmdd]" 或 "tag:[标签名]"
    2. [笔记集合] 中不应包含空格!
```
**!注: 目前仅支持 `new`, `exit`, `list`, 及 `list tag:xxx`.**

#### 新建笔记
* 输入命令 `new` 或 `n` , 将进入新建笔记界面. 
* 可在笔记末尾用'#'输入标签. 
* 输入完毕后按回车结束并保存, 程序会提示"note added!"
```
$ n
New note:
>>> 继续刷笨办法! #todo
Note added!
```

#### 列出笔记
输入命令 `list` 或 `list all`, 程序将在屏幕上打印出所有笔记.
```
$ list

 No            CreateTime   Content
 --            ----------   -------
  0   2015-10-27 14:40:01   继续刷笨办法! #todo
  1   2015-10-27 14:40:30   熟悉字符串的常用方法 #todo
  2   2015-10-27 14:42:05   为何用 sublime text 打开 mynotes.txt 会显示乱码? #q
  3   2015-10-27 14:43:08   勤奋 专注 持久 创意 良善

     4 notes listed.       
```

也可选择仅列出包含某个标签的笔记, 输入命令 `list tag:[tagname]` 即可:
```
$ list tag:todo                                             
                                                            
 No            CreateTime   Content                         
 --            ----------   -------                         
  0   2015-10-27 14:40:01   继续刷笨办法! #todo                   
  1   2015-10-27 14:40:30   熟悉字符串的常用方法 #todo                
                                                            
     2 notes listed.                                        
```

#### 其他

输入的笔记将自动存储在程序所在目录下的 mynotes.txt 文件中