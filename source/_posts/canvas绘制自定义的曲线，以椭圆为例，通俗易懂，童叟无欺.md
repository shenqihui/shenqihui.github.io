title: canvas绘制自定义的曲线，以椭圆为例，通俗易懂，童叟无欺
tags: [javascript,技术]
date: 2013-08-21 04:57:00
---

本篇文章，将讲述如何通过自定义的曲线函数，使用 canvas 的方式进行曲线的绘制。

为了通俗易懂，将以大家熟悉的椭圆曲线为例，进行椭圆的绘制。至于其他比较复杂的曲线，用户只需通过数学方式建立起曲线函数，然后变换成为距离函数方程，替换即可。另外：代码还没进行任何优化。
<!--more-->
（注：本文只适合那种能在一个点为原点、基于原点的每个角度只能存在一个点的曲线，通俗说就是，过原点作直线，与曲线相交的交点最多两个，而且两交点分别位于原点两端。）

目录结构

[1、数学分析](#hh1)

[2、曲线方程](#hh2)

[3、画一个点](#hh3)

[4、画形状](#hh4)

[5、废话](#hh5)

正文：

1、数学分析

首先讲解下椭圆的构造，如图所示，数学厉害的忽视这段。

========分割线，数学帝请忽略这一段========

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

看好，我要变形了。 →_→

假设 θ 为 ∠POF，P 点距离 x 轴的长度为 Y<sub>1</sub> 的值，设为 y；距离 Y 轴长度为 X<sub>1</sub> 值，设为 X，P 点基于 O 的坐标就是 (x<sub>1</sub>,y<sub>1</sub>)。

tanθ = y/x

y = xtanθ

带入椭圆方程 x²/a²+x2(tanθ)2/b²=1 ，解得。(注：tanθ * tanθ ，不记得是用 tanθ²/tan²θ 表示了，貌似是 tan²θ，本文统一 ((tanθ)²) 表示)

x² = a²b² / (b²+a²(tanθ)²)，代入 y = xtanθ，并进行化简得出  x²+y² = (a²b²(1+(tanθ)²)/ (b²+a²(tanθ)²)，就是说，通过 a，b，θ; 能计算出 OP 的距离来了。

========分割线，忽略了上面段的可以回来了========

2、曲线方程

因此，得到一个方程，返回的是OP的距离

```javascript
/*
  func: 
        ellipseFunc:return the length
  args:
        a:[number] ellipse's a
        b:[number] ellipse's b
        theta:[number] how much of Math.PI
*/
function ellipseFunc(a,b,theta) {
  // javascript Math对象下面的三角函数，传入的theta值必须是转换成弧度制的值，就是多少个3.141592…等等等的那个弧度制
  return Math.pow(((a*a*b*b)*(1+Math.tan(theta)*Math.tan(theta)))/(b*b+a*a*Math.tan(theta)*Math.tan(theta)),1/2);
}
```

3、画一个点

既然曲线函数完毕，下面就行画图了，先从画一个点来说，网上很对关于描绘一个点的帖子，我选了 ctx. [fillRect](http://www.w3schools.com/tags/canvas_fillrect.asp) (x,y,a,b)，这是绘制矩形的函数，x、y 为绘制矩形的起点，就是左上角，设置 a=b=1 ，就能绘制一个长宽各为 1px 大小的矩阵，个人喜欢使用其他也行。 

下面是绘制一个点的函数，填充风格没有定义，在传入 _ctx 时是什么 [fillStyle](http://www.w3school.com.cn/html5/canvas_fillstyle.asp) 就填充什么风格。

```javascript
/*
  func: 
        drawPoint:draw a point
  args:
        _ctx:[object]the canvas's getContent("2d") variable
        point:[object] the point where to draw a dot such as {"x":200,"y":200}
        strokwidth:[number] the draw line's width and height 
*/
function drawPoint(_ctx,point,strokwidth){
  strokwidth = strokwidth || 1;
  if(!(_ctx !== undefined && _ctx !== null)) return false;
  var x = point.x,
      y = point.y;
  _ctx.fillRect(x,y,strokwidth,strokwidth);
  return true;
}
```

4、画形状

点的绘制讲述完毕，开始画曲线了，用 for 循环，画图吧。
```javascript
/*
  func: 
        drawShape:draw a shape
  args:
        canvasId:[string]the canvas's id
        func:[function]the shape function
        ellipse:[object] the ellipse's a and b length such as {"a":300,"b":200}
        center:[object] the draw center such as {"x":400,"y":400}
*/
function drawShape(canvasId,func,ellipse,center){
   var _c = document.getElementById(canvasId);
  if(_c === null) return false;
  var _ctx = _c.getContext("2d");
 // 默认椭圆中心为canvas的中心
  var a = ellipse.a || 0,
      b = ellipse.b || 0,
      centerX = center.x || _c.width/2,
      centerY = center.y || _c.height/2,
      drawX,drawY,pointCX,pointCY;
  shapeGet = func;
  for(var i = 0;i <= 2*Math.PI; i+=0.0001){// 通过弧度绘图，精确到每个0.0001弧度画图，可以更加精确。但是小图的话，没必要那么精确，浪费CPU时间。
    length = shapeGet(a,b,i);
    pointCX = length*Math.cos(i);
    pointCY = length*Math.sin(i);
    drawX = centerX + pointCX;
    drawY = centerY - pointCY;
    drawPoint(_ctx,{"x":drawX,"y":drawY},1);
  }
  return true;
}
```

调用方式

```javascript
drawShape("myCanvas",ellipseFunc,{"a":300,"b":200},{"x":400,"y":400});
```

页面的全部源码如下：

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
<body>
  <div id="cloud">
    <canvas id="myCanvas" width="800" height="800"></canvas>
  </div>

<script>
  /*
    func: 
          ellipseFunc:return the length
    args:
          a:[number] ellipse's a
          b:[number] ellipse's b
          theta:[number] how much of Math.PI
  */
  function ellipseFunc(a,b,theta) {
    // javascript Math对象下面的三角函数，传入的theta值必须是转换成弧度制的值，就是多少个3.141592…等等等的那个弧度制
    return Math.pow(((a*a*b*b)*(1+Math.tan(theta)*Math.tan(theta)))/(b*b+a*a*Math.tan(theta)*Math.tan(theta)),1/2);
  }

  /*
    func: 
          drawPoint:draw a point
    args:
          _ctx:[object]the canvas's getContent("2d") variable
          point:[object] the point where to draw a dot such as {"x":200,"y":200}
          strokwidth:[number] the draw line's width and height 
  */
  function drawPoint(_ctx,point,strokwidth){
    strokwidth = strokwidth || 1;
    if(!(_ctx !== undefined && _ctx !== null)) return false;
    var x = point.x,
        y = point.y;
    _ctx.fillRect(x,y,strokwidth,strokwidth);
    return true;
  }

  /*
    func: 
          drawShape:draw a shape
    args:
          canvasId:[string]the canvas's id
          func:[function]the shape function
          ellipse:[object] the ellipse's a and b length such as {"a":300,"b":200}
          center:[object] the draw center such as {"x":400,"y":400}
  */
  function drawShape(canvasId,func,ellipse,center){
     var _c = document.getElementById(canvasId);
    if(_c === null) return false;
    var _ctx = _c.getContext("2d");
   // 默认椭圆中心为canvas的中心
    var a = ellipse.a || 0,
        b = ellipse.b || 0,
        centerX = center.x || _c.width/2,
        centerY = center.y || _c.height/2,
        drawX,drawY,pointCX,pointCY;
    shapeGet = func;
    for(var i = 0;i <= 2*Math.PI; i+=0.0001){// 通过弧度绘图，精确到每个0.0001弧度画图，可以更加精确，0.0001更加欢迎。但是小图的话，没必要那么精确，浪费CPU时间。
      length = shapeGet(a,b,i);
      pointCX = length*Math.cos(i);
      pointCY = length*Math.sin(i);
      drawX = centerX + pointCX;
      drawY = centerY - pointCY;
      drawPoint(_ctx,{"x":drawX,"y":drawY},1);
    }
    return true;
  }
  drawShape("myCanvas",ellipseFunc,{"a":300,"b":200},{"x":400,"y":400});

</script>
</body>
</html>
```

5、废话

本文产生的原因，本来是想做词云的，给定词云的形状，在这个形状内填充词语，产生了这个念头，词云还没实现，关键是如何才能让填充词语相互不覆盖的问题。后来，选择在 github 里面搜索算了，选择了一个 [jQuery.awesomeCloud.plugin](https://github.com/indyarmy/jQuery.awesomeCloud.pluginplugin)，但是填充效率确实压力山大。想过去模拟他的方法，做一个出来，因此先从画自定义曲线开始了。