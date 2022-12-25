---
title: Java 17新特性：密封类
date: 2022-12-25 18:52:07
categories:
- [编程语言, Java]
tags:
- Java
- 面向对象
---
在 Java 17 之前，一个 Java 类只有两种状态：可派生和不可派生（即 `final` 类），这导致如果需要对类进行派生的时候，我们无法将其设置为 `final` 类，也就无法限制其他人对于该类的派生。

Java 17 带来的密封类解决了这个问题，可以限制父类只能派生预先指定的子类，不允许再派生其他子类。

<!-- more -->

## 密封类语法

密封类的语法如下：

```java
[修饰符] sealed class 类名 permits 子类列表 {
  // ...
}
```

使用密封类时没必须满足以下要求：

- 子类和密封类要么处于同一个模块，要么术语同一个类。如果在未命名的模块中，则必须位于同一个包中。
- 密封类允许派生的子类必须直接继承密封类。
- 密封类的子类必须使用 `final`、`sealed` 或 `non-sealed` 修饰。
  - `final`：无法再次派生子类。
  - `sealed`：子类仍然为密封类。
  - `non-sealed`：非密封类，可以自由派生子类。

## 密封类例子

密封类 A 允许派生 B 和 C

```java
public sealed class A permits B, C { }
```

B 同样为密封类，允许派生出 D

```java
public sealed class B extends A permits D { }
```

D 为 `final` 类，即无法再进行派生子类

```java
public final class D extends B { }
```

C 为非密封类，允许进行任意派生

```java
public non-sealed class C extends A { }
```

对应的继承关系图如下：

{% asset_img image-20221225180518140.png %}

特别地，如果密封类和子类均位于同一个文件中，`permits` 可以省略。

```java
sealed class A { }

sealed class B extends A { }

non-sealed class C extends A { }

final class D extends B { }
```

## 密封接口

密封接口与密封类类似，密封接口的实现类也必须使用 `sealed`、`non-sealed`、`final` 修饰，而密封接口下的子接口也必须为 `sealed`、`non-sealed` 修饰（接口不可能为 `final` 修饰）

```java
sealed interface Foo { }
non-sealed interface Bar {}
sealed class Tar implements Foo {}
final class Car implements Foo {}
class Par implements Bar {}
```
