title: nodejs 平台的 webscoket 的实现
tags: []
date: 2013-08-07 04:43:00
---

新手入门，没办法，只能选择不断不断的google吧。

找了很多的例子都跑不了，不知道什么原因。

后，自己在git搜索吧，选择了一个下面的例子：&nbsp;**[nodejs-web-socket](https://github.com/kashiif/nodejs-web-socket)**

经过我的改造，改成我自己想要的方式。
<!--more-->
只是将客户端发送的数据直接原封不动发回客户端。

先说说运行环境：window 7 ，node&nbsp;v0.10.5，全局安装了websocket.io模块，chrome 28浏览器。

（注：以下提到的两个js文件放在同一层目录下面即可，html文件随便放置）

这是后台的js代码：

1、将其存为socketServer.js文件里面，并且进行module导出。

<div class="cnblogs_code">
<pre><span style="color: #008000;">/*</span><span style="color: #008000;">
  仅用于测试，
  客户端发送的东西将被服务器原封不动的返回到客户端
  运行环境：node v0.10.5
            window 7
            chromw 28
</span><span style="color: #008000;">*/</span>
<span style="color: #008000;">/*</span><span style="color: #008000;">var server = </span><span style="color: #008000;">*/</span>module.exports = ( <span style="color: #0000ff;">function</span><span style="color: #000000;">() {
  </span><span style="color: #0000ff;">var</span> ws = require('websocket.io'<span style="color: #000000;">);
  </span><span style="color: #0000ff;">var</span> socketServer = <span style="color: #0000ff;">null</span><span style="color: #000000;">;
  </span><span style="color: #0000ff;">var</span> socketInitListen = <span style="color: #0000ff;">function</span><span style="color: #000000;">(port) {
    socketServer </span>=<span style="color: #000000;"> ws.listen(port);
    socketServer.on(</span>'listening',<span style="color: #0000ff;">function</span><span style="color: #000000;">() {
      console.log(</span>'Socket server running'<span style="color: #000000;">);
    });
    socketServer.on(</span>'connection',<span style="color: #0000ff;">function</span><span style="color: #000000;">(socket) {
      console.log(</span>'Connected to client'<span style="color: #000000;">);
      socket.on(</span>'message', <span style="color: #0000ff;">function</span><span style="color: #000000;">(data) {
        </span><span style="color: #008000;">//</span><span style="color: #008000;"> client send message to server</span>
        console.log('Server received message : '<span style="color: #000000;">,data);
        socket.send(data);
      });
      socket.on(</span>'close',<span style="color: #0000ff;">function</span><span style="color: #000000;">() {
        socket.send(</span>'close'<span style="color: #000000;">);
      })
    })
  };
  </span><span style="color: #0000ff;">var</span> init = <span style="color: #0000ff;">function</span><span style="color: #000000;">(socketPort) {
    socketInitListen(socketPort);
  };
  </span><span style="color: #0000ff;">return</span><span style="color: #000000;"> {
    init: init
  };
})();

</span><span style="color: #008000;">//</span><span style="color: #008000;"> server.init(9000);</span></pre>
</div>

<span style="line-height: 1.5;">2、引用上面那个module的文件，并且将端口绑定为9000端口，存为文件server.js。</span>

<div class="cnblogs_code">
<pre><span style="color: #0000ff;">var</span> socketServer = require('./socketServer').init(9000);</pre>
</div>

3、页面的代码 ：index.html

<div class="cnblogs_code">
<pre><span style="color: #0000ff;">&lt;!</span><span style="color: #ff00ff;">DOCTYPE html</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;</span><span style="color: #800000;">html</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;</span><span style="color: #800000;">head</span><span style="color: #0000ff;">&gt;</span>
    <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">meta </span><span style="color: #ff0000;">charset</span><span style="color: #0000ff;">="utf-8"</span><span style="color: #0000ff;">&gt;</span>
  <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">title</span><span style="color: #0000ff;">&gt;</span>WebSockets Node.js<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">title</span><span style="color: #0000ff;">&gt;</span>
  <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">style</span><span style="color: #0000ff;">&gt;</span><span style="background-color: #f5f5f5; color: #800000;">
        .container</span><span style="background-color: #f5f5f5; color: #000000;">{</span><span style="background-color: #f5f5f5; color: #ff0000;">
            margin</span><span style="background-color: #f5f5f5; color: #000000;">:</span><span style="background-color: #f5f5f5; color: #0000ff;">auto</span><span style="background-color: #f5f5f5; color: #000000;">;</span><span style="background-color: #f5f5f5; color: #ff0000;">
            width</span><span style="background-color: #f5f5f5; color: #000000;">:</span><span style="background-color: #f5f5f5; color: #0000ff;">300px</span><span style="background-color: #f5f5f5; color: #000000;">;</span>
        <span style="background-color: #f5f5f5; color: #000000;">}</span><span style="background-color: #f5f5f5; color: #800000;">
        label,input</span><span style="background-color: #f5f5f5; color: #000000;">{</span><span style="background-color: #f5f5f5; color: #ff0000;">
            width</span><span style="background-color: #f5f5f5; color: #000000;">:</span><span style="background-color: #f5f5f5; color: #0000ff;">200px</span><span style="background-color: #f5f5f5; color: #000000;">;</span><span style="background-color: #f5f5f5; color: #ff0000;">
            float</span><span style="background-color: #f5f5f5; color: #000000;">:</span><span style="background-color: #f5f5f5; color: #0000ff;">left</span><span style="background-color: #f5f5f5; color: #000000;">;</span>
        <span style="background-color: #f5f5f5; color: #000000;">}</span><span style="background-color: #f5f5f5; color: #800000;">
        input[type=button]</span><span style="background-color: #f5f5f5; color: #000000;">{</span><span style="background-color: #f5f5f5; color: #ff0000;">
            float</span><span style="background-color: #f5f5f5; color: #000000;">:</span><span style="background-color: #f5f5f5; color: #0000ff;">right</span><span style="background-color: #f5f5f5; color: #000000;">;</span><span style="background-color: #f5f5f5; color: #ff0000;">
            width</span><span style="background-color: #f5f5f5; color: #000000;">:</span><span style="background-color: #f5f5f5; color: #0000ff;">80px</span><span style="background-color: #f5f5f5; color: #000000;">;</span>
        <span style="background-color: #f5f5f5; color: #000000;">}</span>
  <span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">style</span><span style="color: #0000ff;">&gt;</span>
  <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">script </span><span style="color: #ff0000;">src</span><span style="color: #0000ff;">="http://code.jquery.com/jquery.min.js"</span><span style="color: #0000ff;">&gt;&lt;/</span><span style="color: #800000;">script</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">head</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;</span><span style="color: #800000;">body</span><span style="color: #0000ff;">&gt;</span>
  <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">div </span><span style="color: #ff0000;">class</span><span style="color: #0000ff;">="container"</span><span style="color: #0000ff;">&gt;</span>
    <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">label </span><span style="color: #ff0000;">for</span><span style="color: #0000ff;">="content"</span><span style="color: #0000ff;">&gt;</span>发送的内容:<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">label</span><span style="color: #0000ff;">&gt;&lt;</span><span style="color: #800000;">input </span><span style="color: #ff0000;">type</span><span style="color: #0000ff;">="text"</span><span style="color: #ff0000;"> id</span><span style="color: #0000ff;">="content"</span><span style="color: #ff0000;"> value</span><span style="color: #0000ff;">="input something"</span> <span style="color: #0000ff;">/&gt;</span>
        <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">label </span><span style="color: #ff0000;">for</span><span style="color: #0000ff;">="recive"</span><span style="color: #0000ff;">&gt;</span>收到的内容:<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">label</span><span style="color: #0000ff;">&gt;&lt;</span><span style="color: #800000;">input </span><span style="color: #ff0000;">type</span><span style="color: #0000ff;">="text"</span><span style="color: #ff0000;"> id</span><span style="color: #0000ff;">="recive"</span> <span style="color: #0000ff;">/&gt;</span>
    <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">input </span><span style="color: #ff0000;">type</span><span style="color: #0000ff;">="button"</span><span style="color: #ff0000;"> id</span><span style="color: #0000ff;">="send"</span><span style="color: #ff0000;"> value</span><span style="color: #0000ff;">="点击发送"</span> <span style="color: #0000ff;">/&gt;</span>
  <span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">div</span><span style="color: #0000ff;">&gt;</span>
  <span style="color: #0000ff;">&lt;</span><span style="color: #800000;">script</span><span style="color: #0000ff;">&gt;</span>
      <span style="background-color: #f5f5f5; color: #008000;">//</span><span style="background-color: #f5f5f5; color: #008000;"> websocket 连接变量</span>
    <span style="background-color: #f5f5f5; color: #0000ff;">var</span><span style="background-color: #f5f5f5; color: #000000;"> wsConn;
    (</span><span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;"> () {
      </span><span style="background-color: #f5f5f5; color: #0000ff;">try</span><span style="background-color: #f5f5f5; color: #000000;"> {
        wsConn </span><span style="background-color: #f5f5f5; color: #000000;">=</span> <span style="background-color: #f5f5f5; color: #0000ff;">new</span><span style="background-color: #f5f5f5; color: #000000;"> WebSocket(</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">ws://127.0.0.1:9000</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">);
      } </span><span style="background-color: #f5f5f5; color: #0000ff;">catch</span><span style="background-color: #f5f5f5; color: #000000;"> (e) {
        console.log(</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">websocket 连接出错。</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">);
        console.log(e);
      }
    })();

    $(</span><span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;">() {
      </span><span style="background-color: #f5f5f5; color: #0000ff;">if</span><span style="background-color: #f5f5f5; color: #000000;"> (wsConn) {
        wsConn.onopen </span><span style="background-color: #f5f5f5; color: #000000;">=</span> <span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;">() {
          console.log(</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">open Connection.</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">);
        };
        wsConn.onmessage </span><span style="background-color: #f5f5f5; color: #000000;">=</span> <span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;">(msg) {
          console.log(</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">onmessage.</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">);
          console.log(msg.data);
          $(</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">#recive</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">).val(msg.data);
        };
        wsConn.onerror </span><span style="background-color: #f5f5f5; color: #000000;">=</span> <span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;">(msg) {
          console.log(</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">onerror.</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">);
          console.log(msg);
        };
        wsConn.onclose </span><span style="background-color: #f5f5f5; color: #000000;">=</span> <span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;">(msg) {
          console.log(</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">onclose.</span><span style="background-color: #f5f5f5; color: #000000;">"</span><span style="background-color: #f5f5f5; color: #000000;">);
          console.log(msg);
        };
        </span><span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;"> wsConnSend(content) {
            wsConn.send(content);
        };
        $(</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">#send</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">).bind(</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">click</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">,</span><span style="background-color: #f5f5f5; color: #0000ff;">function</span><span style="background-color: #f5f5f5; color: #000000;"> sendClick() {
            wsConnSend($(</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">#content</span><span style="background-color: #f5f5f5; color: #000000;">'</span><span style="background-color: #f5f5f5; color: #000000;">).val())
        })
      }
    });
  </span><span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">script</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">body</span><span style="color: #0000ff;">&gt;</span>
<span style="color: #0000ff;">&lt;/</span><span style="color: #800000;">html</span><span style="color: #0000ff;">&gt;</span></pre>
</div>

这都是源码的三个文件。

运行的方法为：

1、安装node ，我的版本是0.10.5，其他版本没进行测试；

2、安装websocket.io，命令如下 npm i -g websocket.io；

3、环境弄好了，可以跑了，打开命令行，cd到当前目录，跑 node server.js。

4、直接用chrome以本地文件方式直接打开index.html ，里面操作简单。其他浏览器没进行测试。

搭建完毕。

这是控制台下面的一行命令的截图。

![](http://images.cnitblog.com/blog/358891/201308/07124246-07456af2379947258a81200c6353462e.png)

&nbsp;新手习作，若有出错，敬请大神指出。