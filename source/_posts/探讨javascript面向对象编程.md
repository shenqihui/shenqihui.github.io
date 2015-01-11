title: 探讨javascript面向对象编程
tags: []
date: 2014-02-12 05:58:00
---

(个人blog迁移文章。)

**前言：**

下面将探讨javascript面向对象编程的知识。

&nbsp;

请不要刻意把javascript想成面向对象编程是理所当然的。
<!--more-->
javascript里面，对象思想不可少，但是不一定需要面向对象编程，有时候，我们需要的只是一个实例化了的对象，而不是一个创建对象的类。

偏要这样做的话，也行，请看下文。另外请勿与传统面向对象编程做对比，这没有可比性。

&nbsp;

对于javascript来说，所有的变量都可以被称为对象。例如：

<pre>var a = 'hello world';
console.log(a.toUpperCase());</pre>

这里面，a为字符串对象。有其能直接调用的方法。但是这篇文章不讨论这一类的变量，而是讨论如何自定义对象。

**声明一个对象：**

<pre>var obj1 = {};
var obj2 = new Object();<span>&nbsp;</span></pre>

通过上面这两种方式中任意一种，就就声明了一个对象变量，这是一个实例，而且，是一个空对象,不能继承。

何为空对象，就是这个对象里面没有定义任何成员和方法。

**设置对象成员和方法：**

<pre>var Person = {};
Person.name = 'Tom';
Person.gender = 'male';
Person.sayHello = function () {
  console.log("Hello "+this.name+".");
}</pre>

这是一种最直观最简单的对象定义及成员方法添加的方法，里面定义了person对象，person有name和gender的成员，以及sayHello的方法。这也是一个实例，不能继承。通过person.name/persion.gender能直接引用该对象的成员，person.sayHello()能直接调用该对象的方法。这算基础。

在sayHello方法中，this指向的就是person，和其他的面向对象编程方法相同。

上面声明对象的方法太过于累赘，一般选择下面这种对象声明的方法。

<pre>var Person = {
  name:'Tom',
  gender:'male',
  sayHello:function() {
    console.log("Hello "+this.name+".");
  }
}<span>&nbsp;</span></pre>

这样的声明方法比上面的方法都简洁，首推方法。成员方法调用方式一样。

**声明一个可继承的类：**

**情景一：**

<pre>var Person = function (name) {
  this.name = name || 'NoName';
};
Person.sayHello = function () {
  console.log("Hello "+this.name+".");
}
var Tom = new Person();</pre>

这样子，就等于声明了一个person的类，Tom就是person的一个实例。但是person.sayHello方法就等于是私有属性，不能被继承，所有Tom没有sayHello的方法。

**情景二：**

<pre>var Person = function (name) {
  this.name = name||"NoName";
  this.sayHello = function () {
    console.log("Hello "+this.name+".");
  }
};
var Tom = new Person('Tom');
Tom.sayHello();<span>&nbsp;</span></pre>

这样也是定义对象的一个方法，person是一个类，其name和sayHello可被实例继承。但是有一个缺陷，如果通过此类创建多个实例，那么这个类就存在多少份的复制，就如上面来说，创建多个实例：

<pre>var Tom1 = new Person("Tom1");
var Tom2 = new Person("Tom2");
var Tom3 = new Person("Tom3");</pre>

此时，Person就存在三个实例，每个实例有自己的成员和方法，内存中有三个sayHello方法的引用。sayHello作为一个通用的方法，这样定义的话，在新建多个实例时，就会造成内存的浪费。因此，应该把通用的方法使用原型链的方式定义，请看情景三。

**情景三：**

<pre>var Person = function (name) {
  this.name = name||"NoName";
};
Person.prototype.sayHello = function () {
  console.log("Hello "+this.name+".");
}
var Tom = new Person('Tom');
Tom.sayHello();<span>&nbsp;</span></pre>

通过原型链的方式，基于这个类新建的实例，其方法就不会再内存里面存在多个实例。

但是此时，又涉及一个问题，如何知道Tom属于哪个类的呢，通过哪个构造函数来创建的呢？就引申到情景四了。

**情景四：**

这里，讨论的是实例的构造函数，每一个对象都有一个construcor的成员方法，指向的是创建该对象的那个函数。

例如：

