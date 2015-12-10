title: "fab 部署脚本"
tags: ['proxy', '部署脚本']
date: 2015-12-10 22:23:23
---

这是遇到的某个项目（[zoomeye](https://www.zoomeye.org)）的 fab 部署脚本的改写通用版本。

可能对大型项目没起作用，但是对于小项目，作用还是很大，所以发出来写个文章分享下。


<!--more-->
---

# 有啥功能
* 部署开发人员的测试环境
* 部署测试环境
* 部署生产环境

---

# 部署生产环境
```
fab deploy:master
```

---

# 部署测试环境
```
fab deploy:dev
```

---
# 部署开发人员的测试环境
```
fab deploy:test,userA,funBranch,ubuntu@10.10.10.12
```

---

# 依赖
python, pip, fabric
```
sudo apt-get build-essential python-dev python-pip
sudo pip install fabric
```

---

# 配置
* 前 30 行针对性修改
* git 地址针对性修改
* 部署前，前端编译，后端编译等等针对修改
* 部署后，环境安装，服务重启等等针对修改

---

# 注意事项：
* 所有机器的 ssh 端口，都统一，不支持运行时修改 ssh 端口
* 所有仓库的仓库名都一致， 推荐 fork 方式进行 git 协助
* 执行这脚本的机器有 ssh 方式部署各个部署 git 仓库的权限，有 ssh 方式访问各个部署机器的权限。

---

看看源码：
<script src="http://gist.stutostu.com/shenqihui/64205c52078ce6c14602.js?file=fabfile.py"></script>

---

更多详情，查看 [https://gist.github.com/shenqihui/64205c52078ce6c14602](https://gist.github.com/shenqihui/64205c52078ce6c14602)

