layout: photo
title: "我的 hexo pithy 主题"
date: 2016-02-24 19:53:02
tags: [技术,前端,设计]
---

这两天，写了个 hexo 简洁主题。

<!--more-->

就是这样， 主题地址： [hexo-theme-pithy](https://github.com/shenqihui/hexo-theme-pithy) 。  

## 效果
看看效果，拖出来遛一遛，你现在看到的这个网页，就是使用这个主题的了。

大屏幕效果：
![大屏幕效果](/picture/hexo-theme-pithy/desktop.jpg)
大屏幕效果之 Archive ：
![大屏幕 archive 效果](/picture/hexo-theme-pithy/desktop-archive.jpg)

iPad 效果：
![iPad 效果](/picture/hexo-theme-pithy/pad.jpg)  
iPad 效果之 Archive ：
![iPad 效果](/picture/hexo-theme-pithy/pad.jpg)  

iPhone 效果：
![iPhone 效果](/picture/hexo-theme-pithy/phone.png)

## 设计理念

我想要的，只是下面几个需求：

* 打开超快
* 整洁
* 干掉所有多余的东西
* 响应式

所以，最终下来，有里面几个特点：

* 出 disqus 评论和谷歌统计类 script ，没有任何其他 script 
* 只有一个 css 文件，没有字体文件
* 响应式做个取舍，导航栏超出讲隐藏，因此需要确保在不隐藏部分显示出重要的链接(例如 iPhone 效果图中的导航条中，最后那个 about 就被隐藏了。)
* 既然导航栏隐藏了，推荐增加个链接(list)的页面，里面有所有的链接，包含导航条的所有，还能加友情链接，详情可参考我上面的做法

## 依赖

* jade
* less

配置方法：在你的 blog 目录执行下面，增加插件。
```bash
npm install hexo-renderer-jade --save  
npm install hexo-renderer-less --save
```

## 使用
首先下载到你的主题目录，并且配置成为该主题。
``` bash
$ git clone https://github.com/shenqihui/hexo-theme-pithy.git themes/pithy
```
修改 `_config.yml` 的 theme 为 `pithy`

## 配置

### hexo 必写配置

* date_format
* title 

### 主题配置

默认的配置就能跑起来了。  
需要配置的时候，打开看看，针对性填充或者修改就行。

## 补充

主题还在不断开发，啥时候有更改，会改上去，欢迎提 issue 


## End