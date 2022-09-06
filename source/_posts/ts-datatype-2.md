---
title: TypeScript 学习笔记 3——类型（下）
date: 2022-09-06 22:36:56
categories:
- [编程语言, TypeScript]
tags:
- TypeScript
---

本文主要介绍 TypeScript 种的枚举（`enum`）类型，以及 `type` 和 `interface` 的区别。

<!-- more -->

## `enum`

一般在需要进行某种映射关系的时候，使用 `enum`。例如，从后端获取到某个数据，前端对其进行判断的时候使用，使其更有语义化。

```typescript
enum Status {
  TODO = 1, // 1
  DONE,     // 2
  ARCHIVED, // 3
  DELETED,  // 4
}

// 假设 st 是从后端服务器获取到的数据
let st: Status = 3
if (st === Status.TODO) {
  console.log('TODO')
} else if (st === Status.DONE) {
  console.log('DONE')
} else if (st === Status.ARCHIVED) {
  console.log('ARCHIVED')
} else if (st === Status.DELETED) {
  console.log('DELETED')
}

st = Status.ARCHIVED
```

## `type`

`type` 是指类型别名，用于给其他类型取个名字，而不是产生一个新的数据类型。

```typescript
type Name = string  // 为 string 取个名叫 Name
type FalseLike = '' | 0 | null | undefined | false // 代指所有类false的值
type Point = { x: number; y: number } // 对象
type Points = Point[]   // 数组
type Line = [Point, Point] // 元组
type Circle = { center: Point; radius: number } // 复杂的对象
type Fn = (a: number, b: number) => number // 函数

// 带有属性的函数
type FnWithProps = {
    (a: number, b: number): number
    prop1: Name
}
const fnWithProp: FnWithProps = (x, y) => x + y
fnWithProp.prop1 = 'Hi'
```

## `interface`

`interface` 用于声明一个接口，描述对象的属性。用于描述一个对象。

```typescript
type TA = {
  a: string
  b: string
}
interface IA {
  a: string
  b: string
}

type TB = {
  [k: string]: string
}
interface IB {
  [k: string]: string
}
```

## `type` 和 `interface` 的区别

1. `interface` 只 **描述对象**，`type` 则描述所有数据。
2. `type` 仅仅是类型别名，`interface` 则是类型声明。
3. `type` 不可以重新赋值，`interface` 多次定义会合并。

  ```typescript
  interface Person {
      name: string
  }
  interface Person {
      age: number
  }
  const p: Person = {
    name: "张三",
    age: 18
  }
  ```

  一般对外的 API 尽量使用 `interface`，以方便扩展。对内的 API 使用 `type`，防止代码分散。
