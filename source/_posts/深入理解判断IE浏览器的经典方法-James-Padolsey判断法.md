title: 深入理解判断IE浏览器的经典方法-James Padolsey判断法
tags: []
date: 2012-07-20 02:11:00
---

标题这样子，是为了吸引眼球，至于是不是<span>James&nbsp;Padolsey原创的方法，网上是这么流传的就是了。菜鸟习作，写的不好，请轻拍。如果错误，请指出，感谢。</span>
<!--more-->
<span>正题：</span>

IE浏览器钉子户不断，IE 6像个老不死的一样存活在世界上，有人说：主要是因为chinese多。

我们现在开发网站都不针对IE6，需要针对的话得增加项目经费，毕竟IE6及其以下的css变现比较坑爹。

因此，多了下面这个函数，提醒客户不要在IE6及其以下版本进行浏览网站。

请看

<div class="cnblogs_code">
<pre><span style="color: #0000ff;">&lt;</span><span style="color: #800000;">html</span><span style="color: #0000ff;">&gt;</span>

<span style="color: #0000ff;">&lt;</span><span style="color: #800000;">head</span><span style="color: #0000ff;">&gt;</span>
  <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">script </span><span style="color: #ff0000;">type</span><span style="color: #0000ff;">="text/javascript"</span><span style="color: #0000ff;">&gt;</span>
    <span style="background-color: #f5f5f5; color: #0000ff;">var</span><span style="background-color: #f5f5f5; color: #000000;"> ie </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> (</span><span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;">(){  
      </span><span style="background-color: #f5f5f5; color: #0000ff;">var</span><span style="background-color: #f5f5f5; color: #000000;"> undef,  
      v </span><span style="background-color: #f5f5f5; color: #000000;">=</span> <span style="background-color: #f5f5f5; color: #000000;">3</span><span style="background-color: #f5f5f5; color: #000000;">,  
      div </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> document.createElement(</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">div</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">),  
      all </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> div.getElementsByTagName(</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">i</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">);         
      </span><span style="background-color: #f5f5f5; color: #0000ff;">while</span><span style="background-color: #f5f5f5; color: #000000;"> (  
        div.innerHTML </span><span style="background-color: #f5f5f5; color: #000000;">=</span> <span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">&lt;!--[if gt IE </span><span style="background-color: #f5f5f5; color: #000000;">'</span> <span style="background-color: #f5f5f5; color: #000000;">+</span><span style="background-color: #f5f5f5; color: #000000;"> (</span><span style="background-color: #f5f5f5; color: #000000;">++</span><span style="background-color: #f5f5f5; color: #000000;">v) </span><span style="background-color: #f5f5f5; color: #000000;">+</span> <span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">]&gt;&lt;i&gt;&lt;/i&gt;&lt;![endif]--&gt;</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">,
        all[</span><span style="background-color: #f5f5f5; color: #000000;">0</span><span style="background-color: #f5f5f5; color: #000000;">]
      ) ;   
      </span><span style="background-color: #f5f5f5; color: #0000ff;">return</span><span style="background-color: #f5f5f5; color: #000000;"> v </span><span style="background-color: #f5f5f5; color: #000000;">&gt;</span> <span style="background-color: #f5f5f5; color: #000000;">4</span> <span style="background-color: #f5f5f5; color: #000000;">?</span><span style="background-color: #f5f5f5; color: #000000;"> v : undef  
      }());
    </span><span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;"> is_ie(){        
      </span><span style="background-color: #f5f5f5; color: #0000ff;">if</span><span style="background-color: #f5f5f5; color: #000000;">(</span><span style="background-color: #f5f5f5; color: #000000;">!</span><span style="background-color: #f5f5f5; color: #000000;">ie)
        alert(</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">您当前使用非Microsoft Internet Explorer.</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">);
      </span><span style="background-color: #f5f5f5; color: #0000ff;">else</span> <span style="background-color: #f5f5f5; color: #0000ff;">if</span><span style="background-color: #f5f5f5; color: #000000;"> (ie</span><span style="background-color: #f5f5f5; color: #000000;">&lt;=</span><span style="background-color: #f5f5f5; color: #000000;">6</span><span style="background-color: #f5f5f5; color: #000000;">)
        alert(</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">您当前使用的浏览器版本过低。为获取良好的用户体验，\n请选择 IE 7.0 及其以上版本的Microsoft Internet Explorer.</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">);    
　　}//一楼 </span>[Jefft](http://home.cnblogs.com/u/66564/)<span>&nbsp; 评论说漏了一半大括号，现在补充了，多谢了。</span></pre>
<pre>[
](http://home.cnblogs.com/u/66564/)<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">script</span><span style="color: #0000ff;">&gt;</span></pre>
<pre><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">head</span><span style="color: #0000ff;">&gt;</span>

<span style="color: #0000ff;">&lt;</span><span style="color: #800000;">body </span><span style="color: #ff0000;">onload</span><span style="color: #0000ff;">="is_ie()"</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">body</span><span style="color: #0000ff;">&gt;</span>

<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">html</span><span style="color: #0000ff;">&gt;</span></pre>
</div>

这算是最简单又最高高效的IE判别方法了。不过，大部分人看不懂。

下面解析下为什么这样子：我的理解，如有错误，敬请指出，共同学习，多谢。

首先怎么调用，我就不讲了，如果不是IE，直接将ie赋值为undef的值，就是undefined，现在直接讲讲这货的代码块里面这个吧。<span style="color: #ffffff;">
</span>

<div class="cnblogs_code">
<pre><span style="color: #000000;">while (  
  div.innerHTML = '</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">[if gt IE ' + (++v) + ']&gt;&lt;i&gt;&lt;/i&gt;&lt;![endif]</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">',
  all[0]
) ;</span></pre>
</div>

这段代码。听巧妙的用到了逗号表达式，逗号表达式就是在表达式中，无论什么情况，返回最后一个子表达式的值，在这里就是返回all[0]的值了。

前面的div的赋值，为什么要放在这里，是因为这样子才能保证每次循环都能赋值，原创者这样写的话，是为了精简，这段代码，已经不能再精简了。

其实，能改成另外一种符合常人思维的形式。如下

<div class="cnblogs_code">
<pre><span style="color: #000000;">do {  
  div.innerHTML = '</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">[if gt IE ' + (++v) + ']&gt;&lt;i&gt;&lt;/i&gt;&lt;![endif]</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">';         
}while(all[0])  </span></pre>
</div>

改成这样子，while循环应该能看懂了吧？

其实不然，毕竟控制循环的变量很难理解对吧。

首先我们测试一下，就在这个while循环的下面，写上 alert(all[0])，

如

<div class="cnblogs_code">
<pre><span style="color: #000000;">do {  
  div.innerHTML = '</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">[if gt IE ' + (++v) + ']&gt;&lt;i&gt;&lt;/i&gt;&lt;![endif]</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">';         
}while(all[0]) 
alert(all[0])</span></pre>
</div>

你会发现，警告都是 undefined 。

但是，如果将这个写在while循环里面，你会发现，最后的那次警告必然是undefined ，之前的都是object（IEtester下面），非IE浏览器的话，只有一个警告，为undefined。代码如下，

<div class="cnblogs_code">
<pre><span style="color: #000000;">do {  
  div.innerHTML = '</span><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">[if gt IE ' + (++v) + ']&gt;&lt;i&gt;&lt;/i&gt;&lt;![endif]</span><span style="color: #008000;">--&gt;</span><span style="color: #000000;">';
  alert(all[0])         
}while(all[0]) </span></pre>
</div>

说道这里，大家应该知道用什么变量控制while循环的吧。

然后讲讲为什么all[0]会被赋值成为这样。下面根据w3c标准来讲讲看。

因为<span>getElementsByTagName这个函数返回的是一个指向<span>NodeList类型，请看[getElementsByTagName](http://www.w3.org/TR/DOM-Level-3-Core/core.html#ID-A6C9094 "getElementsByTagName")
</span></span>

<span><span>而当</span></span>div进行了重新赋值之后，应为NodeList 是活动的（目测这么翻译，摘自&nbsp;`NodeList`<span>&nbsp;objects in the DOM are&nbsp;</span>[live](http://www.w3.org/TR/DOM-Level-3-Core/core.html#td-live)<span>. 摘自[Interface NodeList](http://www.w3.org/TR/DOM-Level-3-Core/core.html#ID-536297177)</span>），所以整个NodeList的对象集合也就发生改变。请看[live](http://www.w3.org/TR/DOM-Level-3-Core/core.html#td-live)&nbsp;。

因此，all每次指向的东西都是不变的，变的是NodeList，all[0]指向的是NodeList的第一个 i 元素，也因此发生改变。

然后讲讲，为什么通过这样子的判断能判断出all[0]到底是object还是undefined呢？

原因很简单，就是，非IE浏览器不认识这样的条件注释。IE浏览器也不认不能相对应的那些条件注释。

下面是部分条件注释写法。

<div class="cnblogs_code">
<pre><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">[if IE]&gt;&lt;i&gt;您使用的是IE浏览器。&lt;/i&gt;&lt;![endif]</span><span style="color: #008000;">--&gt;</span>
<span style="color: #008000;">&lt;!--</span><span style="color: #008000;">[if IE 6]&gt;&lt;i&gt;欢迎使用Internet Explorer 6&lt;/i&gt;&lt;![endif]</span><span style="color: #008000;">--&gt;</span>
<span style="color: #008000;">&lt;!--</span><span style="color: #008000;">[if !(IE 6)]&gt;&lt;i&gt;您正在使用的不是 IE6。&lt;/i&gt;&lt;![endif]</span><span style="color: #008000;">--&gt;</span></pre>
</div>

太多，我就不写出来，详细规则请看[微软官方](http://msdn.microsoft.com/en-us/library/ms537512(VS.85).aspx)。

到了这里，大家应该大概了解了吧。

估计现在大家看我这篇文章的时候，用的都不是IE，那就举一个是IE的例子。

<div class="cnblogs_code">
<pre><span style="color: #008000;">&lt;!--</span><span style="color: #008000;">[if IE]&gt;&lt;i&gt;您使用的不是IE浏览器。&lt;/i&gt;&lt;![endif]</span><span style="color: #008000;">--&gt;</span></pre>
</div>

如果是IE浏览器，那么这段东西里面的&lt;i&gt;&lt;/i&gt;标签就能被 IE浏览器当正常的DOM元素。

如果不是IE浏览器，那么&ldquo;[if IE]&gt;&lt;i&gt;您使用的不是IE浏览器。&lt;/i&gt;&lt;![endif]&rdquo;整一句都会被当场注释掉了。至于<span>[if !IE]，目前来说，还是不能被非IE正确判别。</span>

讲到这里，大家还不懂的话，那么我这篇文章写得不好。抱歉浪费您的时间来看了。

感谢一楼[Jefft](http://home.cnblogs.com/u/66564/)&nbsp;和[xiiiiii](http://home.cnblogs.com/u/Xdoable/ "xiiiiiin")指导错误。