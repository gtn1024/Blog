---
title: Go 语言简介及安装
date: 2023-01-15 17:27:50
categories:
- [编程语言, Go]
tags:
- Go
---
本文主要介绍 Go 语言，以及 Go 语言的安装及环境搭建。

<!-- more -->

## 什么是 Go 语言

Go 语言是由 Google 开发的一门跨平台的编程语言，最早在2009年发布。

Go 语言具有如下特点：

- 高性能、高并发。在编程语言的层面上实现了高并发，十分容易就可以写出高并发的程序。
- 语法简单，学习曲线平缓。Go 语言的语法类似 C，同时语法风格较为简洁。
- 丰富的标准库。Go 语言提供了大量高质量的标准库。
- 完善的工具链。在编译、格式化、质量检查、包管理、测试等方面拥有完善的工具链。
- 静态链接。在代码编译之后以单个可执行文件作为构件，可将该可执行文件直接部署。
- 快速编译。编译速度较快，同时支持增量编译。
- 跨平台。可以在几乎所有的平台、架构下运行。同时自带交叉编译。
- 垃圾回收。无需考虑内存管理。

## Go 语言环境配置

### Go 语言安装及配置

进入 [Go 语言官网](https://go.dev/)，下载安装最新版即可。

安装完成后，在国内因为某些原因，常常需要配置 proxy 使用。可使用七牛的 [goproxy](https://goproxy.cn/) 服务对于 Go 进行加速。

```shell
go env -w GO111MODULE=on  # 开启 Go 1.11 module功能
go env -w GOPROXY=https://goproxy.cn,direct # 使用 goproxy 进行加速
```

### 使用 VSCode 进行 Go 开发

安装 [Visual Studio Code](https://code.visualstudio.com)，并安装 [Go 语言插件](https://marketplace.visualstudio.com/items?itemName=golang.Go)，即可进行 Go 语言开发。

## 第一行 Go 代码

使用  `go mod init github.com/gtn1024/helloworld` 命令，即可创建一个新的项目，随后创建 `main.go`，输入如下代码：

```go
package main

import "fmt"

func main() {
 fmt.Println("Hello, world!")
}
```

在项目目录中执行 `go run .` 即可运行该程序。

{% asset_img 20230115165947.png %}

在如上代码中，将包名设置为 `main`，代表该文件是一个程序的入口文件。Go 语言的程序由 `main` 包中的 `main()` 函数启动。`import "fmt"` 则代表需要导入 `fmt` 包，该包主要用于程序的字符串和输入输出。`fmt.Println("Hello, world!")` 则代表输出 `Hello, world!` 语句。

## 编译 Go 程序

### 编译为当前平台可执行程序

运行 `go build .` 即可将当前项目编译成当前平台的可执行文件，该文件可以独立执行而无需任何的依赖。

{% asset_img 20230115170829.png %}

### 交叉编译其他平台程序

Go 编译程序可以通过环境变量的方式来切换目标平台。本文使用的是 `Git Bash`，所以可以直接在命令前面添加环境变量。

{% asset_img 20230115172126.png %}

Go 语言可交叉编译的平台可以由 `go tool dist list` 命令查看：

{% asset_img 20230115171820.png %}
