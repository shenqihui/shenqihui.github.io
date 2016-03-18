title: 'javascript 函数劫持'
tags: [javascript,技术,前端]
date: 2015-02-12 00:38:04

---


最近在搞坏事，因此总会有一些很猥琐很猥琐的想法。  
具体有多少，只有你想不到，没有做不到。   
这里就来讲讲如何在 js 层面，神不知鬼不觉的劫持函数。

<!--more-->

## 函数劫持是什么？

这里所说的函数劫持，是在不改变原有功能的前提下，注入自己想要的功能。  
改变原有功能的劫持方式简单粗暴，这里不推荐这种想法。  
我们要做的，就是天知地知你知我知其他人不知。  

## 函数劫持能干什么？

首先你得明白为什么要劫持。  
一旦你明白了为什么要劫持，就需要找劫持点，进行函数重写劫持。  
具体在这个重写之后的函数增加什么功能，就看你为什么要劫持了。  
函数劫持了，你想干什么，就能干什么。

## 劫持的原理
一般的劫持原理都是一个思路：  
一、使用新的变量保存即将被劫持的函数。  
二、改写被劫持函数的功能。  
三、在被劫持函数的末尾段（或者其他适当部位）重新调用重写之前的函数。  

## 如何进行劫持

先来看看下面这段代码。  

```javascript
// save old ajax
$._ajax = $.ajax;
// incase something.
function noop() {}
// 我想要加入的功能
function myFunctionToHack(data) {
  console.log(data);
  // do something you want
}
// accord $.ajax to change
function ajaxHacker(e, n) {
  // old success function
  e._success = e.success || noop;
  // new success function of lucky money
  e.success = function success(data) {
    myFunctionToHack(data);

    e._success.call(this, data);
    
  };
  $._ajax(e, n);
}
// change default ajax
$.ajax = ajaxHacker;
```

这段代码的作用估计大家都一目了然。  
主要的功能就是重写 jquery 的 ajax 请求函数，在原生的 ajax 功能的基础上，劫持 success 回调功能。

具体劫持方式：

### 使用新的变量保存即将被劫持的函数
  
```javascript
$._ajax = $.ajax;  
e._success = e.success || noop;
```
保存旧方法方便调用。

### 改写被劫持函数的功能

```javascript
$.ajax = ajaxHacker;
e.success = function success(data) {
  // ...
}
```
把 `jquery` 的 `ajax` 替换为 `ajaxHacker` 函数，实现就功能的改写。

### 在被劫持函数的末尾段重新调用重写之前的函数

为了保持功能与原来的基本一致，需要重新调用原来的函数。  
一般情况下面都是在处理完毕自己想要的功能之后调用。这些都看个人习惯进行。   
由于上面的代码有两个函数劫持，所以分开来讲：  

先看一个简单的： 

```javascript
function ajaxHacker(e, n) {
  // ...
  
  $._ajax(e, n);
}
```
这个时候，旧的 `jquery` `ajax` 功能就能在 `ajaxHacker` 执行末尾调用，  
中途就能增加自己想要的功能了。

复杂点的：

```javascript
e.success = function success(data) {
  // ...
  myFunctionToHack(data);

  e._success.call(this, data);
    
};
```

`success` 回调函数保存在 `e._success` 里面，重写了 `success` 功能之后，重新调用 `e._success`。
但是这个时候使用了 `call` 进行调用，原因就是避免函数运行环境 `this` 对象变化了。使用 `call` 能够确保劫持之前的运行上下文与劫持之后的运行上下文一致。  
当然如果 `this` 对象没被使用的话，不使用 `call` 也是可以的，  

```javascript
e._success(data);
```
这样子调用，也行。

另外也可以使用 `apply` 代替 `call` ，两者都能操控 `this` 。

PS: 第二个例子，不使用 `call` 其 `this` 对象也是 `e`。因为使用了命名空间的方式进行了调用。如果不是使用 `e._success` 而是使用 `_success` 保存就函数，就必须使用 `call` 或者 `apply` 来确保运行上下文正确。