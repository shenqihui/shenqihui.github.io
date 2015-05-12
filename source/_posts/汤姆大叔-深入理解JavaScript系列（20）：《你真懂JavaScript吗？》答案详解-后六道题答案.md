title: 汤姆大叔 深入理解JavaScript系列（20）：《你真懂JavaScript吗？》答案详解 后六道题答案
tags: []
date: 2014-02-03 15:00:00
---

原题目地址：http://www.cnblogs.com/TomXu/archive/2012/02/10/2342098.html

答案丰富多彩。我只是记录下自己思考了半天全部的答案。
<!--more-->
&nbsp;

**题目一：找出数字数组中最大的元素（使用Match.max函数）**

这个题目，看到Match，不知道啥东西，结果放在最后，

用了个很笨的解决方法：

```javascript
var arr=[0,1,2,3,4,5,6,7,8,9],arrFunc = [], max = -Infinity
for(var i = 0, l = arr.length; i < l; i++){
  max = Math.max(max,arr[i])
}
console.log(max);
```

后来看了下原文评论，原来这么简单。

```javascript
var arr=[0,1,2,3,4,5,6,7,8,9];
console.log(Math.max.apply(null,arr))
```

这个问题就没啥好解析的了。

**题目二：转化一个数字数组为function数组（每个function都弹出相应的数字）**

for循环闭包的问题，大叔的文章很多提到这个问题。

```javascript
var arr=[0,1,2,3,4,5,6,7,8,9],arrFunc = [];
for(var i = 0, l = arr.length; i < l; i++){
  arrFunc.push((function(i) {
    return function() {
      console.log(arr[i]);
    }
  })(i))
}
```

个人觉得对于闭包最简单的解析：闭包的作用就是保存当前的作用链域的环境。


**题目三：给object数组进行排序（排序条件是每个元素对象的属性个数）**

这个说起来好像很坑爹的赶脚。我居然用了这么笨的想法。

```javascript
Object.prototype.myLength = function(){
  var length = 0;
  for(var i in this){
    length ++;
  }
  return length;
}
var objArr = [
  {a:1, b:2, c:5, d:7, e:8, g:0, h:12, i:5, v:9, w:9, x:9, y:9, z: 15},
  {a:2, b:2, c:5, d:7, e:8, g:0, h:12, i:5, j:7, k:5, l:9, m:9, n:0, o:1, p:9, x:9, y:9, z:9 }, 
  {a:3, b:2, c:5, d:7, e:8, g:0, h:12, i:5, j:7, k:5, l:9, m:9, n:0, o:1, p:9, q:0 },
  {a:4, b:2, c:5, d:7, e:8, g:0, h:12, i:5, j:7, k:5, w:9, x:9, y:9, z:9 },
  {a:5, b:2, c:5, d:7, e:8, g:0, h:12, i:5, j:7, k:5, v:9, w:9, x:9, y:9, z:9 },
  {a:6, b:2, c:5, d:7, e:8, g:0, h:12, i:5, j:7, k:5, l:9, m:9, n:0, o:1, p:9, q:0, r:8, s:9, t:9, z:9 },
  {a:7, b:2, c:5, d:7, e:8, x:9, y:9, z:9 }
];
// arr before sort
var numArr1 = []
for(var i = 0, l = objArr.length; i < l; i++ ){
  numArr1.push( objArr[i].myLength() )
}
console.log(numArr1.join(" ")) //result
// arr after sort
objArr.sort(function(a,b){
  // stable sort
  // return (a.myLength() > b.myLength()) === true? 1:-1;
  // unstable sort
  return (a.myLength() >= b.myLength()) === true? 1:-1;
  // return a.myLength() - b.myLength();
})
var numArr2 = []
for(var i = 0, l = objArr.length; i < l; i++ ){
  // console.log(i,l,objArr[i].myLength());
  numArr2.push( objArr[i].myLength() )
}
console.log(numArr2.join(" ")) //result
```

感觉突然自己的想法和别人的有点不同（不好的方向）。


**题目四：利用JavaScript打印出Fibonacci数（不使用全局变量）**

这个问题，写完之后我看了下其他人的写法，一半一半都没写中间缓存保存，我觉得这也是大叔表明不适用全局变量的原因，我把两种方式都写了进去。

这个是有缓存的，

```javascript
var fibonacci = (function(){
  var s = [];
  var fun = function(x) {
    if(s[x]){
      return s[x];
    }
    if(x < 0) {
      throw "Can't be negative";
      return ;
    }
    else if(x === 0 || x === 1) {
      s[x] = s[x] || x;
      return s[x];
    }
    else{
      s[x] = ( fun(x - 1) + fun(x - 2) );
      return s[x];
    }
  };
  fun.print = function() {
    console.log(s.join(" "));
  }
  fun.printLast = function() {
    // console.log(s.length);
    return(s[s.length-1]);
  }
  window.s = s;
  return fun;

})()
console.time(200);
console.log(fibonacci(200));
console.log(fibonacci.printLast());
console.log(fibonacci.print());
console.timeEnd(200);
```

测试几百几千位的时间不足1000ms。

这个是递归无缓存的，

```javascript
var fibonacci2 = function(x){
  if(x < 0) {
    throw "Can't be negative";
    return ;
  }
  if(x === 0 || x === 1) {
    return x;
  }
  var num = ( fibonacci2(x - 1) + fibonacci2(x - 2) )
  return num;
}
console.time(32);
console.log(fibonacci2(32));
console.timeEnd(32);
```

测试个32位已经4000ms+，时间呈数量级增长，太坑。

**题目五：实现如下语法的功能：var a = (5).plus(3).minus(6); //2**

这个算是最简单的吧，但是我居然和别人的不一样，都能运行。

```javascript
Number.prototype.plus = function(x) {
  var num = this.valueOf() + x;
  return Number(num);
}
Number.prototype.minus = function(x) {
  var num = this.valueOf() - x;
  return Number(num);
}

var a = (5).plus(3).minus(6);
console.log(a);
alert(a);
```

人家直接返回一个num，我返回一个Number封装的num对象，其实都一样是Number对象。

**题目六：实现如下语法的功能：var a = add(2)(3)(4); //9**

这个题目算是第一个做出来的题目，因为我觉得这个题目的要求最简单，一看就记得，半夜睡醒了在床上直接脑袋打草稿运行了。

```javascript
function add(x) {
  var mid;
  mid = x || 0;
  function addObj(x) {
    x = x || 0;
    mid = mid + x;
    return addObj;
  }
  addObj.valueOf = function() {
    return mid;
  }
  addObj.toString = function() {
    return mid;
  }
  return addObj;
}
//call the obj.valueOf function
console.log(add(2));
console.log(add(2)(3));
console.log(add(2)(3)(4));
console.log(add(2)(3)(4)(5));

//call the obj.toString function
alert(add(2));
alert(add(2)(3));
alert(add(2)(3)(4));
alert(add(2)(3)(4)(5));
```

能无限调用。

写完上述代码，我参考了下原文评论里面的，看了下自己的代码，和别人的比较下，有好的地方，也有不足之处，不过我的代码比较浅显，不想部分人写的那些看了很久才看明白，特别是那个写了缓存的fibonacci数列的答案。