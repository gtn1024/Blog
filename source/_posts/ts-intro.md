---
title: TypeScript 学习笔记——初识TS
date: 2022-08-25 21:27:43
categories:
- [编程语言, TypeScript]
tags:
- TypeScript
- 多线程
---
本系列主要是在学习方应杭老师的《TypeScript全解》所做笔记。该系列文章可能会结合 Java 上的知识对 TypeScript 进行理解。

<!-- more -->

## TypeScript 是什么

TypeScript 是添加了类型系统的 JavaScript，是 JavaScript 的超集。所有的 JavaScript 代码都是合法的 TypeScript 代码。

## 类型擦除是什么

普通的 JavaScript 代码可以在 Chrome、Node 等环境中直接运行，而 TypeScript 无法在无任何其他工具的帮助下直接运行。

{% asset_img 20220825201047.png %}

类型擦除指将 TypeScript 代码中与类型相关的东西移除，变为纯真的 JavaScript 代码。通常也可以称它为编译的过程。

编译 TypeScript 主要有如下工具：

- esbuild
- swc
- tsc
- babel

其中，esbuild 和 swc 在编译时不会检查 TS 语法，仅仅将类型擦除，故其在使用时十分快速。而 tsc 和 babel 工具会检查 TS 语法，如果 TS 语法错误则无法进行编译，故编译过程较慢。

### 使用 `esbuild` 编译 TS 代码

首先使用 npm 安装 `esbuild` 工具：`npm i -g esbuild`

用于测试的代码如下：

```ts
// 1.ts
const a: number = 1 + 2;
console.log(a);
```

使用 `esbuild 1.ts` 命令编译结果如下：

{% asset_img 20220825202237.png %}

可以看到，`esbuild` 将 `number` 移除了。

如果需要将编译后的结果输出到文件，可以使用重定向符将标准输出转移到文件。

`esbuild 1.ts > 1.js`

{% asset_img 20220825202541.png %}

### 使用 `swc` 编译 TS 代码

使用 `npm i -g @swc/cli @swc/core` 安装 swc

{% asset_img 20220825202730.png %}

### 使用 `tsc` 编译 TS 代码

`tsc` 是 TypeScript 官方提供的编译工具，安装 TypeScript 后将自带该工具。

`npm i -g typescript`

{% asset_img 20220825203026.png %}

### 不检查 TS 语法是什么意思

不检查 TS 语法是指工具在编译 TS 的过程中不对其正确性进行检查，仅仅将类型删去。

例如，我在 `bad.ts` 的文件中将 `number` 写成 `numbe`，`esbuild` 可以正常输出编译结果，而 `tsc` 会报错。

{% asset_img 20220825203337.png %}

## 运行 TypeScript 代码

### TypeScript Playground

TypeScript Playground 是 TypeScript 官方提供的演练场，有大量的配置可以修改。在学习 TypeScript 语法时可以使用该演练场进行代码编写。

{% asset_img 20220825204400.png %}

{% asset_img 20220825204341.png %}

### 使用 `ts-node` 执行 TypeScript 代码

在系统中全局安装 `ts-node`（需要有 TypeScript 环境）

`npm i -g ts-node`

安装后就可以使用 `ts-node` 命令直接运行 TS 代码

{% asset_img 20220825205116.png %}

### 使用 `esno` 执行 TypeScript 代码

同样使用 npm 安装工具：`npm i -g esno`

随后使用 `esno` 运行，效果与 `ts-node` 类似

{% asset_img 20220825205515.png %}
