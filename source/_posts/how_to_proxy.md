title: "搭建网络代理的几种方法。"
tags: ['proxy']
date: 2015-10-18 21:21:21
---
搭建网络代理的几种方法。

<!--more-->

# 讲讲代理方法
## shadowsocks
这个基本上很常用很常用的了。
需要服务器端和客户端，具体详情，查看[官网](https://github.com/shadowsocks/shadowsocks/wiki/Configuration-via-Config-File)，都很简单的，加密通信。  
缺点就是：一定要需要客户端，而且，转成 http 代理有点麻烦。

## ssh 转发
一条指令即可，直接生成了一个 socks5 的代理：
```
ssh -N -D 127.0.0.1:8080 user@vpsip -p sshport
```
基于 ssh 进行的代理。  
缺点：客户端执行 ssh 。

## 直接创建 proxy
网上一堆软件。github 搜索关键字 `proxy` ，基本上一堆，直接按照说明运行，即可开启一个 http(s) 的代理。

# 另外
同事推荐了 cow ，好像不错，还没尝试使用。

![汪汪汪](/img/cat_1.gif)
