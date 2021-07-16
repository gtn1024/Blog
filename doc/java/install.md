---
title: Java 简介及安装
date: 2021-07-08 20:43:36
category: 实用教程
tags:
  - Java
---

# Java 简介及安装

## 什么是 Java

> Java 是一种全世界广泛使用的编程语言，具有跨平台、面向对象、泛型等特性，广泛应用于企业级 Web 应用开发及移动应用开发。
>
> 来源：[维基百科](https://zh.wikipedia.org/wiki/Java)

行吧，我承认以上内容大家是不会看的，下面我直接说下重点。

- Java 是全球排名第一的编程语言。见[TIOBE](https://www.tiobe.com/tiobe-index/)
- Java 市场需求量大。见各大招聘网站。
- Java 跨平台，一次编写，到处运行。
- Java 具有内存回收机制。
- Java...

## Java 的历史

Java 的诞生可以说是对于 C/C++语言的反抗。其没有 C 语言的指针，不用考虑内存管理，完全支持跨平台。

最初该编程语言的命名为`C++--`，即在 C++的基础上做一些改进。后来创始人发现设计理念差别太大，故将其命名为`Oak`。待编程语言发布的时候，发现 Oak 商标已被别人使用，最终命名 Java。

Java 逐步出名之后，一些商业巨头（如 Oracle、Microsoft）纷纷与 Java 合作。其中 Bill Gates 称 Java 是迄今为止设计得最好的语言。

2006 年 Hadoop 框架的出现，使得 Java 进军大数据领域。

2008 年 Android 系统的诞生，更是使得 Java 进入了全新的高度，Android 中的应用由 Java 开发。

## Java 的版本

Java 主要有 3 个版本：

- Java SE（Standard Edition）
- Java EE（Enterprise Edition）（现在为 Jakarta EE）
- Java ME（Micro Edition）

Java SE 为标准版，提供标准 JVM 和标准库。

Java EE 为企业版，在 Java SE 的基础上加入了大量的 API 和类库，使其方便 Web 应用、数据库等服务的开发。其使用的虚拟机与 Java SE 完全相同。Java EE 在 2018 年已被 Oracle 公司转交给 Eclipse 基金会管理，并改名为 Jakarta EE。

Java ME 则为一种“瘦身版”，是一个针对嵌入式设备的版本。

## 几个名词

在刚接触 Java 的时候，你一定听到下面几个名字：

- JDK（Java Development Kit）
- JRE（Java Runtime Environment）
- JVM（Java Virtual Machine）

下图为这三者的关系：

<pre class="ascii-pic">
<code>
┌───────────────────────────┐
│ JDK                       │
│     ┌───────────────────┐ │
│     │ JRE               │ │
│     │     ┌───────────┐ │ │
│     │     │ JVM       │ │ │
│     │     │           │ │ │
│     │     └───────────┘ │ │
│     └───────────────────┘ │
└───────────────────────────┘
</code>
</pre>

## Java 安装

在[Oracle 官网](https://www.oracle.com/java/technologies/javase-downloads.html)下载最新的 Java SE 16 后安装即可。

<pre class="ascii-pic">
<code>
┌───────────────────────────────────────────────────┐
│                 Java SE Downloads                 │
│          Java Platform, Standard Edition          │
│                                                   │
│Java SE 16                                         │
│Java SE 16.0.1 is the latest...                    │
│                                                   │
│· Documentation          Oracle JDK                │
│· Installation...          ■■■■■■■■■■■■■■■■        │
│· Release Notes            ■ <a href="https://www.oracle.com/java/technologies/javase-jdk16-downloads.html" target="_blank">JDK Download</a> ■        │
│· Oracle License           ■■■■■■■■■■■■■■■■        │
│    · Binary License         Documentation Download│
│    · Documentation License                        │
└───────────────────────────────────────────────────┘
</code>
</pre>

::: tip
注意：M1 芯片的 mac 用户，目前请使用[zulu jdk](https://www.azul.com/downloads/?version=java-16-sts&os=macos&architecture=arm-64-bit&package=jdk)
:::

## 环境变量配置

在 Windows 系统中，设置`JAVA_HOME`环境变量，指向 Java 安装目录，然后在`PATH`环境变量中追加`%JAVA_HOME%\bin`即可。

在 macOS 系统中，在用户配置文件（如`~/.bash_profile`或`~/.zprofile`）中加入以下内容：

```bash
export JAVA_HOME=`/usr/libexec/java_home -v 16`
export PATH=$JAVA_HOME/bin:$PATH
```

最后打开终端，输入`java -version`，如正确显示 Java 16 版本信息，则证明配置成功。
