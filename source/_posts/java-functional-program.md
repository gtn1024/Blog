---
title: Java 函数式编程详解
date: 2021-09-28 11:04:31
categories:
- [编程语言, Java]
tags:
- Java
- 函数式编程
- Lambda
---
Java 8 中有着许许多多特别好用的特性，Lambda 表达式就是其中一个。

<!-- more -->

## 函数式接口

**函数式接口**指**只有**一个**抽象方法**的接口。如果定义函数式接口只需在接口上方加入`@FunctionalInterface`注解。**函数式接口**中可以有**类方法**、**默认方法**等，**但只能有一个抽象方法**。

```java
@FunctionalInterface
interface Foo {
  void foo();

  static int sum(int a, int b) {
    // 可以有类方法
    return a + b;
  }

  default void bar() {
    // 可以有默认方法
    System.out.println("bar");
  }
}
```

在**Lambda 表达式**出现之前，通常使用 [**匿名内部类**](/archives/java-oop#匿名内部类) 来创建实例：

```java
Foo f = new Foo() {
  @Override
  public void foo() {
    System.out.println("匿名内部类测试...");
  }
};
f.foo();    // 匿名内部类测试...

System.out.println(Foo.sum(1, 2)); // 3
f.bar();    // bar
```

## Lambda 表达式

由以上代码可见，使用**匿名内部类**时会有大量多余的代码（如`new Foo()`、重写唯一的抽象方法）。Java 8 引入了 Lambda 表达式，用于简化代码。

**Lambda 表达式本质上就是函数式接口的匿名内部类。**

以上代码使用 Lambda 表达式则为：

```java
Foo f = () -> {
  System.out.println("匿名内部类测试...");
};
```

**如果该抽象方法有参数，参数不可省略**

例如：

```java
@FunctionalInterface
interface Foo {
  void foo(String name);
}
public class LambdaTest {
  public static void main(String[] args) {
    Foo f = (String name) -> {   // 参数类型可以省略
      System.out.println("欢迎回来，" + name);
      System.out.println("——来自Lambda表达式");
    };
    f.foo("巴掌");
    // 欢迎回来，巴掌
    // ——来自Lambda表达式
  }
}
```

## Lambda 表达式简化

Lambda 表达式可以有如下简化：

- 形参列表中参数类型可以省略；
- 如果形参列表只有一个参数，那么圆括号可以省略；
- 如果方法体只有一行代码，花括号可以省略；
- 如果方法体只有一行代码，且为`return`语句，`return`可以省略。

例如：

```java
@FunctionalInterface
interface Foo {
  int foo(int a);
}
public class LambdaTest {
  public static void main(String[] args) {
    Foo f = a -> a * a;
    System.out.println(f.foo(5));   // 25
  }
}
```

## 方法引用和构造器引用 (重点)

**当方法体只有一条代码时才可以使用**。**方法引用**本质是**进一步省略形参列表**，形参列表顺序与传入参数的顺序完全相同。

### 引用类方法

**引用类方法**转化前的格式为`(参数列表) -> 类.类方法(参数列表)`，转化后为`类::类方法`。

```java
@FunctionalInterface
interface Foo {
  double min(double i1, double i2);
}

public class Test {
  public static void main(String[] args) {
//  Foo f = (i1, i2) -> Math.min(i1, i2);
    Foo f = Math::min;
    System.out.println(f.min(5.0, 2.0));  // 2.0
  }
}
```

### 引用实例方法

**引用实例方法**转化前的格式为`(参数1, 其他参数) -> 参数1.实例方法(其他参数)`，转化后为`类::实例方法`。

```java
@FunctionalInterface
interface Foo {
  String sub(String s, int start, int end);
}

public class Test {
  public static void main(String[] args) {
//  Foo f = (s, start, end) -> s.substring(start, end);
    Foo f = String::substring;
    System.out.println(f.sub("Java, yes!", 1, 4));  // ava
  }
}
```

### 引用特定对象的实例方法

**引用特定对象的实例方法**转化前的格式为`(参数) -> 某对象.实例方法(参数)`，转化后为`某对象::实例方法`。

```java
@FunctionalInterface
interface Foo {
  String sub(int start, int end);
}

public class Test {
  public static void main(String[] args) {
//  Foo f = (start, end) -> "Java, yes!".substring(start, end);
    Foo f = "Java, yes!"::substring;
    System.out.println(f.sub(1, 4));  // ava
  }
}
```

### 构造器引用

**构造器引用**转化前的格式为`(参数) -> 类.构造器(参数)`，转化后为`类::new`。

```java
@FunctionalInterface
interface Foo {
  StringBuilder foo(String s);
}

public class Test {
  public static void main(String[] args) {
//  Foo f = s -> new StringBuilder(s);
    Foo f = StringBuilder::new;
    System.out.println(f.foo("Welcome to Java World!"));
  }
}
```

## 参考资料

- [《疯狂 Java 讲义 · 第 5 版》](https://union-click.jd.com/jdc?e=&p=JF8BAMUJK1olXDYCV1pdAUoUB19MRANLAjZbERscSkAJHTdNTwcKBlMdBgABFksUB28BGlgRQl9HCANtdUpkA2twQgV1PE59KjxDcCNISg1pXVcZbQcyVF9cC04VBWsBHGslXQEyAjBdCUoWAm4NG14WbQcyVFlfC0oTAmYNGVoTWTYFVFdtUx55dQRLWCBQCXlcMgM9OHsnAF84K1slXjZAOlhYARtHBTtaHgsRXwNXA1cNC0hHBTwJGFkSDVJRB1ddOEkWAmsBKw)
- [跟着李刚老师学 Java（视频）](https://bfw.h5.xeknow.com/s/1YClVz)
