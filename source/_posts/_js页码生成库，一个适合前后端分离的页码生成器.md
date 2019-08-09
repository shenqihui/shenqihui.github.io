title: js页码生成库，一个适合前后端分离的页码生成器
tags: [javascript,技术,前端]
date: 2014-07-13 09:50:00
show: hide
hidden: true
visible: hide
---

**前言**

上星期写的任务里面有需要进行分页的处理，git搜索了一番，没有觉得合适的，于是自己临时写了个分页的算法。

然后等闲下来的时候，决定把分页进行优化并推广。于是乎，一个适合前后端分离的页码生成器就这样出来了。
<!--more-->
先别废话了，直接上 [git 地址](https://github.com/shenqihui/pagination) 和 [demo 地址](http://shenqihui.github.io/pagination/)。看官果断点击进去瞧瞧看。项目主页的 readme 文档的自动排版将更好。

**先讲讲设计思想**

整个开发流程围绕事件绑定进行开发。

脱离 callback 回调这种回调方法，直接使用 事件 方式触发换页前后的动作，方便解耦。

既然使用这种方式进行回调，就使用全局变量挂载分页的数据，方便回调时候进行分页数据的访问。

**库的依赖**

由于开发库的时候，并没有使用原生的语法进行元素或者事件绑定的操作，因此需要依赖某个库。

现阶段，经过测试支持 zepto 以及 jquery （二选一）。

css 方面，建议还是直接自己写或者使用 bootstrap 的库，源代码里面有从 bootstrap 里面抽出来的分页 css 代码。

**简洁demo**

由于分页就必须知道分页数据大小，因此必须传输配置对象。

```javascript
var pageConfig = {
  // 每页显示的数据长度，必填，而且 >1
  prePageLenght: 10,
  // 数据的总长度，必填，而且 >1
  dataLength: 30,
  // 现在的页码，默认 1
  pageNow: 1,
  // 渲染分页 html 的容器，一般框架的容器即可
  renderBox: $('.pagination-box')
};
```

配置之后，进行调用

```javascript
// 运行即可分页
pageBuilder(pageConfig);
```

这样子就能进行分页了。

**回调的书写**

回调的书写虽然放在了调用分页的主函数后面，但是记得在调用分页之前就定义这些事件，因为一旦调用分页函数，就马上触发分页回调，写在后面了，就会忘记了刚分页时候的事件回调了。

首先是分页前的回调，分页之前会触发 window 下面一个自定义分页之前的事件&nbsp;<span class="s1">beforePageChange ，因此要触发处理分页前的动作，就这样处理：</span>

```javascript
// 提前定义好分页之前的动作，可选
$(window).on('beforePageChange', function() {
  // callback
  // todo
  // 获取当前页码，可以从 pageBuilder.page.pageNow 取得，注意此时的值为未分页之前的旧页码。
})

```

同样道理，分页之后的回调差不多：

```javascript
// 提前定义好分页之后的动作，可选
$(window).on('afterPageChange', function() {
  // callback
  // todo
  // 获取当前页码，可以从 pageBuilder.page.pageNow 取得
})
```

**特别说明**

一个页面只适合使用一个分页实例。分页的动作将在 hashchange 触发之后进行分页。

里面监控页码变化的函数：

```javascript
// 绑定换页的事件
$(window).on('hashchange', function() {
  var hash = location.hash;
  var pageTemp = 0;
  if (/^#page=\d+$/.test(hash) === true) {
    // 直接是页码的
    pageTemp = hash.substring(6) | 0;
    if (defaultConfig.pageNow !== pageTemp) {
      defaultConfig.pageNow = pageTemp;
      $(window).trigger("renderPagination");
    }

  } else if (hash === "#page=next") {
    // 下一页的
    location.hash = "page=" + ( defaultConfig.pageNow + 1 );
  } else if (hash === "#page=prev") {
    // 上一页的
    location.hash = "page=" + ( defaultConfig.pageNow - 1 );
  }
})
```

因为 hashchange 只支持 IE8+，

所以，该插件只适合 IE8+，甚至IE8的怪异模式不支持 hashchange 事件。


**结束语**

这个库还有很多可以优化的地方，例如页码缓存，还有作用域优化之类的，还没进行优化。

希望大家喜欢。喜欢的话，点个推荐吧，如果使用上了，记得 star 下哦。
