title: Git 最佳实践
tags: []
date: 2015/01/29 23:11:00 
---

今天一个朋友在他们的 git 工作流上面遇到问题了。来询问我关于我们团队是如何使用 git 进行团队协作的。 然后我就秉着技术分享的思想给他们讲解。特意写下此文。git 这东西，用得好就是好东西。用得不好，那就只能怪你没下功夫去用了。骚年，勇敢的用起来吧。  

<!--more-->

## 前言
怎么使用 git， 为啥使用 git， 如何使用 git， git 和 svn 或者 hg 哪个好，就不说了，个人还是觉得 git 好。如果你觉得意见不同，来打我啊。  
本文提到的项目是网站类型的，迭代比较快，所以一旦有功能完成就即刻发布。  

## 我们的使用场景
项目是一个网站，开发团队 n(n>3)人。使用的时内部的 git 仓库。  


## 仓库规范
项目发起由项目组组织（organization）发起，每个项目成员进行仓库的 fork 操作，不允许 push 代码至非自己所有的远程仓库。  


## 分支规范
每个人都进行了仓库的 fork 操作，因此每个人的仓库（下称 origin ）分支就自由发挥了。主要讲讲主仓库（下称 upstream ）的分支规范。  
主仓库主要存在两个分支，master + dev 分支，具体名字可以随便，能理解就好。


### dev 分支的功能
dev 有两个功能，一个是发布到测试环境进行新功能测试，另外一个是用于团队成员进行 mr 时候使用的分支，最新功能一旦开发测试完毕，就进行 origin/branchname mr 到 upstream/dev 的操作， 分配给其他项目成员进行 review 。  
mr 期间成员可以任意对代码进行审查评论，mr 发起人需要对评论进行回应。  


### master 分支的功能
master 是生产环境所使用的代码，因此得确保 master 分支的代码时刻可用。如何确保，就是确保 dev 的代码能够无已知 bug 地运行了，才进行 upstream/dev mr upstream/master 的操作。dev 一旦新功能测试成功，就提 mr 至 master 分支， 分配给自己。然后自己点击 accept mr 的操作。  
这一步操作，看似多余，但是能确保 master 分支时刻可用。


## mr 的规范
上面讲完了两个分支的作用，这是大部分仓库基本上的操作，估计很多人都清楚。
那如何是用这两个分支进行方便团队协作呢？这个就是一门学问了。
由于前面提到了， dev 和 master 只能通过 mr 方法进行代码的变动，所以，提交 mr 的时候就需要确保该 mr 能够让 git 仓库程序自动 accept（自动 accept 的意思是点击 accept 按钮就能合并代码），其他成员确定 mr accept 时候，只需点击按钮即可完成，而不是 merge this request manually 。


## 团队协作踩坑大法
说一个场景很容易遇到的场景，假设项目 A 同时有 B 、 C 两个功能同时开发。不久， B 、 C 同时提了个 mr 上来。然后， B 经过 review 目测无 bug，点击了 accept ， 然后 C 也经过了 review 目测无 bug，点击了 accept 。  
但是目测失败了，线上生产环境是非常复杂，一堆的机器、分布式数据库，超大数据量等等，造成 B 功能在模拟环境运行失败的情形。然而此时 C 功能目测无 bug 测试也无 bug ，可发布生产环境了。但是由于 B 功能出现 bug ，dev 此时就不能进行 mr 到 master 进行功能发布了。  
C 功能急着发布，也只能看着 B 功能的成员修复此 bug 了。或者先把 B 功能从 dev 慢慢抠出来发布。但是这个是坑。

这里的漏洞就是 B 、 C 功能在 mr 阶段没有进行模拟生产环境测试就直接 accept 造成的。所以，就得解决这个问题。只有通过了 mr 阶段的模拟生产环境测试的 mr 才能点击 accept 进行代码合并。


## 如何解决 mr 阶段测试的问题
说说项目的测试环境，  
1、 用于 dev 分支代码的测试，基本上和生产环境一致，只是运行的代码不同而已。
2、 用于测试 mr 的测试环境，mr 测试的功能由自己控制，随便部署，每个提交 mr 的所有者需要部署 mr 环境给其他 review 代码的成员进行测试使用。在确保代码质量的同时，也确保了由于开发环境跟生产环境差异造成的代码缺陷。


## 团队协助规范
1. 禁止 push 代码至非 origin 仓库  
2. 使用 fetch + rebase 代替 pull + merge 更新其他成员最新的代码，不予许使用 pull + merge  
3. upstream 只能通过 mr 方式进行代码合并请求  
4. 功能 mr 必须 asign 给非自己进行代码审查  

------

我要开始讲故事了

------

## 如何进行团队的协助
以场景进行讲解吧。

### 需求订立
开发的功能都商量好了，产品狗可以一边玩去。项目起了个响当当的名字，叫做古猫搜索引擎，小明（git id ming） 和 小花（git id hua，女的打字工哦） 再加几个打酱油的打字工进行开发。

### 创建仓库
他们创建了个组织叫古猫组织（git id goocat），然后创建了个 goocat 仓库，设置主分支为 dev ，master 留着暂时不管，push 个 相同的 init 到 dev 和 master ，然后把小明和小花还有几个打酱油的设置为管理员权限。仓库就这样子弄上来了。 .gitignore 、 WTFPL 什么的，也在这个时候加上去。  

