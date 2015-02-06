#博客系统
---

### blog
[地址](http://shenqihui.github.io/). [仓库](https://github.com/shenqihui/shenqihui.github.io/)


## 配置

需要配置的地方有两个，  

```
_config.yml    
themes/alberta/_config.yml    
```

## 初始化
```bash
npm install
```


## 如何修改主题

主题文件位于 theme 下面，使用的是 hexo-theme-alberta ，目前已经把此 主题 整入仓库，后期将不对主题进行开发，直接位于此仓库进行开发。


## 发布到 Github 
```bash
hexo clean
hexo generate
hexo deploy
```
然后得到一个 .deploy 的文件夹，推送到想要的仓库即可。


## 说明

此仓库进行了个人定制，因此，可能不能通用。