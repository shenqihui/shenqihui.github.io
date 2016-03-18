#!/bin/bash
nodeppt generate index.md ../../ppt/experience
mv ../../ppt/experience/index.htm ../../ppt/experience/index.html
# 复制静态文件
cp -rn ../_static/* ../../ppt/experience/
