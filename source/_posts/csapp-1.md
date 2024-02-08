---
title: 「深入理解计算机系统」学习笔记（第一章）
date: 2024-02-08 11:42:24
tags:
- 深入理解计算机系统
---

本文主要是《深入理解计算机系统》第一章（计算机系统漫游）的学习笔记。主要依据 B 站 UP 主九曲阑干对 CSAPP 的 [中文讲解](https://www.bilibili.com/video/BV1cD4y1D7uR)。

CSDIY 上对于本课程的介绍：<https://csdiy.wiki/%E4%BD%93%E7%B3%BB%E7%BB%93%E6%9E%84/CSAPP>

<!-- more -->

## 程序的生命周期

本章主要是依据一个普通 Hello World 程序的生命周期，对计算机系统主要概念做一个概述。

一个程序大体上分为如下四个步骤：

1. 创建 Create
2. 编译 Compile
3. 运行 Run
4. 退出 Exit

首先，创建一个 C 语言程序，命名为 `hello.c`：

```c
#include <stdio.h>
int main()
{
  printf("hello, world!\n");
  return 0;
}
```

使用 GCC 对程序进行编译：

```bash
$ gcc -o hello.exe hello.c
```

通过本命令，编写的 `hello.c` 通过编译系统进行编译后，生成名为 `hello.exe` 的可执行程序。

{% asset_img compile-abs.drawio.png %}

虽然我们只通过了一条命令就完成了程序的编译，但事实上编译过程是很复杂的。

一个编译过程主要分为四部分：

1. 预处理 Pre-processing (cpp)：经过预处理器将 `hello.c` 转变为 `hello.i` 文件。
2. 编译 Compile (cc1)：通过词法分析、语法分析、语义分析、中间代码生成、优化等一系列操作，将 `hello.i` 转变为 `hello.s` 文件。
3. 汇编 Assemble (as)：汇编器根据指令集翻译为机器指令，并且按照固定规则进行打包。将 `hello.s` 转变为可重定位目标文件 `hello.o`。
4. 链接 Link (ld)：链接器将 `hello.o` 与其他库文件链接，生成可执行文件 `hello.exe`。

{% asset_img compile-process.drawio.png %}

## 理解编译系统过程的意义

为什么要理解编译系统是如何工作的？

1. 优化程序性能
2. 理解链接时出现的错误
3. 避免安全漏洞

## 通过 Shell 运行程序

```bash
$ ./hello.exe
hello, world!
$
```

## 计算机系统的硬件组成

{% asset_img hardware.png %}

## 高速缓存

在通常情况下，大容量的存储设备的存取速度要比小容量的慢，运行速度更快的设备的价格相对于低速设备要更贵。

例如，在一个系统上，磁盘容量一般为 TB 级，内存容量一般为 GB 级，而寄存器文件的容量一般为 B 级别。

对于处理器而言，从磁盘上读取一个字所花费的时间开销比从内存中读取的开销大 1000 万倍；从寄存器文件读取数据比从内存读取数据快 100 倍。随着半导体技术的发展，处理器与内存之间的差距还在持续增大。

针对处理器和内存的差异，系统设计人员在寄存器和内存之间引入了了高速缓存（cache）。比较强的处理器一般有三级缓存，分别是 L1、L2 和 L3，从前往后容量逐渐变大，速度逐渐变慢。L1 与寄存器之间的速度差异不大，容量为 KB 级别；L2 与 L3 容量更大一些，分别为 MB 级别。

{% asset_img cache.png %}

## 操作系统

操作系统是应用程序和硬件之间的中间层，所有应用程序对硬件的操作都需要经过操作系统进行完成。

{% asset_img os.png %}

操作系统引入几个概念：

1. 文件 Files：对于 I/O 设备的抽象
2. 虚拟内存 Virtual memory：对于内存和磁盘 I/O 的抽象
3. 进程 Processes：对处理器、内存和 I/O 设备的抽象

{% asset_img os-abs.png %}

## 虚拟机

虚拟机是对于整个计算机系统的抽象，包括操作系统、处理器、内存、I/O 设备。

{% asset_img vm.png %}

