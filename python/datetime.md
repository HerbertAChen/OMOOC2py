### datetime模块学习
* 重点学习其中的 datetime 对象
* 两类 objects
    - aware: 包含时区等信息；可互相比较；多一个 tzinfo 特性
    - naive: 更单纯，easy to understand and to work with
    - 判定条件：
        + A datetime object d is aware if d.tzinfo is not None and d.tzinfo.utcoffset(d) does not return None. 
        + If d.tzinfo is None, or if d.tzinfo is not None but d.tzinfo.utcoffset(d) returns None, d is naive.
* UTC：Coordinated Universal Time 
* Subclass relationships: （datetime 类是 date 类的子类？）
    * object
        * timedelta
        * tzinfo
        * time
        * date
            * datetime
* datetime 对象
    - Constructor:
    `class datetime.datetime(year, month, day[, hour[, minute[, second[, microsecond[, tzinfo]]]]])`
    - datetime.date(), datetime.time()
        + 由 datetime 对象得到 同一天的date对象/同时刻的time对象
    - datetime.strptime(*date_string*, *format*) 
        + 由字符串得到datetime对象，似乎能满足目标
        + Return a datetime corresponding to *date_string*, parsed according to *format*. 
        + This is equivalent to datetime(*(time.strptime(date_string, format)[0:6]))
            * [0:6] 是否代表：年月日时分秒？
        + parse: 语法分析
    - datetime.isoformat([sep]) 
        - 由对象得到string
        + Return a string representing the date and time in ISO 8601 format, YYYY-MM-DDTHH:MM:SS.mmmmmm or, if microsecond is 0, YYYY-MM-DDTHH:MM:SS
        + If utcoffset() does not return None, a 6-character string is appended, giving the UTC offset in (signed) hours and minutes: YYYY-MM-DDTHH:MM:SS.mmmmmm+HH:MM or, if microsecond is 0 YYYY-MM-DDTHH:MM:SS+HH:MM
            * 需要小心：当 datetime 对象包含时差信息时，该方法的返回值中也会包含时差信息
        + The optional argument sep (default 'T') is a one-character separator, placed between the date and time portions of the result
    - datetime.__str__()
        + For a datetime instance d, str(d) is equivalent to d.isoformat(' ').
    - 其他值得关注的方法
        + datetime.weekday()
            * Return the day of the week as an integer, where Monday is 0 and Sunday is 6
        + datetime.isoweekday()
            * Return the day of the week as an integer, where Monday is 1 and Sunday is 7
* strftime() and strptime() behavior
    - strftime(): 
        - date, datetime, time 对象都支持
        + 由这些对象得到 string
    - datetime.strptime()
        + 仅支持datetime对象
        + 与strftime() 相反：由 string (及指定格式format) 得到 datetime对象
        + format 的形式类似：'%Y-%m-%d %H:%M:%S'
            + 支持的 format codes 可查表
* 另：区分 strftime() 与 isoformat() 方法

### 字符串转换为 datetime对象
用 datetime.strptime() 方法即可实现
```python
>>> from datetime import datetime
>>> s = '2011-02-14 04:30:20'
>>> fmt = '%Y-%m-%d %H:%M:%S'
>>> dt = datetime.strptime(s, fmt)
>>> dt
datetime.datetime(2011, 2, 14, 4, 30, 20)
>>> str(dt)
'2011-02-14 04:30:20'
```

strptime() 方法只适用于 datetime 对象，若需继续转换为 date 或 time 对象，可用 datetime.date() 或 datetime.time()

务必区分模块名和对象名。以上提及的对象均来自 datetime 模块 (而非 time 或其他模块)，即相当于
`from datetime import datetime, date, time`