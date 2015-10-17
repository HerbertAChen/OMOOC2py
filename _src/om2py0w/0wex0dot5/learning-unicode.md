## 草稿

存储方式的区别
* 普通字符串string: ASCII码
* unicode字符串: Unicode字符


```
>>> a = "汉字"
>>> b= u"汉字"
>>> a
'\xba\xba\xd7\xd6'
>>> b
u'\u6c49\u5b57'
```

一般文件、代码的建议保存方式：`utf-8`
