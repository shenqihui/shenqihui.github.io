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

<div class="cnblogs_code">
<pre><span style="color: #0000ff;">var</span> arr=[0,1,2,3,4,5,6,7,8,9],arrFunc = [], max = -<span style="color: #000000;">Infinity
</span><span style="color: #0000ff;">for</span>(<span style="color: #0000ff;">var</span> i = 0, l = arr.length; i &lt; l; i++<span style="color: #000000;">){
  max </span>=<span style="color: #000000;"> Math.max(max,arr[i])
}
console.log(max);</span></pre>
</div>

后来看了下原文评论，原来这么简单。

<div class="cnblogs_code">
<pre><span style="color: #0000ff;">var</span> arr=[0,1,2,3,4,5,6,7,8,9<span style="color: #000000;">];
console.log(Math.max.apply(</span><span style="color: #0000ff;">null</span>,arr))</pre>
</div>

这个问题就没啥好解析的了。

**题目二：转化一个数字数组为function数组（每个function都弹出相应的数字）**

for循环闭包的问题，大叔的文章很多提到这个问题。

<div class="cnblogs_code">
<pre><span style="color: #0000ff;">var</span> arr=[0,1,2,3,4,5,6,7,8,9],arrFunc =<span style="color: #000000;"> [];
</span><span style="color: #0000ff;">for</span>(<span style="color: #0000ff;">var</span> i = 0, l = arr.length; i &lt; l; i++<span style="color: #000000;">){
  arrFunc.push((</span><span style="color: #0000ff;">function</span><span style="color: #000000;">(i) {
    </span><span style="color: #0000ff;">return</span> <span style="color: #0000ff;">function</span><span style="color: #000000;">() {
      console.log(arr[i]);
    }
  })(i))
}</span></pre>
</div>

个人觉得对于闭包最简单的解析：闭包的作用就是保存当前的作用链域的环境。

&nbsp;

**题目三：给object数组进行排序（排序条件是每个元素对象的属性个数）**

这个说起来好像很坑爹的赶脚。我居然用了这么笨的想法。

<div class="cnblogs_code">
<pre>Object.prototype.myLength = <span style="color: #0000ff;">function</span><span style="color: #000000;">(){
  </span><span style="color: #0000ff;">var</span> length = 0<span style="color: #000000;">;
  </span><span style="color: #0000ff;">for</span>(<span style="color: #0000ff;">var</span> i <span style="color: #0000ff;">in</span> <span style="color: #0000ff;">this</span><span style="color: #000000;">){
    length </span>++<span style="color: #000000;">;
  }
  </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> length;
}
</span><span style="color: #0000ff;">var</span> objArr =<span style="color: #000000;"> [
  {a:</span>1, b:2, c:5, d:7, e:8, g:0, h:12, i:5, v:9, w:9, x:9, y:9, z: 15<span style="color: #000000;">},
  {a:</span>2, b:2, c:5, d:7, e:8, g:0, h:12, i:5, j:7, k:5, l:9, m:9, n:0, o:1, p:9, x:9, y:9, z:9<span style="color: #000000;"> }, 
  {a:</span>3, b:2, c:5, d:7, e:8, g:0, h:12, i:5, j:7, k:5, l:9, m:9, n:0, o:1, p:9, q:0<span style="color: #000000;"> },
  {a:</span>4, b:2, c:5, d:7, e:8, g:0, h:12, i:5, j:7, k:5, w:9, x:9, y:9, z:9<span style="color: #000000;"> },
  {a:</span>5, b:2, c:5, d:7, e:8, g:0, h:12, i:5, j:7, k:5, v:9, w:9, x:9, y:9, z:9<span style="color: #000000;"> },
  {a:</span>6, b:2, c:5, d:7, e:8, g:0, h:12, i:5, j:7, k:5, l:9, m:9, n:0, o:1, p:9, q:0, r:8, s:9, t:9, z:9<span style="color: #000000;"> },
  {a:</span>7, b:2, c:5, d:7, e:8, x:9, y:9, z:9<span style="color: #000000;"> }</span><span style="color: #000000;">
];
</span><span style="color: #008000;">//</span><span style="color: #008000;"> arr before sort</span>
<span style="color: #0000ff;">var</span> numArr1 =<span style="color: #000000;"> []
</span><span style="color: #0000ff;">for</span>(<span style="color: #0000ff;">var</span> i = 0, l = objArr.length; i &lt; l; i++<span style="color: #000000;"> ){
  numArr1.push( objArr[i].myLength() )
}
console.log(numArr1.join(</span>" ")) <span style="color: #008000;">//</span><span style="color: #008000;">result</span><span style="color: #008000;">
//</span><span style="color: #008000;"> arr after sort</span>
objArr.sort(<span style="color: #0000ff;">function</span><span style="color: #000000;">(a,b){
  </span><span style="color: #008000;">//</span><span style="color: #008000;"> stable sort</span>
  <span style="color: #008000;">//</span><span style="color: #008000;"> return (a.myLength() &gt; b.myLength()) === true? 1:-1;</span>
  <span style="color: #008000;">//</span><span style="color: #008000;"> unstable sort</span>
  <span style="color: #0000ff;">return</span> (a.myLength() &gt;= b.myLength()) === <span style="color: #0000ff;">true</span>? 1:-1<span style="color: #000000;">;</span>
  <span style="color: #008000;">//</span><span style="color: #008000;"> return a.myLength() - b.myLength();</span><span style="color: #000000;">
})
</span><span style="color: #0000ff;">var</span> numArr2 =<span style="color: #000000;"> []
</span><span style="color: #0000ff;">for</span>(<span style="color: #0000ff;">var</span> i = 0, l = objArr.length; i &lt; l; i++<span style="color: #000000;"> ){
  </span><span style="color: #008000;">//</span><span style="color: #008000;"> console.log(i,l,objArr[i].myLength());</span>
<span style="color: #000000;">  numArr2.push( objArr[i].myLength() )
}
console.log(numArr2.join(</span>" ")) <span style="color: #008000;">//</span><span style="color: #008000;">result</span></pre>
</div>

