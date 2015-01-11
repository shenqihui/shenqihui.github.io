title: flotr2 中英文文档 对照
tags: []
date: 2013-07-17 03:39:00
---

<div class="clear">

近期工作用到 flotr2 。学了一下，然后使用吧。鉴于现在还没完全的中文文档信息，做点贡献，翻译[官方的文档](http://www.humblesoftware.com/flotr2/documentation "flotr2 documentation")信息。鉴于时间关系，将陆续进行翻译。不过感觉官方文档信息很简单。

</div>
<!--more-->
<div class="clear">
> ## Introduction
> 
> Flotr2 is a library for drawing HTML5 charts and graphs. It is a branch of [flotr](http://code.google.com/p/flotr/ "flotr") which removes the Prototype dependency and includes many improvements.
> 
> ### Features:
> 
> *   mobile support
> *   framework independent
> *   extensible plugin framework
> *   custom chart types
> *   FF, Chrome, IE6+, Android, iOS
> 
> 
> *   lines
> *   bars
> *   candles
> *   pies
> *   bubbles
</div>
<div class="clear">

## 这里翻译

</div>
<div class="clear">
> ## <a id="usage"></a>Usage
> 
> To use Flotr2, include the `flotr2.min.js` script in your page and create a visible `&lt;div&gt;` with positive width and height. A graph is drawn with the `Flotr.draw(container, data, options)` method.
> 
> ### <a id="usage-example"></a>Usage Example ([stand alone](http://www.cnblogs.com/flotr2/example))
> 
> <div class="editor usage">&nbsp;</div>
> 
> 
> ### API: `Flotr.draw(container, data, options)`
> 
> *   `container` a visible DOM element with positive width and height.
> *   `data` an Array of series.
> *   `options` a configuration object containing flotr configuration options, defining axes, grids, legends, etc.
> 
> 
> ### Data
> 
> Each series is either an array of points `[[x0, y0], [x1, y1] ...]` or an object with series options and a data member.
> 
> ### Internet Explorer
> 
> Flotr2 is fully supported in IE 9+ and [explorer canvas](http://code.google.com/p/explorercanvas/ "explorer canvas") or [flashcanvas](http://flashcanvas.net/ "flash canvas") may be conditionally included to support older versions, as seen in the [example](#usage-example "usage example") above.
</div>
<div class="clear">

## 这里翻译

</div>
<div class="clear">
> ## <a id="configuration"></a>Configuration
> 
> The following are the default configuration options for Flotr. Additional options are added for individual graph types and plugins. In general, those can be found at the top of each plugin or graph file.
> 
> ### Flotr2 Defaults
> 
> <div class="editor api">&nbsp;</div>
</div>
<div class="clear">

## 这里翻译

</div>
<div class="clear">
> ## <a id="development"></a>Development
> 
> This project uses [ smoosh](https://github.com/fat/smoosh "smoosh") to build and [jasmine](http://pivotal.github.com/jasmine/ "Jasmine BDD") with [js-imagediff](https://github.com/HumbleSoftware/js-imagediff "js-imagediff canvas testing") to test. Tests may be executed by [ jasmine-headless-webkit](http://johnbintz.github.com/jasmine-headless-webkit/ "jasmine headless webkit") with `cd spec; jasmine-headless-webkit -j jasmine.yml -c` or by a browser by navigating to `spec/SpecRunner.html`.
> 
> ### Directories
> 
> *   `js/` main source files
> *   `js/plugins/` flotr plugins
> *   `js/types/` chart types
> *   `spec/` Jasmine tests
> *   `examples/` stable and development example pages
> *   `make/` build configuration files
> *   `lib/` included libraries
> *   `build/` temporary directory used during build
> 
> 
> ### Extending
> 
> Flotr may be extended by adding new graph types and plugins. Graph types define how a particular chart is rendered. Examples include line, bar, pie. Existing graph types are found in [` js/types/`](https://github.com/HumbleSoftware/Flotr2/tree/master/js/types "flotr2 graph types").
> 
> Plugins extend the core of flotr with new functionality. They can add interactions, new decorations, etc. Examples include titles, labels and selection. Plugins are found in [` js/plugins/`](https://github.com/HumbleSoftware/Flotr2/tree/master/js/plugins "flotr2 plugins").
</div>
<div class="clear">

## 这里翻译

</div>
<div class="clear">
> ## <a id="resources"></a>Resources
> 
>  ![Google Groups](http://groups.google.com/intl/en/images/logos/groups_logo_sm.gif) 
> 
>   [Flotr2 is on Google groups](http://groups.google.com/group/flotr2)
> 
> 
> ### Issues
> 
>   Please submit issues and pull requests on github at [http://github.com/HumbleSoftware/Flotr2/issues](http://github.com/HumbleSoftware/Flotr2/issues "Flotr2 issues").
> 
> 
> ### Source
> 
>   The source is available on github at [http://github.com/HumbleSoftware/Flotr2](http://github.com/HumbleSoftware/Flotr2 "Flotr2 source on github").

</div>
<div class="clear">

## 这里翻译

</div>
<script type="text/javascript" src="http://www.humblesoftware.com/static/js/hsd.js?d3fa1"></script>
<script type="text/javascript" src="http://www.humblesoftware.com/static/js/hsd-flotr2.js?d3fa1"></script>
<script type="text/javascript" src="http://www.humblesoftware.com/static/js/hsd-flotr2-documentation.js?d3fa1"></script>
<style><!--
.features, .types{
float:left;
display:block;
}
.clean{width:100%;height:100%;clear:both;}
</stlye>
--></style>