### 打字工出场
这个时候，产品狗的什么，已经为了避免冲突，被送去某个小黑屋好好呆着了。
其他打酱油的被分配开发数据库什么的了。  
小明和小花就马上动手写代码开发 index 页面，自己动手，丰衣足食。马上 fork 仓库， git clone 、 git remote add 什么一气呵成， add 了 upstream 和其他项目组成员的仓库地址。  
小明用上了打 dota 的 apm ，瞬间把后台功能完成了， push origin api 完成，接下来等妹子小花来补充前端开发了。小花真羡慕打 dota 的人的 apm 能这么高，用来写代码瞬间就写完了。  
但是小明完成的功能只是整个功能的一半，需要小花继续进行，所以小花第一步就是更新小明的代码下来
```bash
git remote -v 
git remote add ming git@**.com:ming/goocat.git
git fetch ming 
git checkout -b page 
git rebase -i ming/api
```
然后根据提示把 rebase 进行到底。这样子就能获取小明最新的代码了。

小花技术也杠杠的，瞬间接上了小明的几个 api。

### 需求变动
到了某个 api 的时候，发现页面展示效果其实没那么好，这个时候召唤产品狗和小明过来。

他们间对话
> 小花：这个功能我要这样这样这样，这样才是最好的交互效果。
> 小明这个时候使劲点头，手里的也不停下，拿着犀牛书在看。也能够在跟产品狗起争执时候一书拍过去，屡试不爽好吗，那个产品狗都被吓怕了。  
> 产品狗看了下小明的犀牛书，擦了下汗：这个想法非常好，就这么实现了

就这样子，没啥废话，需求就这样变吧。

### 多人协作
需求变动了，api 继续变下，小花女神交代小明改改api，我的分支是 apge ，小明刷刷刷几下就马上动手改了。

```bash
git checkout api
git status
git remote -v
git remote add nvshen git@**.com:hua/goocat.git
git fetch nvshen
git stash
git rebase -i nvshen/page
# 坐等 git rebase 完成
git stash pop
vim ***.py
vim api.md
# 编辑完毕代码
git add ***.py api.md
git commit -m '根据女神说的需求改动，进行 古猫搜索部分 api 改动'
git push origin api
```
然后跑过女神那里说： 小花，改动完了，你 fetch 下来看看呗。
小花有开始了这个功能代码的编写，获取小明最新的代码：
```bash
git stash 
git fetch ming
git push origin page
git rebase -i ming/api
git stash pop
```
然后继续进行代码的开发，编写完毕果断使用 github 客户端进行代码的 commit，不错不错，功能 done 。提交仓库给小明吧。
```bash
git push origin page
# 打印了一堆的冲突的信息
git push -f origin page
```
然后到线上仓库看看时候提交成功了，看看 commit ，看到了之前小明的 commit 
> '根据女神说的需求改动，进行 古猫搜索部分 api 改动'

然后小花又叹气了
> 这小明，老是这样子，一点勇气都没有。

然后在微信朋友圈发了条 Text ： 你主动一点，我们之间就会有故事。
然后告知小明前端开发完毕了，提 mr 测试吧。

### mr 操作
这个时候小明就开始提 mr 了
```bash
git fetch nvshen
git push origin api
git rebase -i nvshen/page
git push -f origin api
```
上仓库进行 mr 了，提交了个 mr ，指向给了某一个打酱油的打字工 A 进行 review ，看到写着不能自动 accept，原来其他几个打酱油的已经把部分功能提交并且 accept 了，而且代码有冲突，这个时候小明就要做成没冲突了。
```bash
git fetch upstream
git rebase -i upstream/dev
git push -f origin api
```
回 upstream 仓库看看，不错，能自动 accept 了。

### review && accept
打酱油 A 提了部分意见，小明都一一做了改动。最后 mr 环境测试成功了， accept ，发布到 dev 环境， 也成功，上线，古猫搜索引擎 demo 版本出来了。 
v0.1.0 实现了。

### 打版本了
产品狗一阵激动，终于实现了小部分了。
```bash
git clone git@**.com:goocat:goocat.git
git checkout dev
git tag v0.1.0
git push origin --tag
```
奔走相告，今晚大家唱歌庆祝。白天鹅 KTV 唱 K。

### 庆功会
小花点了一首歌： she 的 《恋人未满》，申请的唱出来了，眼睛还冒着泪花，时不时还望了望小明。

故事唱完了，小花很伤心：
> 那小明怎么能这样子，一点都不主动。  

然后喝了很多酒。结果醉了，领导说：
> 小明，公司里面你和小花关系最好了，今晚你负责送她回家啦。  

小明呆呆的望着女神去了。

散场了，小明扶着小花上了出租车，送小花回家，然后就没有然后了。
这是个悲伤的故事。

------

故事讲完了，大家洗洗睡吧。

------

## 科普下上面提到的名词
upstream : 上层仓库  
origin : 当前所有者的仓库  
master : 生产代码主分支  
dev : 开发代码主分支  
merge : 合并代码  
mr : merge request, 合并代码请求  
accept : 接受代码合并请求  
review : 队友对你的代码进行审查  
bug : 八阿哥  
~~以下的词我解析不了，有很多东西中文是没法解析的，自己理解~~
git : 词典释义为饭桶，无用的人 →_→  
organization : 相对于成员，它就是组织  
fork : 词典释义为叉子   
clone : 克隆

## 彩蛋
看到这里，也挺艰难的，其实 dev 测试环境可以去掉不用。  
至于其他的不同的方法，欢迎评论指导。


