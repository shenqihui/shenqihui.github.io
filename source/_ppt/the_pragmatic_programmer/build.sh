#!/bin/bash
nodeppt generate index.md ../../ppt/the_pragmatic_programmer
mv ../../ppt/the_pragmatic_programmer/index.htm ../../ppt/the_pragmatic_programmer/index.html
# 复制静态文件
cp -rn ../_static/* ../../ppt/the_pragmatic_programmer/
