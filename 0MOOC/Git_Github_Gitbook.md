#Git 三件套初印象

##Git与Github

Git 是一个版本管理系统，是 Github 的内在核心。Git 的操作主要是命令行形式，而 Github 可以用 Gui 的形式实现Git的多数(?)功能。当然，极客们大多是推崇命令行的，其妙处我尚未领会到。

###基本术语

可以先从 [Github bootcamp](Gbootcamp) 上手，了解一些基本概念。更多的术语可在[Github glossary](Gglossary) 中查询。

[Gbootcamp]:https://help.github.com/categories/bootcamp/
[Gglossary]:https://help.github.com/articles/github-glossary/

* **repository**: a project's folder. 
	* poject 可以是软件，个人网站，书稿，或者仅仅是存储想法或与人讨论的平台。
* **commit** (a change): commit 好比 "a snapshot of all the files in your project at a particular point in time".
	* 大致就是有改动后提交 project 的一个新版本
	* commit 时有选项：add the commit to the current or a new branch
* **branch**
	* "a parallel version of a repository, **contained within the repository**"
	* 用处：Develop features，Fix bugs，Safely experiment with new ideas
* **fork** 
	* "**a personal copy of another user's** repository that lives on your account"
	* 用处：
		* propose changes to another users repository
		* 或，借用别人已有的项目作为起点
* **pull request**
	* 即：将 branch 的改动提交给 upstream branch
	* 经审核后，pull request can be **merged into the repository**. 

###Git基本命令

这个简短的互动教程介绍了一些基本的Git命令： [try Git](https://try.github.io/levels/1/challenges/1)。包括：

* `git status`
	* 查看本地文件的变动状态
* `git add`
	* 将文件加入staging area. Staging area 是指
		> a place where we can group files together before we "commit" them to Git
* `git commit`
	* 修改记录信息可用后缀 `-m "message内容"`
* `git push`. 例如： `git push -u origin master`
	* `origin`: 远程仓库的惯用名称
	* `master`: 默认的本地 branch 名称
	* `-u`: 表示记住参数

以上只是 Git 的最基本命令。为做进一步的学习，我还需要查阅 [Git Documentation](http://git-scm.com/doc)。 

## Gitbook

###创建 gitbook

我还没有仔细研究 Gitbook 的用法。我创建 gitbook 的方法是参照了此文-- [gitbook-double-push][doublepush]。即：在 github 上 fork 已有的 gitbook 模板，clone 下来后，在本地编辑文件，并同时 `git push` 到 gitbook 和 github。   

###添加Disqus评论插件

参考：[Gitbook 如何安装 disqus 插件][disqus]

步骤：

1. 安装 npm （下载安装最新的 node.js 即可）
2. 用 npm 安装 gitbook disqus 插件，命令为：
`$ npm install gitbook-plugin-disqus -g`
3. 注册 Disqus，为 gitbook 建立一个 site，填写识别代号（shortname）。
4. 按[上述参考文章][disqus] 编辑 book.json 配置文件，写入 shortname值。
5. 重新发布 gitbook 图书即可。

[doublepush]:https://github.com/OpenMindClub/OMOOC.py/wiki/gitbook_double_push
[disqus]:http://www.chengweiyang.cn/gitbook/plugins/functional/disqus.html