 title : 探讨 css 中 repaint 和 reflow
 tags : []
 date : 2014-02-12 05:47:00
 show: hide
 hidden: true
 visible: hide
---

**前言：**

页面设计中，不可避免的需要浏览器进行 repaint 和 reflow 。那到底什么是 repaint 和 reflow 呢。下面谈谈自己对 repaint 和 reflow 的理解，以及结合其他技术牛的讲解，谈谈如何优化 repaint 和 reflow 。
<!-- more -->
**初步介绍：**

开发一个页面时，不可避免的需要进行 repaint 和 reflow 。也就只有古来的静态页面才会不存在 repaint 和 reflow 。 repaint 主要是针对某一个 DOM 元素进行的重绘， reflow 则是回流，针对整个页面的重排。字面意思来说： repaint 就是重绘， reflow 就是回流。 repaint 和 reflow 的目的是：展示一个新的页面样貌。

**严重性：**

在性能优先的前提下，性能消耗  reflow 大于 repaint 。

**体现：**

 repaint 是某个 DOM 元素进行重绘； reflow 是整个页面进行重排，也就是页面所有 DOM 元素渲染。

**如何触发：**

 style 变动造成 repaint 和 reflow 。

不涉及任何 DOM 元素的排版问题的变动为 repaint ，例如元素的 color / text - align / text - decoration 等等属性的变动。

除上面所提到的 DOM 元素 style 的修改基本为 reflow 。例如元素的任何涉及长、宽、行高、边框、 display 等 style 的修改。

**常见触发场景：**

1.  触发 repaint ：
    1.   color 的修改，如 color =# ddd ；
    2.   text - align 的修改，如 text - align = center ；
    3.   a : hover 也会造成重绘。
    4.  : hover 引起的颜色等不导致页面回流的 style 变动。
    5.  等等太多，一时间写出来也太难想了。

2.  触发 reflow ：
    1.   width / height / border / margin / padding 的修改，如 width =778 px ；
    2.  动画，: hover 等伪类引起的元素表现改动， display = none 等造成页面回流；
    3.   appendChild 等 DOM 元素操作；
    4.   font 类 style 的修改；
    5.   background 的修改，注意着字面上可能以为是重绘，但是浏览器确实回流了，经过浏览器厂家的优化，部分 background 的修改只触发 repaint ，当然 IE 不用考虑；
    6.   scroll 页面，这个不可避免；
    7.   resize 页面，桌面版本的进行浏览器大小的缩放，移动端的话，还没玩过能拖动程序， resize 程序窗口大小的多窗口操作系统。
    8.  读取元素的属性（这个无法理解，但是技术达人是这么说的，那就把它当做定理吧）：读取元素的某些属性（ offsetLeft 、 offsetTop 、 offsetHeight 、 offsetWidth 、 scrollTop / Left / Width / Height 、 clientTop / Left / Width / Height 、 getComputedStyle ()、 currentStyle ( in   IE ))；

**如何避免：**

说避免那是不可能的，不然就是以前古老的静态页面了，没有交互，那在现在看来，就是一个失败的作品。所以，在我们进行网页设计的时候，就必须尽量减少页面的 repaint 和 reflow 。 repaint 和 reflow 的目的是为了展示一个新的页面，那么我们在进行页面交互时，尽量通过各种方法减少 repaint 和 reflow 但又能展示一个新的页面的目的。所以下面将结合其他技术达人的建议，通过自己的理解，给大家讲解如何避免和优化 repaint 和 reflow ：

下面是大神 Nicole   Sullivan 的原话：

> 1.   Change   classes   on   the   element   you   wish   to   style  ( as   low   in   the   dom   tree   as   possible )
> 2.   Avoid   setting   multiple   inline   styles
> 3.   Apply   animations   to   elements   that   are   position   fixed   or   absolute
> 4.   Trade   smoothness   for   speed
> 5.   Avoid   tables   for   layout
> 6.   Avoid   JavaScript   expressions   in   the   CSS ( IE   only )

1.  **尽可能在 DOM 末梢通过改变 class 来修改元素的 style 属性**：尽可能的减少受影响的 DOM 元素。
2.  **避免设置多项内联样式**：使用常用的 class 的方式进行设置样式，以避免设置样式时访问 DOM 的低效率。
3.  **设置动画元素 position 属性为 fixed 或者 absolute **：由于当前元素从 DOM 流中独立出来，因此受影响的只有当前元素，元素 repaint 。
4.  **牺牲平滑度满足性能**：动画精度太强，会造成更多次的 repaint / reflow ，牺牲精度，能满足性能的损耗，获取性能和平滑度的平衡。
5.  **避免使用 table 进行布局**： table 的每个元素的大小以及内容的改动，都会导致整个 table 进行重新计算，造成大幅度的 repaint 或者 reflow 。改用 div 则可以进行针对性的 repaint 和避免不必要的 reflow 。
6.  **避免在 CSS 中使用运算式**：学习 CSS 的时候就知道，这个应该避免，不应该加深到这一层再去了解，因为这个的后果确实非常严重，一旦存在动画性的 repaint / reflow ，那么每一帧动画都会进行计算，性能消耗不容小觑。

**参考文献：**

1.  [页面重构应注意的 repaint 和 reflow ]( http :// www . blueidea . com / tech / web /2011/8365. asp  " http :// www . blueidea . com / tech / web /2011/8365. asp ")
2.  [如何减少浏览器 repaint 和 reflow （上）]( http :// blog . csdn . net / baiduforum / article / details /5415527 "如何减少浏览器 repaint 和 reflow （上）")
3.  [回流与重绘： CSS 性能让 JavaScript 变慢？]( http :// www . zhangxinxu . com / wordpress /2010/01/% E 5%9 B %9 E % E 6% B 5%81% E 4% B 8%8 E % E 9%87%8 D % E 7% BB %98% EF % BC %9 Acss % E 6%80% A 7% E 8%83% BD % E 8% AE % A 9 javascript % E 5%8 F %98% E 6%85% A 2% EF % BC %9 F / "回流与重绘： CSS 性能让 JavaScript 变慢？")
4.  [ Reflows  & amp ;  Repaints :  CSS   Performance   making   your   JavaScript   slow ?]( http :// www . stubbornella . org / content /2009/03/27/ reflows - repaints - css - performance - making - your - javascript - slow / " Permanent   Link :  Reflows  & amp ;  Repaints :  CSS   Performance   making   your   JavaScript   slow ?")


觉得有用，点个赞，赞赞更健康。
