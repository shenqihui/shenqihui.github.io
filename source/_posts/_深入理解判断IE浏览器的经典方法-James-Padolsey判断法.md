title: 深入理解判断IE浏览器的经典方法-James Padolsey判断法
tags: [javascript,技术,前端]
date: 2012-07-20 02:11:00
show: hide
hidden: true
visible: hide
---

标题这样子，是为了吸引眼球，至于是不是 James Padolsey 原创的方法，网上是这么流传的就是了。菜鸟习作，写的不好，请轻拍。如果错误，请指出，感谢。
<!--more-->
正题：

IE浏览器钉子户不断，IE 6像个老不死的一样存活在世界上，有人说：主要是因为 chinese 多。

我们现在开发网站都不针对 IE6，需要针对的话得增加项目经费，毕竟 IE6 及其以下的 css 变现比较坑爹。

因此，多了下面这个函数，提醒客户不要在IE6及其以下版本进行浏览网站。

请看

```html
<html>
  <head>
    <script type="text/javascript">
      var ie = (function(){
        var undef,
        v = 3,
        div = document.createElement('div'),
        all = div.getElementsByTagName('i');
        while (
          div.innerHTML = '<!—[if gt IE ' + (++v) + ']><i></i><![endif]—>',
          all[0]
        ) ;
        return v > 4 ? v : undef
      }());
      function is_ie(){
        if(!ie)
          alert('您当前使用非Microsoft Internet Explorer.');
        else if (ie<=6)
          alert('您当前使用的浏览器版本过低。为获取良好的用户体验，\n请选择 IE 7.0 及其以上版本的Microsoft Internet Explorer.');
  　　}
    </script>
  </head>
  <body onload="is_ie()">
  </body>
</html>
```


这算是最简单又最高高效的IE判别方法了。不过，大部分人看不懂。

下面解析下为什么这样子：我的理解，如有错误，敬请指出，共同学习，多谢。

首先怎么调用，我就不讲了，如果不是 IE，直接将 ie 赋值为 undefined 的值，就是 undefined，现在直接讲讲这货的代码块里面这个吧。

```javascript
while (
  div.innerHTML = '<!—-[if gt IE ' + (++v) + ']><i></i><![endif]-—>',
  all[0]
)
```

这段代码。听巧妙的用到了逗号表达式，逗号表达式就是在表达式中，无论什么情况，返回最后一个子表达式的值，在这里就是返回 all[0] 的值了。

前面的 div 的赋值，为什么要放在这里，是因为这样子才能保证每次循环都能赋值，原创者这样写的话，是为了精简，这段代码，已经不能再精简了。

其实，能改成另外一种符合常人思维的形式。如下

```javascript
do {
  div.innerHTML = '<!--[if gt IE ' + (++v) + ']><i></i><![endif]-->';
} while(all[0])
```

改成这样子，while 循环应该能看懂了吧？

其实不然，毕竟控制循环的变量很难理解对吧。

首先我们测试一下，就在这个 while 循环的下面，写上 alert(all[0])，

如

```javascript
do {
  div.innerHTML = '<!--[if gt IE ' + (++v) + ']><i></i><![endif]-->';
}while(all[0])
alert(all[0])
```

你会发现，警告都是 undefined 。

但是，如果将这个写在 while 循环里面，你会发现，最后的那次警告必然是 undefined ，之前的都是 object （IEtester 下面），非IE浏览器的话，只有一个警告，为 undefined。代码如下，

```javascript
do {
  div.innerHTML = '<!--[if gt IE ' + (++v) + ']><i></i><![endif]-->';
  alert(all[0])
}while(all[0])
```

说道这里，大家应该知道用什么变量控制 while 循环的吧。

然后讲讲为什么 `all[0]` 会被赋值成为这样。下面根据 w3c 标准来讲讲看。

因为 `getElementsByTagName` 这个函数返回的是一个指向 `NodeList` 类型，请看[getElementsByTagName](http://www.w3.org/TR/DOM-Level-3-Core/core.html#ID-A6C9094 "getElementsByTagName")

而当 `div` 进行了重新赋值之后，应为 `NodeList`  是活动的（目测这么翻译，摘自 `NodeListobjects in the DOM are [live](http://www.w3.org/TR/DOM-Level-3-Core/core.html#td-live)`. 摘自[Interface NodeList](http://www.w3.org/TR/DOM-Level-3-Core/core.html#ID-536297177)），所以整个NodeList的对象集合也就发生改变。请看[live](http://www.w3.org/TR/DOM-Level-3-Core/core.html#td-live)。

因此，all 每次指向的东西都是不变的，变的是 NodeList，all[0] 指向的是 NodeList 的第一个 i 元素，也因此发生改变。

然后讲讲，为什么通过这样子的判断能判断出 all[0] 到底是 object 还是 undefined 呢？

原因很简单，就是，非IE浏览器不认识这样的条件注释。IE浏览器也不认不能相对应的那些条件注释。

下面是部分条件注释写法。

```html
<!--[if IE]><i>您使用的是IE浏览器。</i><![endif]-->
<!--[if IE 6]><i>欢迎使用Internet Explorer 6</i><![endif]-->
<!--[if !(IE 6)]><i>您正在使用的不是 IE6。</i><![endif]-->
```

太多，我就不写出来，详细规则请看[微软官方](http://msdn.microsoft.com/en-us/library/ms537512(VS.85).aspx)。

到了这里，大家应该大概了解了吧。

估计现在大家看我这篇文章的时候，用的都不是IE，那就举一个是IE的例子。

```html
<!--[if IE]><i>您使用的不是IE浏览器。</i><![endif]-->
```

如果是IE浏览器，那么这段东西里面的 `<i></i>` 标签就能被 IE 浏览器当正常的 DOM 元素。

如果不是IE浏览器，那么 `[if IE]><i>您使用的不是IE浏览器。</i><![endif]` 整一句都会被当场注释掉了。至于 `[if !IE]`，目前来说，还是不能被非IE正确判别。

讲到这里，大家还不懂的话，那么我这篇文章写得不好。抱歉浪费您的时间来看了。
