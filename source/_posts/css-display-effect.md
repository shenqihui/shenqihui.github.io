title: "CSS: display 对 css 个个属性的影响"
date: 2016-03-04 11:00:00
tags: [技术,前端,css]
---

最近踩坑，踩了 rotate 的坑。

然后才发现，不同的 display 是会影响 rotate 的。毕竟没能熟悉各个类型的 css 属性。

<!--more-->

然后，我就写了个东西，研究 display 对个个 css 属性的影响。

## 发个现在的总结吧：

inline 类型的元素， rotate 属性不作用。
block 类型的元素，基本差不多万能的感觉。
float 了的元素，就会变成 block 类型的了。

大概就这么多吧。其他我遇到坑了，会继续加加加。

详情参看：

<p data-height="268" data-theme-id="0" data-slug-hash="eZpNGq" data-default-tab="result" data-user="shenqihui" class="codepen">See the Pen <a href="http://codepen.io/shenqihui/pen/eZpNGq/">display effect</a> on <a href="http://codepen.io">CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>
