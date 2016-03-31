title: 我的程序员经验分享
speaker: 神奇辉
url: http://blog.shenqh.com
transition: zoomin/cards/slide
theme: dark


[slide]
<style type="text/css">
  a {
    display: inline;
  }
</style>

# 我的程序员经验分享


神奇辉  
微博：[@神奇辉](http://www.weibo.com/p/1005051896403155)  
Github：[shenqihui](https://github.com/shenqihui)  
Blog: [http://blog.shenqh.com](http://blog.shenqh.com)  

[slide]
# 分享目录

* 废话 {:&.moveIn}
* vagrant
* docker
* git
* github
* Github Desktop
* Mac
* 程序员必备素质


[slide]
# 废话1

* 我是谁 {:&.moveIn}
  * 干过啥：目前，一名*前端工程师*， ~~干过电商，传统企业，金融行业创业公司，~~ 安全行业公司。 {:&.moveIn}
  * 工具：~~svn，TortoiseHg，~~ git，github，vagrant，docker，npm， fabric， 等等
  * 前端：nodejs，javascript，html，css
  * 后端：~~php，ruby，java，~~ python，nodejs
  * 运维：linux，nginx
  * 数据库：mysql，redis，ES，mongo
  * 总结：渣渣程序员一枚
* 程序员社交网站
  * github {:&.moveIn}
  * cnblog
  * weibo 
  * twitter
  * v2ex
* [知道创宇研发技能表](http://blog.knownsec.com/Knownsec_RD_Checklist/v3.0.html)

[slide]
# 废话2

* 为啥做程序员 {:&.moveIn}
  * 小学开始接触电脑和互联网  {:&.moveIn}
  * 只是初一年级，但已经有了近5年的网络安全技术的学习和实践经验
  * 初中获得 ** 计算机大赛 ** 奖励
  * 高中获得 ** 计算机编程大赛一等奖，保送 ** 大学
  * ** 以上几条都是假的，→_→ ** 
  * 考大学时候，文科不是我的料，理科，化学没意思，物理弱鸡，其他，没兴趣，还是对计算机更感兴趣吧
  * ![word_lrean_m.jpg](/word_lrean_m.jpg)
  * ![word_lrean_m1.jpg](/word_lrean_m1.jpg)
* 废话完毕

[slide]
# vagrant

参考链接：http://www.stutostu.com/?p=1395

* 什么是 vagrant 
  * Create and configure lightweight, reproducible, and portable development environments.
  * Development environments made easy.
  * 因开发环境而生
  * https://www.vagrantup.com/ 官网
  * http://www.vagrantbox.es/  打包好的镜像

[slide]
# vagrant

* 用起来之 hello world
  * 安装 vagrnat
  * $ vagrant init hashicorp/precise64
  * $ vagrant up

[slide]
# vagrant

* 实际用起来
  * 到 http://www.vagrantbox.es/ 下载个喜欢的
  * $ vagrant box add {title} {url}  # url 可以为本地路径
  * $ vagrant init {title}
  * vi Vagrantfile # 修改 vagrant 例子。
  * $ vagrant up

[slide]
# vagrant

常用的 vagrant file 配置
![vagrantfile.jpg](/vagrantfile.jpg)

[slide]
# vagrant
实际 vagrant 编码，上面那幅图的文字版本
```python
Vagrant.configure(2) do |config|
  # 刚刚那个 title
  config.vm.box = "temp"
  # 虚拟机端口转发到宿主机
  config.vm.network "forwarded_port", guest: 8000, host: 8002
  # 设置内网 ip
  config.vm.network "private_network", ip: "192.168.100.100"
  # 文件挂载，写绝对路径
  config.vm.synced_folder "/Users/shenqihui/github", "/home/vagrant/github"
  config.vm.synced_folder "/Users/shenqihui/github", "/opt"
  config.vm.synced_folder "/Users/shenqihui/.ssh/", "/home/vagrant/.ssh_mac"
  config.vm.provider "virtualbox" do |vb|
    # 图形界面开启
    # vb.gui = true
    # 内存处理
    # vb.memory = "2048"
  end
  # 下面我不用
  # config.push.define "atlas" do |push|
  #   push.app = "YOUR_ATLAS_USERNAME/YOUR_APPLICATION_NAME"
  # end
  # 下面我基本不用
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
  #   sudo apt-get install -y apache2
  # SHELL
end
```

[slide]
# vagrant 实例
1.4M GIF, 时长 2 min ， 一次播放，想重复看刷新页面即可。  
看到 `vagrant@ubuntu-14:~$ ls` 就结束了。
![vagrant_hello.gif](/vagrant_hello.gif)

[slide]
# vagrant 总结：

* 专为开发环境而生 {:&.moveIn}
* 方便同步团队成员的开发环境
* 和生产环境一致的 OS
* 方便挂载文件系统
* 方便转发端口
* 方便配置内网 IP 和公网 IP
* 那用不用？
* 用起来

[slide]
# docker

* 是啥？ {:&.moveIn}
* 用来干啥？
* 建议：
  * 如果有人写好了 Dockerfile ， 那就用吧。  {:&.moveIn}
  * ci 测试使用这个来快速搭建环境。
  * 用来开发，不建议，调试比较坑。
  * 总要学着玩下，踩下坑的。 

[slide]
# git 

* 是啥？ {:&.moveIn}
  * 目前最流行的版本管理工具 {:&.moveIn}
  * 管理代码
* 怎么学？怎么用？
  * 多搜索查看下文章 {:&.moveIn}
  * 参与下 github 的开源项目
  * 参与下实际的 mr 合作
  * 善于使用工具： mac 、 Github Desktop
  * 多使用 git 尝试新的指令

[slide]
# github

* 说啥？ {:&.moveIn}
* 世界上最大的同性交友网站，好好回去探索下有啥。
* 不说了。自己回去注册个，参与下上面的活动。

[slide]
# Github Desktop

![github_desktop.jpg](/github_desktop.jpg)

# 用来干啥的？

* 查看 history  
* 进行 commit ，特别是一个文件中的其中几行的 commit 
* 无冲突分支 push 
* 其他操作呢？终端运行吧。


[slide]
# Mac

* 苹果操作系统， 基于 unix 的操作系统。  {:&.moveIn}
* 新手入门？ 推荐的软件： iterm2 , zsh , alfred , brew , 等等。
* 看看 [http://macshuo.com/?tag=mac](http://macshuo.com/?tag=mac)
* 那买不买？
* 果断买买买啦。

[slide]
# 程序员必备素质

* 思考能力，探索能力
  * 这个问题，该如何解决？
* 搜索能力
  * 很多问题，前人已经踩过坑了，网上已经有解决方法
* 理解能力
  * 这个问题为啥这样子就能解决
  * 刨根问底
* 总结能力
  * 为啥总结
  * 书读得越多而不加思索，你就会觉得你知道得很多；而当你读书而思考得越多的时候，你就会越清楚地看到，你知道得还很少。 ——伏尔泰

[slide]
# 给个讨论

举个 js 领域的例子：js 数组排序的问题

```javascript
[3,4,5,6,7,8,9,2,3,1,1,2,3,4,5,].sort()
[1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]
```

---

```javascript
[3,4,5,6,7,8,9,2,3,1,1,2,3,4,5,].sort(function(a, b) {
  return a - b;
})
[1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 6, 7, 8, 9]
```

---

```javascript
[3,4,5,6,7,8,9,2,3,1,1,2,3,4,5,].sort(function(a, b) {
  return b - a;
})
[9, 8, 7, 6, 5, 5, 4, 4, 3, 3, 3, 2, 2, 1, 1]
```
---

```javascript
[3,4,5,6,7,8,9,2,3,1,1,2,3,4,5,].sort(function(a, b) {
  return Math.random() - 0.5
})
[3, 5, 5, 9, 2, 4, 1, 3, 8, 3, 1, 6, 7, 4, 2]
```

[slide]
举个 js 领域的例子：js 数组排序的问题  
为什么返回不同返回值，排序顺序就不同？

* 内部就是一个排序算法，进行了元素对比，然后插入  {:&.moveIn}
* 我猜测是快排  
* “sort() 方法对数组的元素做原地的排序，并返回这个数组。 sort 可能不是稳定的。默认按照字符串的Unicode码位点（code point）排序。”
* 出自：[MDN> Web 技术文档> JavaScript> JavaScript 参考文档> JavaScript 标准库> Array> Array.prototype.sort()](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Array/sort)

* ![array_sort.jpg](/array_sort.jpg)  
* 图参考[javascript Array.prototype.sort 排序浅谈](http://imweb.io/topic/565cf7253ad940357eb99881) 。不去求证了。


[slide]
# 感谢
感谢大家  
感谢 nodePPT

[slide]

# END