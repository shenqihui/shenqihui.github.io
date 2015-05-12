title: 探讨javascript面向对象编程
tags: []
date: 2014-02-12 05:58:00
---

**前言：**

下面将探讨 javascript 面向对象编程的知识。

请不要刻意把 javascript 想成面向对象编程是理所当然的。
<!--more-->
javascript 里面，对象思想不可少，但是不一定需要面向对象编程，有时候，我们需要的只是一个实例化了的对象，而不是一个创建对象的类。

偏要这样做的话，也行，请看下文。另外请勿与传统面向对象编程做对比，这没有可比性。

对于 javascript 来说，所有的变量都可以被称为对象。例如：

```javascript
var a = 'hello world';
console.log(a.toUpperCase());
```

这里面，a为字符串对象。有其能直接调用的方法。但是这篇文章不讨论这一类的变量，而是讨论如何自定义对象。

**声明一个对象：**

```javascript
var obj1 = {};
var obj2 = new Object();
```

通过上面这两种方式中任意一种，就就声明了一个对象变量，这是一个实例，而且，是一个空对象,不能继承。

何为空对象，就是这个对象里面没有定义任何成员和方法。

**设置对象成员和方法：**

```javascript
var Person = {};
Person.name = 'Tom';
Person.gender = 'male';
Person.sayHello = function () {
  console.log("Hello "+this.name+".");
}
```

这是一种最直观最简单的对象定义及成员方法添加的方法，里面定义了 person 对象，person 有 name 和 gender 的成员，以及 sayHello 的方法。这也是一个实例，不能继承。通过 person.name/persion.gender 能直接引用该对象的成员，person.sayHello() 能直接调用该对象的方法。这算基础。

在 sayHello 方法中，this 指向的就是 person，和其他的面向对象编程方法相同。

上面声明对象的方法太过于累赘，一般选择下面这种对象声明的方法。

```javascript
var Person = {
  name:'Tom',
  gender:'male',
  sayHello:function() {
    console.log("Hello "+this.name+".");
  }
}
```

这样的声明方法比上面的方法都简洁，首推方法。成员方法调用方式一样。

**声明一个可继承的类：**

**情景一：**

```javascript
var Person = function (name) {
  this.name = name || 'NoName';
};
Person.sayHello = function () {
  console.log("Hello "+this.name+".");
}
var Tom = new Person();
```

这样子，就等于声明了一个 person 的类，Tom 就是 person 的一个实例。但是 person.sayHello 方法就等于是私有属性，不能被继承，所有 Tom 没有 sayHello 的方法。

**情景二：**

```javascript
var Person = function (name) {
  this.name = name||"NoName";
  this.sayHello = function () {
    console.log("Hello "+this.name+".");
  }
};
var Tom = new Person('Tom');
Tom.sayHello();
```

这样也是定义对象的一个方法，person 是一个类，其 name 和 sayHello 可被实例继承。但是有一个缺陷，如果通过此类创建多个实例，那么这个类就存在多少份的复制，就如上面来说，创建多个实例：

```javascript
var Tom1 = new Person("Tom1");
var Tom2 = new Person("Tom2");
var Tom3 = new Person("Tom3");
```

此时，Person 就存在三个实例，每个实例有自己的成员和方法，内存中有三个 sayHello 方法的引用。sayHello 作为一个通用的方法，这样定义的话，在新建多个实例时，就会造成内存的浪费。因此，应该把通用的方法使用原型链的方式定义，请看情景三。

**情景三：**

```javascript
var Person = function (name) {
  this.name = name||"NoName";
};
Person.prototype.sayHello = function () {
  console.log("Hello "+this.name+".");
}
var Tom = new Person('Tom');
Tom.sayHello();
```

通过原型链的方式，基于这个类新建的实例，其方法就不会再内存里面存在多个实例。

但是此时，又涉及一个问题，如何知道 Tom 属于哪个类的呢，通过哪个构造函数来创建的呢？就引申到情景四了。

**情景四：**

这里，讨论的是实例的构造函数，每一个对象都有一个 construcor 的成员方法，指向的是创建该对象的那个函数。

