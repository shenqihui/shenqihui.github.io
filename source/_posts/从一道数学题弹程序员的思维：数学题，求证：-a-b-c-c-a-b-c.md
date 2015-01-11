title: "从一道数学题弹程序员的思维：数学题，求证：(a+b%c)%c=(a+b)%c"
tags: []
date: 2014-02-08 03:36:00
---

在学校论坛看到这道题目，全忘了的感觉。

如果你是高中的，那我觉得你完全没问题。但是，在这个博客园的圈子，觉得全部人都是程(ban)序(zhuan)员(gong)相关的人员，解决这个问题有点难度，毕竟，想法已经偏了。

<!--more-->

有句话说得好，如果你拿着一个锤子，那你看什么都像一个钉子。

因此程序员必要的时候必须转换下思路啊。程序员思维是：已知条件，求值；而不是已知 条件 和 值，求证：这求值过程不存在bug。

如果有人叫你这么证明你的程序的求值过程正确，你会不会抡起你的键(zhuan)盘(tou)就拍过去了。

我们能做到的只是，带入a=*,b=**,c=***，验证等式成立。数学题让数学家证明去吧。

&nbsp;

&nbsp;

下面回到高中的想法，谈谈这道题目吧：

<div class="cnblogs_code">
<pre>求证：(a+b%c)%c=(a+<span style="color: #000000;">b)%c
解：

　　假设等式左右边的值为 v，

　　则 存在整数x和y，使得下面等式成立。

　　a</span>+b%c = v +<span style="color: #000000;"> xc;（左边）

　　a</span>+b     = v +<span style="color: #000000;"> yc;（右边）

　　这两式子同时成立，则可以化简为：

　　存在整数 z 使得 z</span>*c = b -<span style="color: #000000;"> b%c 成立。

　　则证明 b </span>-<span style="color: #000000;"> b%c 为 c 的倍数。

　　显然 b </span>- b%c 为 c 的倍数。</pre>
</div>

<span style="line-height: 1.5;">（</span><span style="line-height: 1.5;">　　感觉我自己也跑歪了，如果(b - b%c 为 c 的倍数)不是显然的话，我们还做什么程序员。</span>

<span style="line-height: 1.5;">其实 &nbsp;</span><span style="line-height: 1.5;">(a+b%c)%c=(a+b)%c 也是显然的。</span><span style="line-height: 1.5;">）</span>

&nbsp;

后注：发表了出来，才发现，其实这道题跟程序员思维没啥联系。纯当胡扯。

&nbsp;

下面是整理一楼&nbsp;[五岳](http://home.cnblogs.com/u/228024/)&nbsp;提供的正确方法，谢谢指导。（我的答案已经跑歪了）

<div class="cnblogs_code">
<pre><span style="color: #000000;">假设：
　　a </span>= x*c +<span style="color: #000000;"> a0
　　b </span>= y*c +<span style="color: #000000;"> b0
　　其中x,y,a0,b0&isin;Z,且|a0|</span>&lt;|c|,|b0|&lt;<span style="color: #000000;">|c|
　　那么
　　(a</span>+b%c)%c = (x*c + a0 + (y*c + b0)%c)=(x*c +a0 + b0)%c = (a0 +<span style="color: #000000;"> b0)%c
　　而(a</span>+b)%c = (x*c + a0 + y*c + b0)%c = (a0+<span style="color: #000000;">b0)%c
　　两式相等，得证</span></pre>
</div>

&nbsp;

&nbsp;