感觉突然自己的想法和别人的有点不同（不好的方向）。

&nbsp;

**题目四：利用JavaScript打印出Fibonacci数（不使用全局变量）**

这个问题，写完之后我看了下其他人的写法，一半一半都没写中间缓存保存，我觉得这也是大叔表明不适用全局变量的原因，我把两种方式都写了进去。

这个是有缓存的，

<div class="cnblogs_code">
<pre><span style="color: #0000ff;">var</span> fibonacci = (<span style="color: #0000ff;">function</span><span style="color: #000000;">(){
  </span><span style="color: #0000ff;">var</span> s =<span style="color: #000000;"> [];
  </span><span style="color: #0000ff;">var</span> fun = <span style="color: #0000ff;">function</span><span style="color: #000000;">(x) {
    </span><span style="color: #0000ff;">if</span><span style="color: #000000;">(s[x]){
      </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> s[x];
    }
    </span><span style="color: #0000ff;">if</span>(x &lt; 0<span style="color: #000000;">) {
      </span><span style="color: #0000ff;">throw</span> "Can't be negative"<span style="color: #000000;">;
      </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> ;
    }
    </span><span style="color: #0000ff;">else</span> <span style="color: #0000ff;">if</span>(x === 0 || x === 1<span style="color: #000000;">) {
      s[x] </span>= s[x] ||<span style="color: #000000;"> x;
      </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> s[x];
    }
    </span><span style="color: #0000ff;">else</span><span style="color: #000000;">{
      s[x] </span>= ( fun(x - 1) + fun(x - 2<span style="color: #000000;">) );
      </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> s[x];
    }
  };
  fun.print </span>= <span style="color: #0000ff;">function</span><span style="color: #000000;">() {
    console.log(s.join(</span>" "<span style="color: #000000;">));
  }
  fun.printLast </span>= <span style="color: #0000ff;">function</span><span style="color: #000000;">() {
    </span><span style="color: #008000;">//</span><span style="color: #008000;"> console.log(s.length);</span>
    <span style="color: #0000ff;">return</span>(s[s.length-1<span style="color: #000000;">]);
  }
  window.s </span>=<span style="color: #000000;"> s;
  </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> fun;

})()
console.time(</span>200<span style="color: #000000;">);
console.log(fibonacci(</span>200<span style="color: #000000;">));
console.log(fibonacci.printLast());
console.log(fibonacci.print());
console.timeEnd(</span>200);</pre>
</div>

