尚未整理成可读的教程，只是笔记的堆叠

### 概述
 
SQLite 特点：
* 简单，轻量级，python 内置了接口模块
* 使用文件存储，不需要服务器，不存在授权问题
* 软件上市后如有需要，迁移到其他更强大的数据库（如 MySQL 等）也较容易
 
什么是关系型数据库？
 
### 基本概念
 
表是数据库中存放关系数据的集合，一个数据库里面通常都包含多个表，比如学生的表，班级的表，学校的表，等等。表和表之间通过外键关联。
 
要操作关系数据库，首先需要连接到数据库，一个数据库连接称为Connection；
 
连接到数据库后，需要打开游标，称之为Cursor，通过Cursor执行SQL语句，然后，获得执行结果。
 
如何才能确保出错的情况下也关闭掉Connection对象和Cursor对象：用 try except finally
 
DB-API: 为不同的数据库提供了一致的访问接口，在不同的数据库之间移植代码很方便
 
python 对象与数据库对象之间的类型转换
 
ORM: object-relational mappers 对象-关系管理器，可为用户省去数据库管理的细节？
 
#### connection 对象
* close(), cursor()
* commit(), rollback()
    - 提交/取消当前事务
        + 什么是事务？？
 
#### cursor 对象
* execute, executemany 方法：执行数据库查询或命令
* fetchall, fetchone, fetchmany 方法：返回结果集的某些行
 
### [SQLite Python tutorial](http://zetcode.com/db/sqlitepythontutorial/)
 
`with conn:`
* With the with keyword, the Python interpreter automatically releases the resources. It also provides error handling.
* Using the with keyword, the changes are **automatically committed**. Otherwise, we would have to commit them manually.
 
execute 与 executemany
* 用 execute 进行 insert 时，传入的一组值是元组形式
    `cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")`
* 用 executemany 批量 insert 时，传入的是以元组为元素的元组，例子：
```py
cars = (
    (1, 'Audi', 52642),
    (2, 'Mercedes', 57127),
    (3, 'Skoda', 9000),
)
cur.executemany("INSERT INTO Cars VALUES(?, ?, ?)", cars)
```
* last inserted row id `cur.lastrowid`
* 下面例子：Id INTEGER PRIMARY KEY 是一个自动递增的列，此时在 insert 时需要显式地指明赋值的列名
    - 问题：删除某一行后，后边的Id会不会自动更新？
    ```py
    cur.execute("CREATE TABLE Friends(Id INTEGER PRIMARY KEY, Name TEXT);")
    cur.execute("INSERT INTO Friends(Name) VALUES ('Tom');")
    ```
* fetch data
    - 逐行获取
    ```py
    while True:
        row = cur.fetchone()
        if row == None:
            break
        print row[0], row[1], row[2]
    ```
* 默认情况下 cursor 返回的数据是元组的元组
* 但只需加一句 `con.row_factory = lite.Row`, 就可以用字典的方式获取 curser 返回的单行数据的值 （同时按元组的索引方式也可用）
* 至此 tutorial 尚未读完，后续值得看的还有：
    - parameterized queries
    - export and import of data, 等
