## WEB 开发 ：一些基本知识
尚未整理成可读的教程，只是笔记的堆叠

### 概述

PC 机兴起时主流的应用程序采用 Client/server 架构。而进入互联网时代，越来越多的程序采用 Browser/Server 架构。

Web开发的发展阶段：静态页面 -> CGI -> ASP/JSP/PHP -> MVC.

Web 应用需要频繁修改，而 python 长于快速开发，因此是 Web 开发的得力语言。

一些参考资料：
* Python 官网相关：[Web Programming in Python](https://wiki.python.org/moin/WebProgramming)
* 一个简明清晰的教程：[廖雪峰教程之 web开发篇](http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/001386832648091917b035146084c43b05754ec9408dfaf000)，包含5部分：
    - HTTP协议简介
    - HTML简介
    - WSGI接口
    - 使用web框架
    - 使用模版
    - 另：[关于数据库](
    http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868327777137a11bc6c28214243abad14b191dbc12e000)

### HTTP 与 HTML
* HTTP是在网络上传输HTML的协议，用于浏览器和服务器的通信。
* http 请求

> Web采用的HTTP协议采用了非常简单的请求-响应模式，从而大大简化了开发。当我们编写一个页面时，我们只需要在HTTP请求中把HTML发送出去，不需要考虑如何附带图片、视频等，浏览器如果需要请求图片和视频，它会发送另一个HTTP请求，因此，一个HTTP请求只处理一个资源。

* http 格式：一个HTTP包含Header和Body两部分，其中Body是可选的
* HTML: 规范的HTML包含`<head>...</head>`和`<body>...</body>`
    * 注意不要和HTTP的Header、Body搞混了
* CSS: Cascading Style Sheets（层叠样式表）的简称，CSS用来控制HTML里的所有元素如何展现
* javaScript: 为了让HTML具有交互性而作为脚本语言添加的


### WSGI 接口

> 了解了HTTP协议和HTML文档，我们其实就明白了一个Web应用的本质就是：
1. 浏览器发送一个HTTP请求；
2. 服务器收到请求，生成一个HTML文档；
3. 服务器把HTML文档作为HTTP响应的Body发送给浏览器；
4. 浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。

> 最简单的Web应用就是先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。Apache、Nginx、Lighttpd等这些常见的静态服务器就是干这件事情的。

> 如果要动态生成HTML，就需要把上述步骤自己来实现。不过，接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，如果我们自己来写这些底层代码，还没开始写动态HTML呢，就得花个把月去读HTTP规范。
 
> 正确的做法是底层代码由专门的服务器软件实现，我们用Python专注于生成HTML文档。因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。
这个接口就是WSGI：Web Server Gateway Interface。

>WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。我们来看一个最简单的Web版本的“Hello, web!”：

###　网络框架
廖雪峰：
> 我们需要在WSGI接口之上能进一步抽象，让我们专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做。
在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。Flask通过request.form['name']来获取表单的内容。

From python wiki: 
+ Full-stack frameworks
    * Generally, frameworks provide support for a number of activities such as interpreting requests (getting form parameters, handling cookies and sessions), producing responses (presenting data as HTML or in other formats), storing data persistently, and so on. Since a non-trivial Web application will require a number of different kinds of abstractions, often stacked upon each other, those frameworks which attempt to provide a complete solution for applications are often known as full-stack frameworks in that they attempt to supply components for each layer in the stack.
    * Most popular: Django, TurboGears, web2py
+ Non Full-Stack Frameworks
    * These projects provide the base "application server", either running as its own independent process, upon Apache or in other environments. On many of these you can then introduce your own choice of templating engines and other components to run on top, although some may provide technologies for parts of the technology stack.
    * Most popular: Bottle, CherryPy, Flask, Pyramid, Hug
    * Bottle: a fast and simple micro-framework for small web-applications. It offers request dispatching (Routes) with url parameter support, Templates, key/value Databases, a build-in HTTP Server and adapters for many third party WSGI/HTTP-server and template engines. All in a single file and with no dependencies other than the Python Standard Library.

### RESTful 风格
参：[RESTful Web services: The basics - ibm.com](https://www.ibm.com/developerworks/webservices/library/ws-restful/)
 
* Representational State Transfer (REST) has gained widespread acceptance across the Web as a simpler alternative to SOAP- and Web Services Description Language (WSDL)-based Web services.
* Key evidence of this shift in interface design is the adoption of REST by mainstream Web 2.0 service providers—including Yahoo, Google, and Facebook—who have deprecated or passed on SOAP and WSDL-based interfaces in favor of **an easier-to-use, resource-oriented model to expose their services**.
* REST defines a set of architectural principles by which you can design Web services that focus on a system's resources, including how resource states are addressed and transferred over HTTP by a wide range of clients written in different languages.
* a REST Web service follows **four basic design principles**:
    * Use HTTP methods explicitly.
    * Be stateless.
    * Expose directory structure-like URIs.
        - uri: In computing, a Uniform Resource Identifier (URI) is a string of characters used to identify the name of a resource
        - url: Uniform Resource Locator
    * Transfer XML, JavaScript Object Notation (JSON), or both.

### RESTful APIs in Python

一篇有趣的文章：[Communicating with RESTful APIs in Python](http://isbullsh.it/2012/06/Rest-api-in-python/)
* 对比了 urllib2, httplib2, pycurl, requests 这几个库
* 结论：前三者都很挫，requests 最棒
* requests
    * HTTP for human, 很有 pythonic 范儿
    * 上手比较简单

### Bottle 框架
* 官档：[bottle]( http://bottlepy.org/docs/dev/index.html)
* 一个中文教程：[linux系统运维-bottle框架教程](http://www.linuxyw.com/546.html)

#### Bottle tutorial 笔记

##### hello world
* 可以选择用类来实现
 
```
from bottle import Bottle, run
 
app = Bottle()
 
@app.route('/hello')
def hello():
    return "Hello World!"
 
run(app, host='localhost', port=8080)
```
 
##### request routing
* what is routing: routing 就是把 url 与 函数绑定的行为
* You can bind more than one route to a single callback
 
###### dynamic routes
* dynamic routes: Routes that contain wildcards
    - RESTful, nice-looking and meaningful URLs
        + what is restful?
* filter
    - define more specific wildcards
    - 放在通配符如后，如 < id:int>，对通配符匹配的目标进行限定
    - :int, :float, :path, :re
        + 仅匹配：整数，实数，路径等
 
###### http request methods
* 是什么：The HTTP protocol defines several request methods (sometimes referred to as “verbs”) for different tasks
    - 即：绑定到url上的动作，用以获取信息或完成其他动作
    - 这些动作是 http 协议所规定的
* GET: default
* POST PUT DELETE PATCH
    - 区分：可用 method keyword argument，或 对应的 decorators
* POST
    - for HTML form submission
    - example: handle a login form using POST (见 learnBottle2.py)
        - the /login URL is linked to two distinct callbacks, one for GET requests and another for POST requests
            + **callback**: Programmer code that is to be called when some external action happens. In the context of web frameworks, the mapping between URL paths and application code is often achieved by specifying a callback function for each URL
        - The first one displays a HTML form to the user
        - The second callback is invoked on a form submission and checks the login credentials the user entered into the form.
 
###### Routing static files
 
* Static files such as images or CSS files are not served automatically. You have to add a route and a callback to control which files get served and where to find them
    - what is a css file?
    - the <filename> wildcard won’t match a path with a slash in it.
    - To serve files in subdirectories, change the wildcard to use the path filter
 
```
from bottle import static_file
@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='/path/to/your/static/files')
```
 
###### error pages
* error() decorator
    - The only parameter passed to the error-handler is an instance of HTTPError
 
```
from bottle import error
@error(404)
def error404(error):
    return 'Nothing here, sorry'
```
 
##### Generating content
* in pure WSGI, application 只能返回字符串，且不支持 Unicode，而：
* Bottle is much more flexible and supports a wide range of types. It even adds a Content-Length header if possible and encodes unicode automatically, so you don’t have to
* bottle 支持返回的数据类型：
    - dict: automatically transformed into JSON strings
    - non-true values
    - unicode strings
        + Unicode strings (or iterables yielding unicode strings) are automatically encoded with the codec specified in the Content-Type header (utf8 by default) and then treated as normal byte strings
    - 等等
 
###### static files
You can directly return file objects, but static_file() is the recommended way to serve static files

##### development
###### debug mode
* debug: look for and remove the faults in a computer program
* In this mode, Bottle is much more verbose and provides helpful debugging information whenever an error occurs. It also disables some optimisations that might get in your way and adds some checks that warn you about possible misconfiguration.
* an incomplete list of things that change in debug mode:
    * The default error page shows a traceback.
    * Templates are not cached.
    * Plugins are applied immediately.

###### auto reloading
Every time you edit a module file, the reloader restarts the server process and loads the newest version of your code.
 
原理不大明白：main process， child process