<pre>var arr1 = [1,2,3,4,5]; //此时arr1.constructor就是Array。
var func = function() {};//此时func.constructor就是Function。<span>&nbsp;</span></pre>

因此，情景三中的Tom.constructor 就是 Person，就是

<pre>function (name) {
  this.name = name||"NoName";
};</pre>

这一个函数。通过new运算符创建的实例，该实例成员constructor所指向的就是new后面的变量。

题外话，说说new运算符，MDN上面[关于new运算符的定义](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)是这样的：

> The&nbsp;new&nbsp;operator creates an instance of a user-defined object type or of one of the built-in object types that has a constructor function.

大意是：new运算符能为那些存在构造函数的用户自定义对象类型或者浏览器内部实现对象类型创建一个实例。

new的语法格式为

<pre>new constructor[([arguments])];<span>&nbsp;</span></pre>

可以明显看出 实例的成员constructor就是创建该实例的对象类型。

上面的四个情景，都不能说是面向对象编程，因为，还没有实现类的继承，只实现了类的创建实例。下面情景五来探讨如何继承类。

**情景五：**

不推荐用原生的写法进行面向对象编程，因为确实非常麻烦，推荐使用coffeescript进行面向对象的编程，甚至所有的javascript的编写，能转coffeescript就全部转，你会发现，使用coffeescript写出来的代码非常的优雅，而且，你将全部精力投入的是如何巧妙的设计代码，而不是堆代码的时代。

当然，这里还是会讲讲如何通过原生javascript的方式实现javascript的继承。不过，真的很麻烦。

首先，得要一个extends，把它看成new级别的东西吧。

<pre>var __extends = function(child,father) {
  for(var property in father) {
    child[property] = father[property];
  }
}
var Animal = function (name) {
  this.name = name;
}
Animal.sayHello = function () {
  console.log("Hello "+this.name);
}
var Cat = function (name) {
  this.name = name;
}
__extends(Cat,Animal);
Cat.sayHello();</pre>

&nbsp;<span>这是一种继承的方式，要完美实现，这还是不足的。代码量好大啊。还是使用coffeescript来写吧。</span>

**情景六：**

<span>在情景五中，Cat继承了Animal的sayHello的方法。但是，如果改成&nbsp;Animal.prototype.sayHello = function () {}的话，Cat类就没法继承了，这就是上面那种简单写法的缺陷。</span>

所以需要把prototype的属性也要继承，所以必须把__extends函数重新写，注意prototype对于所有其派生类都是指向同一个内存空间的，修改父类对象的prototype将影响所有的子类。

<pre>var __extends = function(child,father) {
  for(var property in father) {
    child[property] = father[property];
  }
  function ctor() { 
    this.constructor = child; 
  } 
  ctor.prototype = parent.prototype; 
  child.prototype = new ctor(); 
  child.__super__ = father.prototype; 
}</pre>

很麻烦是吧，而且也不知道会不会出错。那您也应该尝试coffeescript的写法了。

**情景七：**

所以，还是来试试coffeescript的写法吧

<pre>class Animal
  constructor:(@name) -&gt;
  sayHello:-&gt;
    console.log "Hello #{this.name}."
    return
class Cat extends Animal
  sayHello:-&gt;
  console.log "喵喵喵喵喵喵，#{this.name}"
class Dog extends Animal
  sayHello:-&gt;
  console.log "汪汪汪汪汪汪，#{this.name}"
cat1 = new Cat "kitty"
dog1 = new Don "哈士奇"</pre>

&nbsp;通过coffeescript写出一个javascript对象继承，代码就是这么简洁。

&nbsp;在这里面，就定义了Animal类，还有派生类Cat和Dog，分别覆盖了父类的sayHello的方法。写完之后，直接使用[koala](http://koala-app.com/)编译一下，马上一段完美的继承代码生成了。

**结语：**

至此，此片面向对象的文章算是草草结束了，断断续续写了一个星期，就写成了这样子，比较糟糕。大家不妨看看下面的参考文献。

**参考文献：**

1.  [new](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new "new operator")
2.  [JavaScript类和继承：constructor属性](http://developer.51cto.com/art/200907/134913.htm "javascript类和继承")
3.  [koala](http://koala-app.com/ "koala")
4.  [coffeescript](http://coffeescript.org/ "coffeescript")

觉得对您有帮助，点个赞。赞赞更健康。