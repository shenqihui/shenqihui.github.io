title: "Django 框架关于 IE 跨域 XDomainRequest 传输的问题"
tags: ["django", "ie", "ajax", "XDomainRequest", "corf"]
date: 2015-08-14 13:24:01
---

Django 是一个强大的 Web 框架。  
不过，  
最近在处理各种跨域传输的问题，其中就遇到了一个坑： Django 服务下 IE 8、9 下面通过 XDomainRequest 无法传输数据的问题。  
<!--more-->

---

# 事情是这样子的。

1、 开发了一个接口，处理 POST 的 http 请求，在各类型 XMLHttpRequest 方法下面的 POST 请求基本处理通过来进行数据传输都能实现， request 的 POST 数据都能获取。
2、 不过，在 IE 8/9 的时候，使用 XDomainRequest 来进行跨域 POST 传输的时候，却没能获取到 POST 数据。

# 然后

事情就是这样，一开始还以为是 XDomainRequest 的 Ajax 请求代码出问题了。后面经过一番调试，越发觉得这不是 js 代码出问题了，而是 Django 解析出问题了。

# 所以

所以我就要测试，到底是我的 js 代码写错了，还是我的猜测正确了。经过验证，确实是 Django 解析这种请求出问题了。所以，就写下了这篇文章。

---

## 验证过程   

然后我就开始验证这个过程了。

### 后端开发不同的 http 服务

#### nodejs 的 http 服务

使用 nodejs 开发一个 http 服务来处理 POST 请求，横向对比 js 代码是否正确，代码很少，能实现功能就行，如下：

```
var http = require('http');

http.createServer(function (req, res) {
  var body = '';
  req.on('data', function (chunk) {
    body += chunk;
  });
  req.on('end', function () {
    console.log('POSTed: ' + body);
    res.writeHead(200, {
      'Content-Type': 'text/html',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': '*',
      'Pragma': 'no-cache'
    });
    res.end('POSTed: ' + body);
  });
}).listen(3001);
```
使用过程，保存为 `node.js`， 然后直接运行 `node node.js` 即可，监听了 3001 端口的 http 服务。

#### django 的 http 服务

这个用来检验，

核心代码如下：
1、 `views.py` 的：
```
import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    if request.method == 'POST':
        data = request.POST
        print 'POSTed: ', data
        response = HttpResponse('POSTed: ' + json.dumps(data), content_type='text/html')
    elif request.method == 'GET':
        response = HttpResponse('Please use post method', content_type='text/html')
    else:
        response = HttpResponse('What', content_type='text/html')

    response['Access-Control-Allow-Origin'] = '*'
    response['Access-Control-Allow-Headers'] = '*'
    response['Pragma'] = 'no-cache'

    return response
```

2、 `urls.py` 的：
```
url(r'^$', 'some_app.views.index', name='test_post'),
```
使用过程，保存为 django 的 `some_app` 对应的 views， 增加到 url 路由中， 然后直接运行 `python manage.py runserver 0.0.0.0:3002` 即可，监听了 3002 端口的 http 服务。

### 前端 js 代码请求。

贴全部出了了。
```
<html>
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <title>test post whit django and nodejs</title>
    <style>
      .red {
        color: red;
      }
    </style>
  </head>
  <body>
    <h1>Test Django POST Request Method</h1>
    <h3>core code</h3>
    <pre>
      var host = location.hostname;
      var sendTimeout = 0;
      var ajax = function(url, type) {
        var xdr = new XDomainRequest();
        xdr.open('POST', url);
        xdr.timeout = 1200;
        xdr.onload = function(){
          console.log(type + ': ', this.responseText);
          document.getElementById(type).innerHTML = type + ' respone: &lt;span class="red"&gt;'
            + this.responseText + '&lt;/span&gt;';
        }
        xdr.onerror = function() {
          console.log('node error', this);
        }
        setTimeout(function() {
          xdr.send('param1=value1&param2=value2');
        }, sendTimeout)
      }
    </pre>
    <hr>
    <h3>node respone</h3>
    <div>
      ajax code:
      <pre>
        ajax('http://'+host+':3001/', 'node');
      </pre>
    </div>
    <pre id="node-xml"></pre>
    <pre id="node-xdomain"></pre>

    <hr>

    <h3>django respone</h3>
    <div>
      ajax code:
      <pre>
        ajax('http://'+host+':3002/', 'django');
      </pre>
    </div>
    <pre id="django-xml"></pre>
    <pre id="django-xdomain"></pre>

    <script>
      var host = location.hostname;
      var sendTimeout = 0;
      var ajax = function(url, type) {
        if(window.XDomainRequest) {
          var xdomainAjax = new XDomainRequest();
          xdomainAjax.open('POST', url);
          xdomainAjax.timeout = 1200;
          xdomainAjax.onload = function(){
            console.log(type + ' with XDomainRequest: ', this.responseText);
            document.getElementById(type + '-xdomain').innerHTML = type + ' with XDomainRequest respone: <span class="red">' + this.responseText + '</span>';
          }
          xdomainAjax.onerror = function() {
            console.log('node error', this);
          }
          setTimeout(function() {
            xdomainAjax.send('param1=value1&param2=value2');
          }, sendTimeout)
        }

        if(window.XMLHttpRequest) {
          var xmlAjax = new XMLHttpRequest();
          xmlAjax.open('POST', url);
          xmlAjax.timeout = 1200;
          xmlAjax.onreadystatechange = function(){
            if (this.readyState==4 && this.status==200) {
              console.log(type + ' with XMLHttpRequest: ', this.responseText);
              document.getElementById(type + '-xml').innerHTML = type + ' with XMLHttpRequest respone: <span class="red">' + this.responseText + '</span>';
              
            }
          }
          setTimeout(function() {
            xmlAjax.send('param1=value1&param2=value2');
          }, sendTimeout)
        }
      }
    </script>
    <script>
      ajax('http://'+host+':3001/', 'node');
    </script>

    <script>
      ajax('http://'+host+':3002/', 'django');
    </script>

  </body>
</html>
```

就酱，用这个静态文件访问就行。
运行方式： 保存为 `index.html` 然后， `sudo npm i -g anywhere` ，然后， cd 到当前目录， `anywhere 3003` 即可。就看到结果了。

## 结论

Django 在处理 XDomainRequest 的 POST 请求时候确实没有正确解析。  但是 nodejs 原生的 http 服务例子能解析。 python 原生的写法没进行测试。

然后发现现在也有框架无法处理 XDomainRequest 的 POST 数据，例如在抓包过程中使用的 `livepool` 工具。

## 测试环境  

后端环境：

硬件： macbook pro retina 13
nodejs ： v0.12.0
django ： 1.8.3

运行环境：
PD 虚拟机 + WIN7 + IE 9

## 源代码
[https://github.com/shenqihui/lab/tree/gh-pages/test_django_post_with_xdomainrequest](https://github.com/shenqihui/lab/tree/gh-pages/test_django_post_with_xdomainrequest)

## END
