title: "关于我"
show: hide
hidden: true
visible: hide
date: 2022-05-17 17:58:21
comments: false
---

# 沈启辉 Solidity 开发

- 微信: xxxxx01357 / 电话: 134...
- 男 / 1990 / 本科 / 广东工业大学 / 计算机学院 / 软件工程 (2009-2013)
- Github: [github.com/shenqihui](https://github.com/shenqihui) / Gist: [gist.github.com/shenqihui](https://gist.github.com/shenqihui)
- 职位: 前端开发 / 架构 ，工作年限: 9+ 年；Solidity 合约开发，工作年限：1+ 年。

---

## 技能清单
以下为我熟练使用的技能 / 工具

- 前端框架/库/工具: React / dva / Taro / axios + jwt / Webpack / antd
- web3: solidity / evm / web3.js / ether / web2.storage / metamask
- 开发工具: Mac / Ubuntu / VS Code / ST3 / vim / git / Nginx
- 其他: linux / rsync / tmux / Less / eslint / zsh / iTerm / docker
- ~~曾熟练掌握但废弃: Python + Django / Fabric / Angular (目前公司转型 React) / XSS 等网站安全知识 / ES,Redis,MySQL,Mongo / Karma~~
- 不懂 vue

---

## 对应 web3

熟悉 evm 链。其他非 evm 类型链只是了解过，没利益驱动，不深入。
使用 solidity 一年+，熟悉 ERC20 / uniswap v2 合约，熟悉 gas 优化。
了解部分 farm 机制 / 预言机 / web3 键盘侠。
不喜欢 ERC721 / ERC1155 （主要是不喜欢乱发 nft，都是土狗的思想）
理解较浅的部分： opcodes （阅读参考未验证的合约使用）
目前还在学习的： proxy contract / thegraph

### oklink 闪电贷套利
手写套利合约，监控链上所有的交易来检测，nodejs 端代码还没公开
大概思路和代码写在了 [gist](https://gist.github.com/shenqihui/d5a2ae5d449133e83027f47d6ad8682f)

### 对赌平台（无上线）
一个人开发
整套对赌平台的合约代码，实现 follow 功能
前端 web 方面直接在某套已公开源码的项目上进行魔改。
由于不想充值类似 thegraph 等平台，还得避免 infura rpc 交互频繁，强行写个合约整合数据查询。

### 其他撸空投
油费太贵，只撸过少部分非贵族链上而且是 evm 类型链的空投。（使用手工 + 代码）
稳定币搬砖套利（前期人工实现，后期代码实现，后由于火币禁止国内用户停止了）

---

## 工作经历

### 🏢 广东青藤教育 (2016 年 05 月 ~ 至今, 前端开发 -> 技术经理)
**引领公司从 ng 走向 react**，负责 **前端的架构及技术调研** 、 **前端人员招聘到培养管理** 、**需求沟通及可行性探讨**、 负责公司项目的运维部署任务，部门开发任务分发安排，同时维护部门 IT 基础服务。
公司大部分项目为前后端分离方案，开发阶段使用 nignx 处理，平台涉及 PC 端 / M 端 / 微信小程序 / 钉钉小程序 。

#### 西北某几个城市智慧教育系统  (2018 年 04 月 ~ 至今，长期开发和维护中)
**负责前端的架构**，搭建前端的基础组件以及业务逻辑基本框架，分发前端任务，代码 review 及质量控制 。
在这个项目基础上，拓展出不同地区的定制化版本。
目前项目持续交付及迭代中，使用的技术 React + React Router V4 + antd + dva v2 + parcel(pc 站) + graphql + restful。里面实现了 graphql 语法自动生成机制(graphql 的错误用法)。


#### 宫主帮管理系统 + 智慧宫定制版本 (2016 年 05 月 ~ 至今，长期开发中)
负责 PC 端管理系统 / 微信小程序的架构以及开发，参与 PC + 微信小程序 + M 站的开发，项目一直处于功能开发及维护中。

**其中，宫主帮技术发展从 ng1 转换到 react ，教育系统在这个基础上第三版再次优化抽象，慧票易为第四版本技术方案。**

#### 公司其他事情
青藤网官网（不维护） / 最美南粤少年活动手机站点（亿级PV，已下线） / 慧票易商票交易平台 PC 端 / 小程序 / 管理后台（已独立公司开发）

---

### 🏢 北京知道创宇 (2014 年 10 月 ~ 2016 年 04 月， 前端开发，北京)
参与公司多个项目的开发，涉及的技术有 ng1 / react / karma / Python + Django / ES,Redis,mongo,mysql / Nginx / XSS之类网站安全 ，改进部分项目的开发、协助、发布模式。

#### ZoomEye 钟馗之眼
曾负责整个 [ZoomEye](https://www.zoomeye.org/) 应用层(非搜索的存储以及查询语法方面)工作的开发，包括其中的运维部署、数据库、后端接口、前端渲染、可视化展现等工作。

#### XSS 攻击平台
水坑攻击平台，经历并主导项目中的几次前后端的迭代重构，整个项目从 Demo 阶段到第一版本、第二版本的迭代。
在项目中负责前端攻击框架的编写、后端架构的优化、周边工具的搭建完善、测试平台的搭建等工作，空余时间进行前端漏洞的挖掘。

#### 公司其他项目
- ZoomEye Pro (ZoomEye 的企业版本，用于描绘内网拓扑，提前发现风险)
- 维护大屏幕展示类项目
- 维护漏洞探测类项目
- 维护 Web 安全类型项目
- 其他内部使用的部署工具类项目

---

### 🏢 广州盈尚信息 前端开发 ( 2014 年 03 月 ~ 2014 年 10 月)
负责公司各种基础 IT 相关工作，负责网站前端的开发，服务器搭建、运维。

### 🏢 威创股份 前端开发 (2013 年 03 月 ~ 2014 年 03 月)
参与大屏幕展示项目及智慧城市系统的开发。

