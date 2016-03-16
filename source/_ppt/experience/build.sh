#!/bin/bash
nodeppt generate index.md ../../ppt/experience
# 复制静态文件
cp -rn ../_static/* ../../ppt/experience/