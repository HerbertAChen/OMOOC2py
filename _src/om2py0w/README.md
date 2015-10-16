# OMOOC.py 周任务代码试作

## 0w

####[ex0: Quick into Python](0wex0\main.py)

*  42行代码，快速上手

####[ex1: Pomo History Reader](0wex1\readpomo.py)

* 功能设计
  * 读取 pomotodo.com 输出的个人番茄记录 csv 文件，按项目及子项目汇总番茄数
     * 番茄记录 csv 的格式：date,time,description
     * description 的个人习惯："项目：子项目"，中文冒号隔开
  * 样例csv文件： [Pomotodo_History\\_test.csv](0wex1\Pomotodo_History_test.csv)
* 技术要点
  * 读取文件内容，识别 description 列
  * 区分项目名和子项名
  * 记录子项与项目的从属关系，为每个子项记录番茄数
  * 最后按项目与子项二级结构输出 番茄数，同时汇总项目番茄数
* 实现难点
  * read csv文件
  * 读取和输出时对中文字符的支持
* 涉及知识
  * [13.1. csv - CSV File Reading and Writing - python documentation](https://docs.python.org/2/library/csv.html)
  * [python-unicodecsv](https://github.com/jdunck/python-unicodecsv)： 支持unicode的 csv 模块

