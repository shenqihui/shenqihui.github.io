title: javascript 控制台输出 图片 console.log 真强大 真佩服你们的创造力
tags: []
date: 2013-07-26 10:42:00
---

&nbsp;

![](http://images.cnitblog.com/blog/358891/201307/26184120-9ac42ecfcc1344508eb358c9f78021c7.png)

无意中，在百度知道页面发现了这货。居然能输出图片到控制台。

完全颠覆自己的三观，果断查阅其输出方法。后得知，原来如此。
<!--more-->
曾经做过的项目中，同事把控制台做成一个网页形式方便远程控制和远程调用。没想到过这控制台原来就是网页。

废话不多说，去片。下面是百度的原始输出页面的code

<div class="cnblogs_Highlighter">
<pre class="brush:javascript;gutter:false;">if (window.console) {
	var cons = console;
	if (cons) {
		cons.log("%c\n       ", "font-size:41px;background:url('http://cdn.iknow.bdimg.com/static/common/pkg/module_zed9cd9fd.png') no-repeat -135px -1px");
		cons.log('想和我们共同打造世界最大中文互动问答平台吗？\n想让自己的成就在亿万用户面前展现吗？想让世界看得你的光芒吗？\n加入我们，在这里不仅是工作，投入你的时间和热情，滴滴汗水终会汇聚成不平凡的成果。\n期待你的加盟。（投简历地址被我砍了）');
		cons.log("请在邮件中注明%c来自:console", "color:red;font-weight:bold;");
	}
}
</pre>
</div>

真佩服发现这东西的那人的想象力。估计这人也是搞浏览器开发的，然后发现了这东西。

然后，就没有然后了。骚年们，去投简历吧。