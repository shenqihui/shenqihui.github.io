title: "CSS: 长度单位"
date: 2016-03-04 11:39:00
tags: [技术,前端,css]
---

说说目前 css 的长度单位

<!--more-->

其实就那几个，参考几篇，直接写个总结，不罗嗦：

### 绝对类型的

- px 多少像素
- in 多少英寸
- cm 多少厘米
- mm 多少毫米
- pt point, 1pt=1/72 in
- pc pica, 1pc=12pt

### 相对类型的

- em 相对当前元素的字体大小
- rem 相对根元素（如 body ） 的字体大小
- ex: 相对当前元素的 x 字母的高度大小
- ch: 相对当前元素的 x 字母的宽度大小
- vw: 相对可视窗口的宽度， %
- vh: 相对可视窗口的高度， %
- vmin: 相对可视窗口的宽度或者高度中的小的一个， %
- vmax: 相对可视窗口的宽度或者高度重的大的一个， %
- %: 相对当前父元素的同一属性的， %


Codepen 例子（我 fork 的）：

<p data-height="268" data-theme-id="0" data-slug-hash="wGKKvN" data-default-tab="result" data-user="shenqihui" class="codepen">See the Pen <a href="http://codepen.io/shenqihui/pen/wGKKvN/">Testing of Length units</a> on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>




参看：
[CSS的长度单位](http://www.w3cplus.com/css/the-lengths-of-css.html)
[七个你可能不了解的CSS单位](http://www.w3cplus.com/css/7-css-units-you-might-not-know-about.html)
