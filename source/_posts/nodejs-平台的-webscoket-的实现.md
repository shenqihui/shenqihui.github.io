title: nodejs 平台的 webscoket 的实现
tags: [javascript,技术,前端]
date: 2013-08-07 04:43:00
---

新手入门，没办法，只能选择不断不断的 google 吧。

找了很多的例子都跑不了，不知道什么原因。

后，自己在 git 搜索吧，选择了一个下面的例子： **[nodejs-web-socket](https://github.com/kashiif/nodejs-web-socket)**

经过我的改造，改成我自己想要的方式。
<!--more-->
只是将客户端发送的数据直接原封不动发回客户端。

先说说运行环境：`window 7` ， `node v0.10.5`，全局安装了 `websocket.io` 模块，`chrome 28` 浏览器。

（注：以下提到的两个 js 文件放在同一层目录下面即可，html 文件随便放置）

这是后台的 js 代码：

1、将其存为 `socketServer.js` 文件里面，并且进行 `module` 导出。
```javascript
/*
  仅用于测试，
  客户端发送的东西将被服务器原封不动的返回到客户端
  运行环境：node v0.10.5
            window 7
            chromw 28
*/
/*var server = */module.exports = ( function() {
  var ws = require('websocket.io');
  var socketServer = null;
  var socketInitListen = function(port) {
    socketServer = ws.listen(port);
    socketServer.on('listening',function() {
      console.log('Socket server running');
    });
    socketServer.on('connection',function(socket) {
      console.log('Connected to client');
      socket.on('message', function(data) {
        // client send message to server
        console.log('Server received message : ',data);
        socket.send(data);
      });
      socket.on('close',function() {
        socket.send('close');
      })
    })
  };
  var init = function(socketPort) {
    socketInitListen(socketPort);
  };
  return {
    init: init
  };
})();

// server.init(9000);
```

2、引用上面那个module的文件，并且将端口绑定为9000端口，存为文件server.js。

```javascript
var socketServer = require('./socketServer').init(9000);
```

3、页面的代码 ：index.html

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
  <title>WebSockets Node.js</title>
  <style>
        .container{
            margin:auto;
            width:300px;
        }
        label,input{
            width:200px;
            float:left;
        }
        input[type=button]{
            float:right;
            width:80px;
        }
  </style>
  <script src="http://code.jquery.com/jquery.min.js"></script>
</head>
<body>
  <div class="container">
    <label for="content">发送的内容:</label><input type="text" id="content" value="input something" />
        <label for="recive">收到的内容:</label><input type="text" id="recive" />
    <input type="button" id="send" value="点击发送" />
  </div>
  <script>
      // websocket 连接变量
    var wsConn;
    (function () {
      try {
        wsConn = new WebSocket('ws://127.0.0.1:9000');
      } catch (e) {
        console.log("websocket 连接出错。");
        console.log(e);
      }
    })();
    
    $(function() {
      if (wsConn) {
        wsConn.onopen = function() {
          console.log("open Connection.");
        };
        wsConn.onmessage = function(msg) {
          console.log("onmessage.");
          console.log(msg.data);
          $('#recive').val(msg.data);
        };
        wsConn.onerror = function(msg) {
          console.log("onerror.");
          console.log(msg);
        };
        wsConn.onclose = function(msg) {
          console.log("onclose.");
          console.log(msg);
        };
        function wsConnSend(content) {
            wsConn.send(content);
        };
        $('#send').bind('click',function sendClick() {
            wsConnSend($('#content').val());
        });
      }
    });
  </script>
</body>
</html>
```

这都是源码的三个文件。

运行的方法为：

1、安装`node` ，我的版本是 `0.10.5`，其他版本没进行测试；

2、安装 `websocket.io`，命令如下 `npm i -g websocket.io`；

3、环境弄好了，可以跑了，打开命令行，cd 到当前目录，跑 `node server.js`。

4、直接用 chrome 以本地文件方式直接打开 `index.html` ，里面操作简单。其他浏览器没进行测试。当然以 http 形式访问更好。

搭建完毕。

这是控制台下面的一行命令的截图。

![](http://images.cnitblog.com/blog/358891/201308/07124246-07456af2379947258a81200c6353462e.png)

新手习作，若有出错，敬请大神指出。