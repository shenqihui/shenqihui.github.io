title: canvas绘制自定义的曲线，以椭圆为例，通俗易懂，童叟无欺
tags: []
date: 2013-08-21 04:57:00
---

本篇文章，将讲述如何通过自定义的曲线函数，使用canvas的方式进行曲线的绘制。[
](http://sharefunny.sinaapp.com/example/ellipse.html)

为了通俗易懂，将以大家熟悉的椭圆曲线为例，进行椭圆的绘制。至于其他比较复杂的曲线，用户只需通过数学方式建立起曲线函数，然后变换成为距离函数方程，替换即可。另外：<span style="color: #ff0000;">代码还没进行任何优化。</span>
<!--more-->
<span style="color: #ff0000;">（注：本文只适合那种能在一个点为原点、基于原点的每个角度只能存在一个点的曲线，通俗说就是，过原点作直线，与曲线相交的交点最多两个，而且两交点分别位于原点两端。）</span>

目录结构

[1、数学分析](#hh1)

[2、曲线方程](#hh2)

[3、画一个点](#hh3)

[4、画形状](#hh4)

[5、废话](#hh5)

正文：

1、数学分析

首先讲解下椭圆的构造，如图所示，数学厉害的忽视这段。

======================================分割线，数学帝请忽略这一段==================================

![](http://images.cnitblog.com/blog/358891/201308/21124416-9a3d72a50a4e4defb07b200019eba1f8.png)

椭圆构造图

其中，OA,OB分别为半长轴和短长轴，通过此两线段的距离能计算出半焦距FO的长度，再确定心O的坐标就能确认整个椭圆的范围。

由此可知，清楚了OA,OB的距离，就能知道椭圆的形状。

[百度百科](http://baike.baidu.com/link?url=pbwLlXdKGl18oSg94MhDTzfi-http://baike.baidu.com/link?url=pbwLlXdKGl18oSg94MhDTzfi-s1HNoSmCs9EfZ3PeGy0hJSE0suePuZqvO7D92Zi)里面讲到，

> 椭圆的标准方程有两种，取决于焦点所在的坐标轴：
> 
> 1）焦点在X轴时，标准方程为：x&sup2;/a&sup2;+y&sup2;/b&sup2;=1 (a&gt;b&gt;0)
> 
> 2）焦点在Y轴时，标准方程为：y&sup2;/a&sup2;+x&sup2;/b&sup2;=1 (a&gt;b&gt;0)

其实两个概念差不多一样，将a 和 b在方程中的位置对调就行。不详细讲。

看好，我要变形了。&rarr;_&rarr;

假设&theta;为&ang;POF，P点距离x轴的长度为Y<sub>1</sub>的值，设为y；距离Y轴长度为X<sub>1</sub>值，设为X，P点基于O的坐标就是(x<sub>1</sub>,y<sub>1</sub>)。

tan&theta; = y/x

y = xtan&theta;

带入椭圆方程 x&sup2;/a&sup2;+x<sup>2</sup>(tan&theta;)<sup>2</sup>/b&sup2;=1，解得(注：tan&theta;*tan&theta;，不记得是用tan&theta;<sup>2</sup>/tan<sup>2</sup>&theta;表示了，貌似是tan<sup>2</sup>&theta;，本文统一(tan&theta;)<sup>2</sup>表示)

x<sup>2</sup> = a<sup>2</sup>b<sup>2</sup> / (b<sup>2</sup>+a<sup>2</sup>(tan&theta;)<sup>2</sup>)，带入y = xtan&theta;，并进行化简得出 x<sup>2</sup>+y<sup>2</sup> = (a<sup>2</sup>b<sup>2</sup>(1+(tan&theta;)<sup>2</sup>)/ (b<sup>2</sup>+a<sup>2</sup>(tan&theta;)<sup>2</sup>)，就是说，通过a，b，&theta; 能计算出OP 的距离来了。

======================================分割线，忽略了上面段的可以回来了====================================

2、曲线方程

因此，得到一个方程，返回的是OP的距离

<div class="cnblogs_code">
<pre><span style="color: #008000;">/*</span><span style="color: #008000;">
    func: 
          ellipseFunc:return the length
    args:
          a:[number] ellipse's a
          b:[number] ellipse's b
          theta:[number] how much of Math.PI
  </span><span style="color: #008000;">*/</span>
  <span style="color: #0000ff;">function</span><span style="color: #000000;"> ellipseFunc(a,b,theta) {
    </span><span style="color: #008000;">//</span><span style="color: #008000;"> javascript Math对象下面的三角函数，传入的theta值必须是转换成弧度制的值，就是多少个3.141592&hellip;等等等的那个弧度制</span>
    <span style="color: #0000ff;">return</span> Math.pow(((a*a*b*b)*(1+Math.tan(theta)*Math.tan(theta)))/(b*b+a*a*Math.tan(theta)*Math.tan(theta)),1/2<span style="color: #000000;">);
  }</span></pre>
</div>

3、画一个点

<span style="line-height: 1.5;">既然曲线函数完毕，下面就行画图了，先从画一个点来说，网上很对关于描绘一个点的帖子，我选了ctx.</span>[fillRect](http://www.w3schools.com/tags/canvas_fillrect.asp)<span style="line-height: 1.5;">(x,y,a,b)，这是绘制矩形的函数，x、y为绘制矩形的起点，就是左上角，设置a=b=1，就能绘制一个长宽各为1px大小的矩阵，个人喜欢使用其他也行。</span>

下面是绘制一个点的函数，填充风格没有定义，在传入_ctx时是什么[fillStyle](http://www.w3school.com.cn/html5/canvas_fillstyle.asp)就填充什么风格。

<div class="cnblogs_code">
<pre>  <span style="color: #008000;">/*</span><span style="color: #008000;">
    func: 
          drawPoint:draw a point
    args:
          _ctx:[object]the canvas's getContent("2d") variable
          point:[object] the point where to draw a dot such as {"x":200,"y":200}
          strokwidth:[number] the draw line's width and height 
  </span><span style="color: #008000;">*/</span>
  <span style="color: #0000ff;">function</span><span style="color: #000000;"> drawPoint(_ctx,point,strokwidth){
    strokwidth </span>= strokwidth || 1<span style="color: #000000;">;
    </span><span style="color: #0000ff;">if</span>(!(_ctx !== undefined &amp;&amp; _ctx !== <span style="color: #0000ff;">null</span>)) <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">false</span><span style="color: #000000;">;
    </span><span style="color: #0000ff;">var</span> x =<span style="color: #000000;"> point.x,
        y </span>=<span style="color: #000000;"> point.y;
    _ctx.fillRect(x,y,strokwidth,strokwidth);
    </span><span style="color: #0000ff;">return</span> <span style="color: #0000ff;">true</span><span style="color: #000000;">;
  }</span></pre>
</div>

4、画形状

点的绘制讲述完毕，开始画曲线了，用for循环，画图吧。

<div class="cnblogs_code">
<pre>  <span style="color: #008000;">/*</span><span style="color: #008000;">
    func: 
          drawShape:draw a shape
    args:
          canvasId:[string]the canvas's id
          func:[function]the shape function
          ellipse:[object] the ellipse's a and b length such as {"a":300,"b":200}
          center:[object] the draw center such as {"x":400,"y":400}
  </span><span style="color: #008000;">*/</span>
  <span style="color: #0000ff;">function</span><span style="color: #000000;"> drawShape(canvasId,func,ellipse,center){
     </span><span style="color: #0000ff;">var</span> _c =<span style="color: #000000;"> document.getElementById(canvasId);
    </span><span style="color: #0000ff;">if</span>(_c === <span style="color: #0000ff;">null</span>) <span style="color: #0000ff;">return</span> <span style="color: #0000ff;">false</span><span style="color: #000000;">;
    </span><span style="color: #0000ff;">var</span> _ctx = _c.getContext("2d"<span style="color: #000000;">);
   </span><span style="color: #008000;">//</span><span style="color: #008000;"> 默认椭圆中心为canvas的中心</span>
    <span style="color: #0000ff;">var</span> a = ellipse.a || 0<span style="color: #000000;">,
        b </span>= ellipse.b || 0<span style="color: #000000;">,
        centerX </span>= center.x || _c.width/2,
        centerY = center.y || _c.height/2,
<span style="color: #000000;">        drawX,drawY,pointCX,pointCY;
    shapeGet </span>=<span style="color: #000000;"> func;
    </span><span style="color: #0000ff;">for</span>(<span style="color: #0000ff;">var</span> i = 0;i &lt;= 2*Math.PI; i+=0.0001){<span style="color: #008000;">//</span><span style="color: #008000;"> 通过弧度绘图，精确到每个0.0001弧度画图，可以更加精确。但是小图的话，没必要那么精确，浪费CPU时间。</span>
      length =<span style="color: #000000;"> shapeGet(a,b,i);
      pointCX </span>= length*<span style="color: #000000;">Math.cos(i);
      pointCY </span>= length*<span style="color: #000000;">Math.sin(i);
      drawX </span>= centerX +<span style="color: #000000;"> pointCX;
      drawY </span>= centerY -<span style="color: #000000;"> pointCY;
      drawPoint(_ctx,{</span>"x":drawX,"y":drawY},1<span style="color: #000000;">);
    }
    </span><span style="color: #0000ff;">return</span> <span style="color: #0000ff;">true</span><span style="color: #000000;">;
  }</span></pre>
</div>

<span style="line-height: 1.5;">调用方式&nbsp;</span>

<div class="cnblogs_code">
<pre>drawShape("myCanvas",ellipseFunc,{"a":300,"b":200},{"x":400,"y":400});</pre>
</div>

页面的全部源码如下：

<div class="cnblogs_code" onclick="cnblogs_code_show('ef49d799-9301-4bf8-aca6-a398ff852e52')">![](http://images.cnblogs.com/OutliningIndicators/ContractedBlock.gif)![](http://images.cnblogs.com/OutliningIndicators/ExpandedBlockStart.gif)
<div id="cnblogs_code_open_ef49d799-9301-4bf8-aca6-a398ff852e52" class="cnblogs_code_hide">
<pre><span style="color: #0000ff;">&lt;!</span><span style="color: #ff00ff;">DOCTYPE html</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;</span><span style="color: #800000;">html</span><span style="color: #0000ff;">&gt;</span>
  <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">head</span><span style="color: #0000ff;">&gt;</span>
    <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">meta </span><span style="color: #ff0000;">charset</span><span style="color: #0000ff;">="utf-8"</span><span style="color: #0000ff;">&gt;</span>
  <span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">head</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;</span><span style="color: #800000;">body</span><span style="color: #0000ff;">&gt;</span>
  <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">div </span><span style="color: #ff0000;">id</span><span style="color: #0000ff;">="cloud"</span><span style="color: #0000ff;">&gt;</span>
    <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">canvas </span><span style="color: #ff0000;">id</span><span style="color: #0000ff;">="myCanvas"</span><span style="color: #ff0000;"> width</span><span style="color: #0000ff;">="800"</span><span style="color: #ff0000;"> height</span><span style="color: #0000ff;">="800"</span><span style="color: #0000ff;">&gt;&lt;/</span><span style="color: #800000;">canvas</span><span style="color: #0000ff;">&gt;</span>
  <span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">div</span><span style="color: #0000ff;">&gt;</span>

<span style="color: #0000ff;">&lt;</span><span style="color: #800000;">script</span><span style="color: #0000ff;">&gt;</span>
  <span style="background-color: #f5f5f5; color: #008000;">/*</span><span style="background-color: #f5f5f5; color: #008000;">
    func: 
          ellipseFunc:return the length
    args:
          a:[number] ellipse's a
          b:[number] ellipse's b
          theta:[number] how much of Math.PI
  </span><span style="background-color: #f5f5f5; color: #008000;">*/</span>
  <span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;"> ellipseFunc(a,b,theta) {
    </span><span style="background-color: #f5f5f5; color: #008000;">//</span><span style="background-color: #f5f5f5; color: #008000;"> javascript Math对象下面的三角函数，传入的theta值必须是转换成弧度制的值，就是多少个3.141592&hellip;等等等的那个弧度制</span>
    <span style="background-color: #f5f5f5; color: #0000ff;">return</span><span style="background-color: #f5f5f5; color: #000000;"> Math.pow(((a</span><span style="background-color: #f5f5f5; color: #000000;">*</span><span style="background-color: #f5f5f5; color: #000000;">a</span><span style="background-color: #f5f5f5; color: #000000;">*</span><span style="background-color: #f5f5f5; color: #000000;">b</span><span style="background-color: #f5f5f5; color: #000000;">*</span><span style="background-color: #f5f5f5; color: #000000;">b)</span><span style="background-color: #f5f5f5; color: #000000;">*</span><span style="background-color: #f5f5f5; color: #000000;">(</span><span style="background-color: #f5f5f5; color: #000000;">1</span><span style="background-color: #f5f5f5; color: #000000;">+</span><span style="background-color: #f5f5f5; color: #000000;">Math.tan(theta)</span><span style="background-color: #f5f5f5; color: #000000;">*</span><span style="background-color: #f5f5f5; color: #000000;">Math.tan(theta)))</span><span style="background-color: #f5f5f5; color: #000000;">/</span><span style="background-color: #f5f5f5; color: #000000;">(b*b+a*a*Math.tan(theta)*Math.tan(theta)),1</span><span style="background-color: #f5f5f5; color: #000000;">/</span><span style="background-color: #f5f5f5; color: #000000;">2</span><span style="background-color: #f5f5f5; color: #000000;">);
  }

  </span><span style="background-color: #f5f5f5; color: #008000;">/*</span><span style="background-color: #f5f5f5; color: #008000;">
    func: 
          drawPoint:draw a point
    args:
          _ctx:[object]the canvas's getContent("2d") variable
          point:[object] the point where to draw a dot such as {"x":200,"y":200}
          strokwidth:[number] the draw line's width and height 
  </span><span style="background-color: #f5f5f5; color: #008000;">*/</span>
  <span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;"> drawPoint(_ctx,point,strokwidth){
    strokwidth </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> strokwidth </span><span style="background-color: #f5f5f5; color: #000000;">||</span> <span style="background-color: #f5f5f5; color: #000000;">1</span><span style="background-color: #f5f5f5; color: #000000;">;
    </span><span style="background-color: #f5f5f5; color: #0000ff;">if</span><span style="background-color: #f5f5f5; color: #000000;">(</span><span style="background-color: #f5f5f5; color: #000000;">!</span><span style="background-color: #f5f5f5; color: #000000;">(_ctx </span><span style="background-color: #f5f5f5; color: #000000;">!==</span><span style="background-color: #f5f5f5; color: #000000;"> undefined </span><span style="background-color: #f5f5f5; color: #000000;">&amp;&amp;</span><span style="background-color: #f5f5f5; color: #000000;"> _ctx </span><span style="background-color: #f5f5f5; color: #000000;">!==</span> <span style="background-color: #f5f5f5; color: #0000ff;">null</span><span style="background-color: #f5f5f5; color: #000000;">)) </span><span style="background-color: #f5f5f5; color: #0000ff;">return</span> <span style="background-color: #f5f5f5; color: #0000ff;">false</span><span style="background-color: #f5f5f5; color: #000000;">;
    </span><span style="background-color: #f5f5f5; color: #0000ff;">var</span><span style="background-color: #f5f5f5; color: #000000;"> x </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> point.x,
        y </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> point.y;
    _ctx.fillRect(x,y,strokwidth,strokwidth);
    </span><span style="background-color: #f5f5f5; color: #0000ff;">return</span> <span style="background-color: #f5f5f5; color: #0000ff;">true</span><span style="background-color: #f5f5f5; color: #000000;">;
  }

  </span><span style="background-color: #f5f5f5; color: #008000;">/*</span><span style="background-color: #f5f5f5; color: #008000;">
    func: 
          drawShape:draw a shape
    args:
          canvasId:[string]the canvas's id
          func:[function]the shape function
          ellipse:[object] the ellipse's a and b length such as {"a":300,"b":200}
          center:[object] the draw center such as {"x":400,"y":400}
  </span><span style="background-color: #f5f5f5; color: #008000;">*/</span>
  <span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;"> drawShape(canvasId,func,ellipse,center){
     </span><span style="background-color: #f5f5f5; color: #0000ff;">var</span><span style="background-color: #f5f5f5; color: #000000;"> _c </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> document.getElementById(canvasId);
    </span><span style="background-color: #f5f5f5; color: #0000ff;">if</span><span style="background-color: #f5f5f5; color: #000000;">(_c </span><span style="background-color: #f5f5f5; color: #000000;">===</span> <span style="background-color: #f5f5f5; color: #0000ff;">null</span><span style="background-color: #f5f5f5; color: #000000;">) </span><span style="background-color: #f5f5f5; color: #0000ff;">return</span> <span style="background-color: #f5f5f5; color: #0000ff;">false</span><span style="background-color: #f5f5f5; color: #000000;">;
    </span><span style="background-color: #f5f5f5; color: #0000ff;">var</span><span style="background-color: #f5f5f5; color: #000000;"> _ctx </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> _c.getContext(</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">2d</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">);
   </span><span style="background-color: #f5f5f5; color: #008000;">//</span><span style="background-color: #f5f5f5; color: #008000;"> 默认椭圆中心为canvas的中心</span>
    <span style="background-color: #f5f5f5; color: #0000ff;">var</span><span style="background-color: #f5f5f5; color: #000000;"> a </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> ellipse.a </span><span style="background-color: #f5f5f5; color: #000000;">||</span> <span style="background-color: #f5f5f5; color: #000000;">0</span><span style="background-color: #f5f5f5; color: #000000;">,
        b </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> ellipse.b </span><span style="background-color: #f5f5f5; color: #000000;">||</span> <span style="background-color: #f5f5f5; color: #000000;">0</span><span style="background-color: #f5f5f5; color: #000000;">,
        centerX </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> center.x </span><span style="background-color: #f5f5f5; color: #000000;">||</span><span style="background-color: #f5f5f5; color: #000000;"> _c.width</span><span style="background-color: #f5f5f5; color: #000000;">/</span><span style="background-color: #f5f5f5; color: #000000;">2,</span>
<span style="background-color: #f5f5f5; color: #000000;">        centerY </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> center.y </span><span style="background-color: #f5f5f5; color: #000000;">||</span><span style="background-color: #f5f5f5; color: #000000;"> _c.height</span><span style="background-color: #f5f5f5; color: #000000;">/</span><span style="background-color: #f5f5f5; color: #000000;">2,</span>
<span style="background-color: #f5f5f5; color: #000000;">        drawX,drawY,pointCX,pointCY;
    shapeGet </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> func;
    </span><span style="background-color: #f5f5f5; color: #0000ff;">for</span><span style="background-color: #f5f5f5; color: #000000;">(</span><span style="background-color: #f5f5f5; color: #0000ff;">var</span><span style="background-color: #f5f5f5; color: #000000;"> i </span><span style="background-color: #f5f5f5; color: #000000;">=</span> <span style="background-color: #f5f5f5; color: #000000;">0</span><span style="background-color: #f5f5f5; color: #000000;">;i </span><span style="background-color: #f5f5f5; color: #000000;">&lt;=</span> <span style="background-color: #f5f5f5; color: #000000;">2</span><span style="background-color: #f5f5f5; color: #000000;">*</span><span style="background-color: #f5f5f5; color: #000000;">Math.PI; i</span><span style="background-color: #f5f5f5; color: #000000;">+=</span><span style="background-color: #f5f5f5; color: #000000;">0.0001</span><span style="background-color: #f5f5f5; color: #000000;">){</span><span style="background-color: #f5f5f5; color: #008000;">//</span><span style="background-color: #f5f5f5; color: #008000;"> 通过弧度绘图，精确到每个0.0001弧度画图，可以更加精确，0.0001更加欢迎。但是小图的话，没必要那么精确，浪费CPU时间。</span>
<span style="background-color: #f5f5f5; color: #000000;">      length </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> shapeGet(a,b,i);
      pointCX </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> length</span><span style="background-color: #f5f5f5; color: #000000;">*</span><span style="background-color: #f5f5f5; color: #000000;">Math.cos(i);
      pointCY </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> length</span><span style="background-color: #f5f5f5; color: #000000;">*</span><span style="background-color: #f5f5f5; color: #000000;">Math.sin(i);
      drawX </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> centerX </span><span style="background-color: #f5f5f5; color: #000000;">+</span><span style="background-color: #f5f5f5; color: #000000;"> pointCX;
      drawY </span><span style="background-color: #f5f5f5; color: #000000;">=</span><span style="background-color: #f5f5f5; color: #000000;"> centerY </span><span style="background-color: #f5f5f5; color: #000000;">-</span><span style="background-color: #f5f5f5; color: #000000;"> pointCY;
      drawPoint(_ctx,{</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">x</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">:drawX,</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">y</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">:drawY},</span><span style="background-color: #f5f5f5; color: #000000;">1</span><span style="background-color: #f5f5f5; color: #000000;">);
    }
    </span><span style="background-color: #f5f5f5; color: #0000ff;">return</span> <span style="background-color: #f5f5f5; color: #0000ff;">true</span><span style="background-color: #f5f5f5; color: #000000;">;
  }
  drawShape(</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">myCanvas</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">,ellipseFunc,{</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">a</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">:</span><span style="background-color: #f5f5f5; color: #000000;">300</span><span style="background-color: #f5f5f5; color: #000000;">,</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">b</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">:</span><span style="background-color: #f5f5f5; color: #000000;">200</span><span style="background-color: #f5f5f5; color: #000000;">},{</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">x</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">:</span><span style="background-color: #f5f5f5; color: #000000;">400</span><span style="background-color: #f5f5f5; color: #000000;">,</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">y</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">:</span><span style="background-color: #f5f5f5; color: #000000;">400</span><span style="background-color: #f5f5f5; color: #000000;">});

</span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">script</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">body</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">html</span><span style="color: #0000ff;">&gt;</span></pre>
</div>
<span class="cnblogs_code_collapse">View Code </span></div>

&nbsp;

5、废话

<span style="line-height: 1.5;">本文产生的原因，本来是想做词云的，给定词云的形状，在这个形状内填充词语，产生了这个念头，词云还没实现，关键是如何才能让填充词语相互不覆盖的问题。后来，选择在github里面搜索算了，选择了一个</span>[jQuery.awesomeCloud.plugin](https://github.com/indyarmy/jQuery.awesomeCloud.pluginplugin)<span style="line-height: 1.5;">，但是填充效率确实压力山大。想过去模拟他的方法，做一个出来，因此先从画自定义曲线开始了。</span>