例如：

```javascript
var arr1 = [1,2,3,4,5]; //此时arr1.constructor就是Array。
var func = function() {};//此时func.constructor就是Function。
```

因此，情景三中的 Tom.constructor 就是 Person，就是

```javascript
function (name) {
  this.name = name||"NoName";
};
```

这一个函数。通过 new 运算符创建的实例，该实例成员 constructor 所指向的就是 new 后面的变量。

题外话，说说 new 运算符，MDN 上面[关于new运算符的定义](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new)是这样的：

> The new operator creates an instance of a user-defined object type or of one of the built-in object types that has a constructor function.

大意是：new 运算符能为那些存在构造函数的用户自定义对象类型或者浏览器内部实现对象类型创建一个实例。

new的语法格式为

```javascript
new constructor[([arguments])];
```

可以明显看出 实例的成员 constructor 就是创建该实例的对象类型。

上面的四个情景，都不能说是面向对象编程，因为，还没有实现类的继承，只实现了类的创建实例。下面情景五来探讨如何继承类。

**情景五：**

不推荐用原生的写法进行面向对象编程，因为确实非常麻烦，推荐使用 coffeescript 进行面向对象的编程，甚至所有的 javascript 的编写，能转 coffeescript 就全部转，你会发现，使用 coffeescript 写出来的代码非常的优雅，而且，你将全部精力投入的是如何巧妙的设计代码，而不是堆代码的时代。

当然，这里还是会讲讲如何通过原生 javascript 的方式实现 javascript 的继承。不过，真的很麻烦。

首先，得要一个 extends，把它看成 new 级别的东西吧。

```javascript
var __extends = function(child,father) {
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
Cat.sayHello();
```

这是一种继承的方式，要完美实现，这还是不足的。代码量好大啊。还是使用 coffeescript 来写吧。

**情景六：**

在情景五中，Cat 继承了 Animal 的 sayHello 的方法。但是，如果改成 Animal.prototype.sayHello = function () {} 的话，Cat 类就没法继承了，这就是上面那种简单写法的缺陷。

所以需要把 prototype 的属性也要继承，所以必须把 __extends 函数重新写，注意 prototype 对于所有其派生类都是指向同一个内存空间的，修改父类对象的 prototype 将影响所有的子类。

```javascript
var __extends = function(child,father) {
  for(var property in father) {
    child[property] = father[property];
  }
  function ctor() { 
    this.constructor = child; 
  } 
  ctor.prototype = parent.prototype; 
  child.prototype = new ctor(); 
  child.__super__ = father.prototype; 
}
```

很麻烦是吧，而且也不知道会不会出错。那您也应该尝试 coffeescript 的写法了。

**情景七：**

所以，还是来试试coffeescript的写法吧

```javascript
class Animal
  constructor:(@name) ->
  sayHello:->
    console.log "Hello #{this.name}."
    return
class Cat extends Animal
  sayHello:->
  console.log "喵喵喵喵喵喵，#{this.name}"
class Dog extends Animal
  sayHello:->
  console.log "汪汪汪汪汪汪，#{this.name}"
cat1 = new Cat "kitty"
dog1 = new Don "哈士奇"
```

通过 coffeescript 写出一个 javascript 对象继承，代码就是这么简洁。

在这里面，就定义了 Animal 类，还有派生类 Cat 和 Dog，分别覆盖了父类的 sayHello 的方法。写完之后，直接使用 [koala](http://koala-app.com/)编译一下，马上一段完美的继承代码生成了。

**结语：**

至此，此片面向对象的文章算是草草结束了，断断续续写了一个星期，就写成了这样子，比较糟糕。大家不妨看看下面的参考文献。

**参考文献：**

1.  [new](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/new "new operator")
2.  [JavaScript类和继承：constructor属性](http://developer.51cto.com/art/200907/134913.htm "javascript类和继承")
3.  [koala](http://koala-app.com/ "koala")
4.  [coffeescript](http://coffeescript.org/ "coffeescript")

觉得对您有帮助，点个赞。赞赞更健康。