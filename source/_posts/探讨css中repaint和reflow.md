title: 探讨css中repaint和reflow
tags: []
date: 2014-02-12 05:47:00
---

(个人blog迁移文章。)

**前言：**

页面设计中，不可避免的需要浏览器进行repaint和reflow。那到底什么是repaint和reflow呢。下面谈谈自己对repaint和reflow的理解，以及结合其他技术牛的讲解，谈谈如何优化repaint和reflow。
<!--more-->
**初步介绍：**

开发一个页面时，不可避免的需要进行repaint和reflow。也就只有古来的静态页面才会不存在repaint和reflow。repaint主要是针对某一个DOM元素进行的重绘，reflow则是回流，针对整个页面的重排。字面意思来说：repaint就是重绘，reflow就是回流。repaint和reflow的目的是：展示一个新的页面样貌。

**严重性：**

在性能优先的前提下，性能消耗 reflow大于repaint。

**体现：**

repaint是某个DOM元素进行重绘；reflow是整个页面进行重排，也就是页面所有DOM元素渲染。

**如何触发：**

style变动造成repaint和reflow。

不涉及任何DOM元素的排版问题的变动为repaint，例如元素的color/text-align/text-decoration等等属性的变动。

除上面所提到的DOM元素style的修改基本为reflow。例如元素的任何涉及长、宽、行高、边框、display等style的修改。

**常见触发场景：**

1.  触发repaint：

        1.  color的修改，如color=#ddd；
    2.  text-align的修改，如text-align=center；
    3.  a:hover也会造成重绘。
    4.  :hover引起的颜色等不导致页面回流的style变动。
    5.  等等太多，一时间写出来也太难想了。
2.  触发reflow：

        1.  width/height/border/margin/padding的修改，如width=778px；
    2.  动画，:hover等伪类引起的元素表现改动，display=none等造成页面回流；
    3.  appendChild等DOM元素操作；
    4.  font类style的修改；
    5.  background的修改，注意着字面上可能以为是重绘，但是浏览器确实回流了，经过浏览器厂家的优化，部分background的修改只触发repaint，当然IE不用考虑；
    6.  scroll页面，这个不可避免；
    7.  resize页面，桌面版本的进行浏览器大小的缩放，移动端的话，还没玩过能拖动程序，resize程序窗口大小的多窗口操作系统。
    8.  读取元素的属性（这个无法理解，但是技术达人是这么说的，那就把它当做定理吧）：读取元素的某些属性（offsetLeft、offsetTop、offsetHeight、offsetWidth、scrollTop/Left/Width/Height、clientTop/Left/Width/Height、getComputedStyle()、currentStyle(in IE))；

**如何避免：**

说避免那是不可能的，不然就是以前古老的静态页面了，没有交互，那在现在看来，就是一个失败的作品。所以，在我们进行网页设计的时候，就必须尽量减少页面的repaint和reflow。repaint和reflow的目的是为了展示一个新的页面，那么我们在进行页面交互时，尽量通过各种方法减少repaint和reflow但又能展示一个新的页面的目的。所以下面将结合其他技术达人的建议，通过自己的理解，给大家讲解如何避免和优化repaint和reflow：

下面是大神Nicole Sullivan的原话：

> 1.  Change classes on the element you wish to style (as low in the dom tree as possible)
> 2.  Avoid setting multiple inline styles
> 3.  Apply animations to elements that are position fixed or absolute
> 4.  Trade smoothness for speed
> 5.  Avoid tables for layout
> 6.  Avoid JavaScript expressions in the CSS&nbsp;(IE only)

1.  **尽可能在DOM末梢通过改变class来修改元素的style属性**：尽可能的减少受影响的DOM元素。
2.  **避免设置多项内联样式**：使用常用的class的方式进行设置样式，以避免设置样式时访问DOM的低效率。
3.  **设置动画元素position属性为fixed或者absolute**：由于当前元素从DOM流中独立出来，因此受影响的只有当前元素，元素repaint。
4.  **牺牲平滑度满足性能**：动画精度太强，会造成更多次的repaint/reflow，牺牲精度，能满足性能的损耗，获取性能和平滑度的平衡。
5.  **避免使用table进行布局**：table的每个元素的大小以及内容的改动，都会导致整个table进行重新计算，造成大幅度的repaint或者reflow。改用div则可以进行针对性的repaint和避免不必要的reflow。
6.  **避免在CSS中使用运算式**：学习CSS的时候就知道，这个应该避免，不应该加深到这一层再去了解，因为这个的后果确实非常严重，一旦存在动画性的repaint/reflow，那么每一帧动画都会进行计算，性能消耗不容小觑。

**参考文献：**

1.  [页面重构应注意的repaint和reflow](http://www.blueidea.com/tech/web/2011/8365.asp "http://www.blueidea.com/tech/web/2011/8365.asp")
2.  [如何减少浏览器repaint和reflow（上）](http://blog.csdn.net/baiduforum/article/details/5415527 "如何减少浏览器repaint和reflow（上）")
3.  [回流与重绘：CSS性能让JavaScript变慢？](http://www.zhangxinxu.com/wordpress/2010/01/%E5%9B%9E%E6%B5%81%E4%B8%8E%E9%87%8D%E7%BB%98%EF%BC%9Acss%E6%80%A7%E8%83%BD%E8%AE%A9javascript%E5%8F%98%E6%85%A2%EF%BC%9F/ "回流与重绘：CSS性能让JavaScript变慢？")
4.  [Reflows &amp; Repaints: CSS Performance making your JavaScript slow?](http://www.stubbornella.org/content/2009/03/27/reflows-repaints-css-performance-making-your-javascript-slow/ "Permanent Link: Reflows &amp; Repaints: CSS Performance making your JavaScript slow?")

&nbsp;

觉得有用，点个赞，赞赞更健康。