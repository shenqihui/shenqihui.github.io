#!/bin/bash

# rm -rf source/ppt
cd source/_ppt/experience/ && bash ./build.sh
cd ../the_pragmatic_programmer/ && bash ./build.sh

hexo clean
hexo generate
hexo deploy
