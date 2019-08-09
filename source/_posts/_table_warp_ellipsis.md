title: "CSS 技巧：table 中，如何进行 warp 和 ellipsis"
tags: [table, warp, ellipsis]
date: 2016-01-17 17:15:23
categories: [BLOG,文章]
show: hide
hidden: true
visible: hide
---

今天谈谈 table 中 warp 和 ellipsis 问题。
table（display:table 形式，下同） 元素， 会随着子元素的高度和宽度直接进行缩放， 自定义的宽度高度基本不起作用，这也是 table 设定的目的。
但是，如果 table 中存在超级长的无法 warp 的单词，想要直接进行 ellipsis 展现，就必须进行特殊的设定。

下面我来讲讲这个的技术细节：

<!--more-->

---

# 例子，眼见为实

<p data-height="500" data-theme-id="0" data-slug-hash="zrEMOj" data-default-tab="result" data-user="shenqihui" class='codepen'>See the Pen <a href='http://codepen.io/shenqihui/pen/zrEMOj/'>zrEMOj</a>) on <a href='http://codepen.io'>CodePen</a>.</p>
<script async src="//assets.codepen.io/assets/embed/ei.js"></script>

---

# 例子讲解

---

## 例子一：任性，随便超出
不进行任何的处理，最基础的表格，我猜测这种情况在网站开发的时候估计会很少发生的。
无需讲解。

---

## 例子二：进行 word 的强制 break 和换行
```less
tag {
  word-wrap: break-word;
  word-break: break-all;
}
```
这个就是影响强制换行的主要代码，一般连用，最重要的就是 `word-break` 这个属性，能把所有的非正常 break 的单词进行强制单词。

---

## 例子三： 限定高度，进行超出的 ellipsis 。
一般这种需求，在进行列表形式的内容展示时候会经常用到。

例如：如果其中一列的文字超长，采用例子二的解决方式，会造成整个页面的不平衡。而这个时候，大部分是在展现的时候进行 ellipsis 隐藏提醒，如果用户 hover 或者其他方式时候，再采用 title 的方式进行提醒等等。

因此，就出现了在 table 中进行 ellipsis 的展现处理。
故，有了这篇文章：

先看代码：
```less
.td-overflow-container {
  // 必须定义上级 td 的高度。不然就没法获取高度。
  height: 100%;
  position: relative;
}
.td-overflow {
  white-space: nowrap;
  position: absolute;
  text-overflow: ellipsis;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
```
```html
<td style="height: 1em;" title="warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_">
  <div class="td-warp-container">
    <div class="td-warp"> warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_warp_</div>
  </div>
</td>
```
理解这段代码，需要理解的技术点有：

* table 是根据子容器大小而进行自己大小的计算的
* 脱离文档流
* position 的四个值的具体含义

## table 是根据子容器大小而进行自己大小的计算的
这个应该不用解析了，直接例子一、二就是这个样子，横或者宽都任意扩张。

## 脱离文档流
脱离了文档流之后，父元素就不能捕捉到该元素的大小了，故如果在 table 中直接运行这种方式，直接把子元素进行脱离文档流，就能避免 table 任性的横宽拓展。

## position 的四个值的具体含义
* static ，流定位，这个是默认的值，文档流中，父元素能知道其大小。
* relative，相对定位，父元素能捕捉该元素大小。
* absolute， 绝对行为，定位标准是最近的、position 为非 static 的父元素。
* fixed， 固定定位，没啥好说的。

上面三个技术点的讲解，估计能理解上面为什么用那些 css 就能处理文本的超出或者 ellipsis 了。

在 `td` 中， 使用了 `.td-overflow-container` ，定义了其宽度高度，使用了 relative 的定位，使 `.td-overflow` 有了定位的参考。
这个时候， `.td-overflow` 就知道了其宽度和高度了，具体的 `text-overflow` 或者 `overflow` 就能和普通的 block 类型的元素一样的处理方式了。
