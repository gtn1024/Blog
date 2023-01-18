---
title: Go 语言入门 —— 数据结构
date: 2023-01-18 20:34:48
categories:
- [编程语言, Go]
tags:
- Go
---
本文主要介绍 Go 语言中的一些基本的数据结构。

<!-- more -->

## 数组

与其他语言类似，Go 语言的数组是长度不可变的。数组的定义如下：

```go
[长度]数据类型
```

如下为数组的定义及赋值操作：

```go
var a [10]int
for i := 0; i < 10; i++ {
 a[i] = i
}
```

在定义数组的时候，可以为数组赋初始值。此时，当数组元素确定时，数组的长度可以自动推导出来。

```go
var a []int = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
var b = []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
c := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
```

## 切片

Go 语言中的切片（slice）就相当于其他编程语言中可以自动扩容的动态数组，如 C++ 中的 `vector`、Java 中的 `ArrayList` 等。

定义切片的语法如下：`make(切片类型, 长度, 容量)`。其中，容量可以省略，如果被省略，则容量和切片的长度一致。

```go
slc1 := make([]int, 3)
fmt.Println(slc1, len(slc1), cap(slc1))
// [0 0 0] 3 3

slc2 := make([]int, 3, 5)
fmt.Println(slc2, len(slc2), cap(slc2))
// [0 0 0] 3 5
```

### 添加元素

在切片的末尾添加元素，可以使用 `append` 函数进行操作。`append` 函数在添加元素时，会自动根据切片的容量对切片进行扩容。同时，函数将返回新的切片。

```go
s := make([]int, 0, 10)
s = append(s, 1, 2)
fmt.Printf("%v\n", s) // [1 2]
```

### 获取切片某一范围

在 Go 语言中，如果需要获取切片的某个范围，可以使用 `s[a : b]` 的语法。其取出来的范围区间是左闭右开（`[a, b)`，即 `b` 取不到）的。

```go
s := make([]int, 0, 10)
s = append(s, []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}...)
fmt.Println(s) // [1 2 3 4 5 6 7 8 9 10]

fmt.Println(s[1:6]) // [2 3 4 5 6]
```

## 哈希

在 Go 语言中，定义哈希的格式是 `map[K]V`，其中 `K` 为 key 的类型，`V` 为 value 的类型。如下演示了两种哈希的定义方式：

```go
hsh1 := map[string]int{
 "one":   1,
 "two":   2,
 "three": 3,
}
hsh1["four"] = 4
fmt.Println(hsh1["one"]) // 1

hsh2 := make(map[string]int)
hsh2["one"] = 1
```

如果需要删除一个 key，可以直接使用 `delete` 函数。

```go
delete(hsh1, "two")
fmt.Println(hsh1["two"]) // 0
```

## `range`

在 [上一篇](/archives/go-basic-syntax/) 中，已经提了 `for-range` 循环。`range` 可以迭代容器中的元素。对于数组、切片等类型，其返回元素所在的下标以及元素值。对于哈希，其返回 key 和 value。

```go
a := []int{1, 2, 3}
for i, v := range a {
 fmt.Printf("i = %v, v = %v\n", i, v)
}
// i = 0, v = 1
// i = 1, v = 2
// i = 2, v = 3

m := map[string]int{
 "one":   1,
 "two":   2,
 "three": 3,
}
for k, v := range m {
 fmt.Printf("k = %v, v = %v\n", k, v)
}
// k = one, v = 1
// k = two, v = 2
// k = three, v = 3
```

## 结构体

Go 语言中，定义结构体的语法如下：

```go
type 结构体名 struct {
 // 成员
}
```

如下为结构体最基本使用示例：

```go
type Point struct {
 x int
 y int
}
p1 := Point{1, 1}
p2 := Point{x: 2, y: 2}

fmt.Printf("%#v\n", p1) // main.Point{x:1, y:1}
fmt.Printf("%#v\n", p2) // main.Point{x:2, y:2}
```
