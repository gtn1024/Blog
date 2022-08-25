---
title: 使用 GitHub 纯免费方案搭建 Hexo 博客
date: 2022-08-24 22:21:18
categories:
- 知识科普
tags:
- 博客
---

现在我们有什么文章往往都会发布到互联网上，一些同学是发布到掘金、CSDN、知乎等平台，还有一些是自己搭建个人的博客平台。本文主要介绍后者，通过 Hexo 搭建个人博客。

Hexo 是基于 Node.js 的纯静态博客系统，即构建以后为纯 HTML 文件。故我们博客可以使用一些托管平台来部署，如 GitHub Pages、Vercel、Netlify、Cloudflare Pages 等平台。

本文主要是用如下方案进行部署：本地搭建 Hexo 博客，推送到 GitHub 上，使用 GitHub Actions 自动构建并部署至 GitHub Pages。

<!-- more -->

## 安装 Node.js

在搭建 Hexo 博客之前，需要先安装 [Node.js](https://nodejs.org/zh-cn/)，打开官网后下载长期维护版即可，目前最新的长期维护版为 `16.17.0`。

{% asset_img 16613481023243.jpg %}

安装完 Node.js 后，执行 `node -v` 和 `npm -v`，如果能够正常显示版本号则安装完成。

如果安装 Node.js 一切正常，能够正常使用 `node` 和 `npm` 命令，我们则可以进行下一步——搭建 Hexo 博客。

## 创建 Hexo

运行 `npm install hexo-cli -g` 命令，在系统全局安装 `hexo-cli` 工具。该工具可以方便地帮助我们创建 Hexo 项目、创建 Hexo 页面、创建 Hexo 文章。当然，如果你熟悉 `yarn`、`pnpm` 等 Node.js 包工具，也可以使用这些工具来安装 `hexo-cli`。

执行 `hexo -v`，正常显示各组件版本信息，则安装成功。

{% asset_img 16613484869822.jpg %}

运行 `hexo init my-blog` 命令，`hexo-cli` 工具就会在 `my-blog` 目录下创建一个 Hexo 博客。如果他没有安装依赖，请运行 `npm install` 安装依赖（注意进入 `my-blog` 目录）。我个人使用 `pnpm` 进行包管理。

{% asset_img 16613488370437.jpg %}

{% asset_img 16613488540908.jpg %}

依赖安装成功后可以使用 `hexo s` 在本地启动服务器便于预览，一般情况下会在本机的 4000 端口开启一个 HTTP 服务。

{% asset_img 16613490348269.jpg %}

{% asset_img 16613490791853.jpg %}

## 玩转 Hexo

正如在上方预览里文章所说，运行 `hexo new` 命令可以新建一篇博客，后面需要接上博客的文件名，通常情况下我们使用英文。运行后他会在 `source/_posts` 目录下创建一个 Markdown 文件，该文件即为新的文章。

{% asset_img 16613491830259.jpg %}

我们对文章进行修改，重新启动服务器进行查看。

{% asset_img 16613492885900.jpg %}

{% asset_img 16613493607001.jpg %}

到这里我们就完成了最基本的博客搭建、文章编写。当然，我们还可以对其进行个性化，比如更换主题什么的。在官网的 `Themes` 栏目下也有许许多多优质的主题推荐。

{% asset_img 16613494499545.jpg %}

## 在 GitHub 上创建 git 仓库并推送

我们可以在 GitHub 创建 `用户名.github.io` 的仓库，该仓库是一个特殊的仓库，开启 GitHub Pages 后可以直接通过该域名来访问 Pages，而其他仓库名则为 `用户名.github.io/仓库名` 访问。例如，我的 GitHub 用户名是 `gtn1024`，那么我创建的仓库则为 `gtn1024.github.io`。

## 编写 GitHub Actions 脚本实现自动构建

在仓库根目录创建 `.github/workflows/deploy.yml` 文件，写入如下 GitHub Actions 脚本，即可自动使用 GitHub Actions 对其进行构建并且部署至 GitHub Pages 上。

```yaml
name: 部署

on:
  push:
    branches:
      - main

jobs:
  deploy-gh-pages:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
        with:
          fetch-depth: 0
      - name: 安装 pnpm
        uses: pnpm/action-setup@v2
        with:
          version: 7
          run_install: true
      - name: 设置 Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 16
          cache: pnpm
      - name: 安装依赖
        run: pnpm install --frozen-lockfile
      - name: 构建
        env:
          NODE_OPTIONS: --max_old_space_size=4096
        run: pnpm run build
      - name: 部署文档
        uses: JamesIves/github-pages-deploy-action@v4
        with:
          # 这是文档部署到的分支名称
          branch: gh-pages
          folder: public
```

push 到 GitHub 后，GitHub Actions 将会自动启动构建，如图为构建成功的截图

{% asset_img 16613503836038.jpg %}

最后，我们将 GitHub Pages 分支设置为 `gh-pages` 即可。

{% asset_img 16613504369414.jpg %}

## 访问

访问 `用户名.github.io` 即可看到刚才搭建的 Hexo 博客。

{% asset_img 16613505129028.jpg %}

## 还有一些事

至此，我们 Hexo 博客的雏形已经搭建完成。事实上，我们还有很多事情要做：

- 配置博客描述
- 换个好看的主题
- ...

将在后续的文章讲解。