测试几百几千位的时间不足1000ms。

这个是递归无缓存的，

<div class="cnblogs_code">
<pre><span style="color: #0000ff;">var</span> fibonacci2 = <span style="color: #0000ff;">function</span><span style="color: #000000;">(x){
  </span><span style="color: #0000ff;">if</span>(x &lt; 0<span style="color: #000000;">) {
    </span><span style="color: #0000ff;">throw</span> "Can't be negative"<span style="color: #000000;">;
    </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> ;
  }
  </span><span style="color: #0000ff;">if</span>(x === 0 || x === 1<span style="color: #000000;">) {
    </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> x;
  }
  </span><span style="color: #0000ff;">var</span> num = ( fibonacci2(x - 1) + fibonacci2(x - 2<span style="color: #000000;">) )
  </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> num;
}
console.time(</span>32<span style="color: #000000;">);
console.log(fibonacci2(</span>32<span style="color: #000000;">));
console.timeEnd(</span>32);</pre>
</div>

测试个32位已经4000ms+，时间呈数量级增长，太坑。

**题目五：实现如下语法的功能：var a = (5).plus(3).minus(6); //2**

这个算是最简单的吧，但是我居然和别人的不一样，都能运行。

<div class="cnblogs_code">
<pre>Number.prototype.plus = <span style="color: #0000ff;">function</span><span style="color: #000000;">(x) {
  </span><span style="color: #0000ff;">var</span> num = <span style="color: #0000ff;">this</span>.valueOf() +<span style="color: #000000;"> x;
  </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> Number(num);
}
Number.prototype.minus </span>= <span style="color: #0000ff;">function</span><span style="color: #000000;">(x) {
  </span><span style="color: #0000ff;">var</span> num = <span style="color: #0000ff;">this</span>.valueOf() -<span style="color: #000000;"> x;
  </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> Number(num);
}

</span><span style="color: #0000ff;">var</span> a = (5).plus(3).minus(6<span style="color: #000000;">);
console.log(a);
alert(a);</span></pre>
</div>

人家直接返回一个num，我返回一个Number封装的num对象，其实都一样是Number对象。

**题目六：实现如下语法的功能：var a = add(2)(3)(4); //9**

这个题目算是第一个做出来的题目，因为我觉得这个题目的要求最简单，一看就记得，半夜睡醒了在床上直接脑袋打草稿运行了。

<div class="cnblogs_code">
<pre><span style="color: #0000ff;">function</span><span style="color: #000000;"> add(x) {
  </span><span style="color: #0000ff;">var</span><span style="color: #000000;"> mid;
  mid </span>= x || 0<span style="color: #000000;">;
  </span><span style="color: #0000ff;">function</span><span style="color: #000000;"> addObj(x) {
    x </span>= x || 0<span style="color: #000000;">;
    mid </span>= mid +<span style="color: #000000;"> x;
    </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> addObj;
  }
  addObj.valueOf </span>= <span style="color: #0000ff;">function</span><span style="color: #000000;">() {
    </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> mid;
  }
  addObj.toString </span>= <span style="color: #0000ff;">function</span><span style="color: #000000;">() {
    </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> mid;
  }
  </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> addObj;
}
</span><span style="color: #008000;">//</span><span style="color: #008000;">call the obj.valueOf function</span>
console.log(add(2<span style="color: #000000;">));
console.log(add(</span>2)(3<span style="color: #000000;">));
console.log(add(</span>2)(3)(4<span style="color: #000000;">));
console.log(add(</span>2)(3)(4)(5<span style="color: #000000;">));

</span><span style="color: #008000;">//</span><span style="color: #008000;">call the obj.toString function</span>
alert(add(2<span style="color: #000000;">));
alert(add(</span>2)(3<span style="color: #000000;">));
alert(add(</span>2)(3)(4<span style="color: #000000;">));
alert(add(</span>2)(3)(4)(5));</pre>
</div>

&nbsp;能无限调用。

&nbsp;

写完上述代码，我参考了下原文评论里面的，看了下自己的代码，和别人的比较下，有好的地方，也有不足之处，不过我的代码比较浅显，不想部分人写的那些看了很久才看明白，特别是那个写了缓存的fibonacci数列的答案。