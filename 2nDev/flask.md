### flask 使用小结

IPE 项目的 web 交互部分采用了 flask 框架，部署到阿里云上。目前，Flask 最新的稳定版本是 0.10.1。以下是浅尝 flask 的一些小结。

#### flask.g
`flask.g` 是一个在 [application context](http://flask.pocoo.org/docs/0.10/appcontext/) 之内存储全局信息的对象，可以轻松地在不同的路由和函数之间实现数据的传递。至少有这样两种非常方便的用法：
* 存入登录的用户信息，可以与 `flask.session` 配合使用
* 存入数据库连接的信息，从而方便地调用数据库的连接，简化数据操作的代码

#### flask.session
`flask.session` 的作用是存储用户登录信息并加密写入 cookies，为此需要设置 `secret key`。session 的操作方法和字典相似，写入信息时用 `session['key'] = value`，移除信息时用 `session.pop('key', None)`，其中 None 是找不到 key 时的返回值，避免引发` KeyError`。

为了识别用户，你可以选择类似 '`userid`' 或 '`username`' 这样的键。而当你用 OAUTH 方式时，情况有所不同，比如用 flask-dance 实现 github 授权时，它会自动往 session 里写入 `github_oauth_token` 这样的键。

值得一提的是，在模版 html 里可以直接访问 g 和 session 里的信息。

#### flask.flash()

用 flash() 可以方便地在页面上提供反馈。为此需要：

* 在模版里留下存储 flash 信息的位置，可以用 with 语句：`{% with messages = get_flashed_messages() %}`
* 在 flask app 的路由函数里，加入一句 `flash('你想要的文字')`

#### 在阿里云上部署 flask app

小赖同学推荐了这篇文章：
[How To Serve Flask Applications with uWSGI and Nginx on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04)

#### flask 周边

flask 被设计为一种小型的网络框架（microframework），其本身专注于实现核心功能。你可以将 flask 与其他一些现有模块结合使用，比如数据库相关、表单检验、用户授权等等，从而适应复杂的需求。在 flask 基础上，也发展出了一系列专注于特定功能的[衍生模块](http://flask.pocoo.org/extensions/)，可以按需选用。比如：

* Flask-Login：提供了用户 session 管理功能
* Flask-Mail：提供邮件发送功能
* OAuth 授权可用：Flask-OAuth、Flask-OAuthlib 和 Flask-Dance
