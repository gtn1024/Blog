---
title: TypeScript 学习笔记 2——类型（上）
date: 2022-09-03 19:03:56
categories:
- [编程语言, TypeScript]
tags:
- TypeScript
---
本文主要介绍如何在 TypeScript 中描述不同类型的对象。

<!-- more -->
文章目录：

- {% post_link ts-intro %}
- {% post_link ts-datatype-1 %}

## 数据类型

在 JavaScript 中有如下数据类型：

- `null`
- `undefined`
- `string`
- `number`
- `boolean`
- `bigint`
- `symbol`
- `object` (包括 `Array`、`Function`、`Date` 等)

而 TypeScript 有如下类型

- JavaScript 中所有数据类型
- `void`
- `never`
- `enum`
- `unknown`
- `any`
- 自定义类型 `type` (类型别名)、`interface`

## 理解类型

值：

```javascript
null undefined
1 2 3 4 1.1 1.2 3.1415926
a b c d abc
true false
------------
{ }
{ name: 'js' }
new Date()
new String()
new Number()
```

通过集合的思想，对应类型如下：

```typescript
null undefined
type number = 1 | 1.1 | 1.11 | ... | 2 | ...
type string = 'a' | 'b' | 'ab' | ...
type boolean = true | false
------------
type Object = { ? } | Any | Function | String | Number | Boolean | RegExp | ...
```

在开发的过程中，通常不使用包装类型（如 `number`-`Number`、`boolean`-`Boolean`、`string`-`String`）。同时，`Object` 通常也不使用，因为其表示范围过大。例如，使用 `Object` 类型可以表示一个数字、数组、函数、正则表达式……

## 描述对象的数据类型

因为在 TypeScript 中使用 `Object` 类型表示对象，其范围过大。我们通常不用 `Object` 类型，而是定义特定的类型来描述一个对象。

### 用 class / constructor 描述

```typescript
const d: Date = new Date(); // d 只能为 Date 类型
const f: Function = () => console.log('a'); // f 只能为函数
const arr: Array = [1, 3, 5, 'a']; // arr 只能为数组
const brr: Array<number> = [1, 3, 5]; // brr 只能为元素为 number 类型的数组
```

### 用 `type` 或 `interface` 描述

#### 定义固定格式的类型

```typescript
type Person = {
  number: string;
  age: number;
}

const p1: Person = {
  number: '张三',
  age: 18,
}

// 错误，缺少 age
const p2: Person = {
  number: '张三',
}

// 错误，多了 gender
const p2: Person = {
  number: '张三',
  age: 18,
  gender: '男',
}
```

#### 定义可变类型

```typescript
type A = {
  [k: string]: number;
}

const a: A = {
 a: 123,
}
const b: A = {
 a: 123,
 b: 456,
}

// 错误，value 只能为 number
const c: A = {
 a: 123,
 b: '字符串',
}
```

除了使用该方法，我们还可以使用 `Record` 来定义类型

```typescript
type B = Record<string, number>
const a: B = {
 a: 123,
}
const b: B = {
 a: 123,
 b: 456,
}

// 错误，value 只能为 number
const c: B = {
 a: 123,
 b: '字符串',
}
```

## 描述各种对象

### 数组对象

```typescript
type A = string[]
// 等价于：
type AA = Array<string>
const a: A = ['h', 'i']
const aa: AA = ['h', 'i']

type B = number[]
// 等价于：
type BB = Array<number>
const b: B = [1, 0.6]
const bb: BB = [1, 0.6]
```

元组：

```typescript
type A = [string, string, string]
const a: A = ['hi1', 'hi2', 'hi3']
console.log(a[1]) // hi2
// 错误，缺少一个元素
const err: A = ['hi1', 'hi2']

type B = [string, number, boolean]
const b: B = ['张三', 18, true]

type C = [string[], number[]]
const c: C = [['a', 'b', 'c', 'd'], [1, 3.14, 10086]]
```

思考题：

```typescript
type A = [1, 2, 3]
const a: A = [1, 2, 3] // a只能为 [1, 2, 3]
```

### 函数对象

函数类型的定义格式如下：`(参数列表) => 返回值类型`

```typescript
type FnA = () => void 
const fnA: FnA = () => {
  console.log('fnA')
}

type AddTwoNum = (a: number, b: number) => number
const addTwoNum: AddTwoNum = (a: number, b: number) => {
  return a + b
}
console.log(addTwoNum(1,2)) // 3
```

在定义函数时，形参列表可以根据实际的使用情况进行删除（即没用的参数可以不用添加上去），如果前面的参数没有使用到可以使用 `_` 作为占位符，但是在调用函数的时候要将参数列表写全。同时，形参类型可以省略（类型推导）。

```typescript
type FnB = (a: number, b: number) => number
const aFnB: FnB = () => 1
console.log(aFnB(1, 2)) // 参数不能省略，返回 1

const bFnB: FnB = (a, b) => a + b // a、b的参数类型可以省略
console.log(bFnB(1, 2)) // 返回 3

const cFnB: FnB = (_, b) => b
console.log(cFnB(1, 2)) // 返回 2
```

==如果函数使用了 `this`，则只能使用普通函数，而不能使用箭头函数。==

```typescript
type Person = {
  name: string
  sayHi: SayHi
}
type SayHi = (this: Person, name: string) => void
const sayHi: SayHi = function(name) {
  console.log(`${this.name} says hi to ${name}!`)
}
const p: Person = {
  name: '张三',
  sayHi: sayHi,
}
p.sayHi('法外狂徒')
sayHi.call(p, '法外狂徒')
sayHi.apply(p, ['法外狂徒'])
```

### 其他对象

除了普通对象、数组对象、函数对象以外的对象通常使用 `class` 来描述。

```,
const d: Date = new Date()
const r1: RegExp = /ab+c/
const r2: RegExp = new RegExp("ab+c")
const map: Map<string, number> = new Map()
map.set('张三', 1)
const set: Set<string> = new Set()
set.add('1')
set.add('2')
set.add('1')
```

事实上，TypeScript 可以根据赋值的类型进行推导：

```typescript
const d = new Date() // Date
const r1 = /ab+c/    // RegExp 
const r2 = new RegExp("ab+c") // RegExp
const map = new Map<string, number>() // Map<string, number>
const set = new Set<string>() // Set<string>
```

## `any` 和 `unknown`

`any` 指可以赋值为任何类型的类型，其不受 TypeScript 类型系统的控制。

`unknown` 指并不知道该对象为什么类型，通常用于从远端返回来的数据。对其进行操作时，需要对其进行类型断言。

```typescript
const a: any = '1,2,3';
console.log(a.split(','));

const b: unknown = '1,2,3';
console.log((b as string).split(','));

const c: any = 123;
console.log(c.split(',')); // 报错
```

## `never` 类型

`any` 指在 TypeScript 中所有的类型，`never` 则代表除 `any` 之外的类型（即其为空集）。出现 `never` 时通常为错误。

```typescript
// A 的类型为 never
type A = string & number;

type B = string | number;
const b: B = ('hello' as any);
if (typeof b === 'string') {
  // b 为 string
} else if (typeof b === 'number') {
  // b 为 number
} else {
  // b 为 never
}
```
