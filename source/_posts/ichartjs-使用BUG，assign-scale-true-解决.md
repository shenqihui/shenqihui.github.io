title: "ichartjs 使用BUG，assign_scale:true 解决"
tags: []
date: 2013-07-22 11:21:00
---

今天纯属灌水，好久没灌水的。

最近使用了flotr2 和 ichartjs进行canvas图标的开发，都不能满足需求。
<!--more-->
没办法，先将就用用吧。然后，既然其他大神推荐使用ichartjs，为了统一，我也只能使用ichartjs了，

使用过程中，发现一个bug。

具体为左右y轴，不能自定义，start_scale,end_scale,scale_space,scale_share限制都不给力。。。。。。。[http://www.ichartjs.com/samples/index.html?page=combination2d_02.html&amp;pageno=11](http://www.ichartjs.com/samples/index.html?page=combination2d_02.html&amp;pageno=11)&nbsp;就仿照这例子弄的而已。

然后，bug提交给大神了，大神没多说，说之前就有人遇到这个问题，后马上给我解决方案：在scale的参数里面添加：assign_scale:true。更新到[latest.min.js](http://www.ichartjs.com/ichart.latest.min.js)文件，就能解决。此参数还没发布正式API，只是在源文件改了而已。

可怜我自己尝试了半天。

我问大神，为什么不发布这新参数，他说，等问题积累到一定程度再发。我想想也对，这东西，一发就是更新版本，又要用户换，又要写更新日志，麻烦。

后，没有然后了。灌水完毕。加班中，一会走人。