# GIT 个人笔记

## 前言
（走了一些弯路才发觉）官方的 [Pro Git book][ProGit] 写得清楚明白。Git 大概也是那种用 20% 的功能可以应付 80% 场景的工具。非重度的日常使用，只读第一章与第二章前两节应该基本足够；有其他问题可再去查其他章节，或者 Reference Manual。

[Pro Git book][ProGit] 的第一章介绍什么是 Git，以及如何安装和配置 Git；第二章前两节基本包含了 Git 最基本的一些使用流程；第三章专门讲 Branching。

[ProGit]:http://git-scm.com/book/en/v2/Git-Basics-Getting-a-Git-Repository

## What is Git
Git is a distributed Version Control System.
* VCS 的发展：local -> centralized -> distributed
* 大项目、多人协作场景下，版本管理并不简单

Git 的特点：
* Git 可记录下：每次修改的 who what when why
* the way Git thinks about its data: Snapshots, Not Differences
* 本地库文件包含了全部历史信息；对服务器的依赖不强

## 安装和配置
### win 下常见的两种安装方式

1. git for windows
  * 含：Git GUI, Git CMD, Git bash
2. github for windows
  * 包含一个 portable Git 命令行工具

### Git 的配置文件
按优先级降序：

* `/etc/gitconfig`：与 `--system` 关联
* `~/.gitconfig` or `~/.config/git/config`：与 `--global` 关联
* `.git/config` for a single repository

### 首次使用可配置项

* `user.name`
* `user.email`
* `core.editor`
* 具体命令见 [Pro Git book][ProGit] Chapter1.6

## Git 部分基本概念

* repository: a project's folder. 
* commit: 好比 "a snapshot of all the files in your project at a particular point in time".
  * 大致就是有改动后提交 project 的一个新版本
  * 在 Github 上 commit 时有选项：add the commit to the current or a new branch
* staging area: 
  * 提供一个中间环节，缓冲区，避免同时 commit 两个不相关的修改
    * 分批 commit，逻辑更清晰
  * 不需要分批时，也可用`git commit -a`跳过 staging area
  * 一个有趣的情形:
    * 一个文件在被 git add 后，先不 commit，做些修改，此时 git status 会看到，此文件同时出现在 staged 和 not staged area
* 可在 `.gitignore` 中添加规则，过滤不需要的文件
* branch
  * "a parallel version of a repository, contained within the repository"
  * 用处：Develop features，Fix bugs，Safely experiment with new ideas
* pull request
  * 即：将 branch 的改动提交给 upstream branch
  * 经审核后，pull request can be merged into the repository. 

## Git 常用命令

* `git init`
  * starting to track an existing project in Git
* `git status`
  * -s short
* `git add`
* `git diff`
  * `--staged`
  * `--cached`
* `git commit`
  * `-m` message
  * `-a` 跳过staging area，直接commit 所有 tracked file
* `git rm`
* `git mv`
  * 重命名也是mv的一种
* `git log`
  * `-p`: shows the difference
  * `-(n)`: last n commits
  * `--stat`: 查看commit的缩略信息
  * format options, limiting options
* Git 命令批量操作可用：**file-glob patterns**，类似正则表达式

## Someday/Maybe

undoing things
working with remotes
tagging
git aliases
git branching

## 进展

151019 初版