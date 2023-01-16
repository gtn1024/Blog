---
title: Go 语言入门 —— 基础语法
date: 2023-01-16 23:29:58
categories:
- [编程语言, Go]
tags:
- Go
---
本文主要对于 Go 语言的类型系统、变量常量及流程控制进行介绍。

<!-- more -->

## 类型系统

### 基本数据类型

在 Go 语言中，有如下的基本数据类型：

- `bool`：表示布尔类型，值为 `true` 或 `false`。
- `int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`int64`、`uint64`：整数类型，最后的数字代表有多少位，以 `u` 开头的为无符号整型。
- `int`、`uint`、`uintptr`：整数类型，类型的大小由编译器决定。保证 `uintptr` 类型能够存下一个内存地址。
- `float32`、`float64`：浮点型。
- `complex64`、`complex128`：复数类型，对应的实部和虚部数据类型相同。分别为 `float32` 和 `float64`。
- `string`：字符串类型。

另外，Go 语言中 `byte` 和 `rune` 类型分别为 `uint8` 和 `int32` 的类型别名。

### 类型别名

在 Go 语言中，可以通过 `type 类型名 = 类型` 来定义一个类型别名，这两个类型是等价的。

```go
type Id = uint64

var id1 Id = 1
var id2 uint64 = 1
fmt.Printf("%#v %#v", id1, id2) // 0x1 0x1
```

## 变量与常量

在 Go 语言中，定义一个变量有 2 种方式。

1. 使用 `var` 关键字定义变量。
2. 使用 `:=` 运算符定义变量。

```go
var a int = 10 // 使用 var 定义变量
var b = 20     // 使用 var 定义变量，自动推导类型
c := 30        // 使用 := 定义变量，自动推导类型

// a = 10, b = 20, c = 30/
fmt.Printf("a = %#v, b = %#v, c = %#v", a, b, c)
```

常量的定义更简单，直接使用 `const` 关键字即可定义常量。

```go
const d int = 40 // 使用 const 定义常量
const e = 50     // 使用 const 定义常量，自动推导类型

fmt.Printf("d = %#v, e = %#v", d, e) // d = 40, e = 50
```

## 流程控制

### 条件语句

在 Go 语言中，主要有如下几种条件语句：

- `if-else` 条件分支结构
- `switch-case` 分支结构

`if-else` 结构与其他编程语言相类似，但是 Go 语言的条件并不需要添加括号。

```go
a := 10
if a > 30 {
 fmt.Println("大于30")
} else if a > 20 {
 fmt.Println("大于20")
} else if a > 10 {
 fmt.Println("大于10")
} else {
 fmt.Println("小于等于10")
}
```

`switch-case` 语句也类似，但 `case` 后可以紧接多个值，并且对于条件较为灵活。同时，在 `switch` 中不需要添加 `break` 语句。

```go
a := 10
switch a {
case 20, 10:
 fmt.Println("a 是 10 或 20")
case 30:
 fmt.Println("a 是 30")
default:
 fmt.Println("a 是其他数字")
}

switch {
case a >= 10:
 fmt.Println("a 大于等于 10")
default:
 fmt.Println("a 小于 10")
}
```

### 循环语句

不同于其他编程语言，Go 语言对于循环只有 `for` 一个关键字。同时，Go 语言的 `for` 关键字十分强大，可以实现传统编程语言的 `for`、`while` 等功能。

```go
for i := 0; i < 10; i++ {
 fmt.Println(i)
}

a := 10
for a <= 20 {
 // 相当于 while (a<=20)
 fmt.Println(a)
 a++
}

b := 0
for {
 // 无限循环，相当于 while (true)
 b++
 if b == 10 {
  break
 }
}
```

与其他语言类似，Go 语言传统 `for` 循环语法中任意部分都可以省略。如下代码为等价的：

```go
for ; ; {}
for true {}
for {}  // 一般使用这种形式
```

另外，Go 语言有一种 `for-range` 循环。其可以用于遍历容器。

如下为遍历数组的用法：

```go
arr := []int{1, 2, 3}
for i, v := range arr {
 fmt.Printf("正在遍历第 %v 个元素，值为 %v\n", i, v)
}
// 正在遍历第 0 个元素，值为 1
// 正在遍历第 1 个元素，值为 2
// 正在遍历第 2 个元素，值为 3
```

遍历一个哈希表：

```go
mp := map[string]int{
 "one":   1,
 "two":   2,
 "three": 3,
}
for k, v := range mp {
 fmt.Printf("k = %v, v = %v\n", k, v)
}
// k = three, v = 3
// k = one, v = 1
// k = two, v = 2
```
