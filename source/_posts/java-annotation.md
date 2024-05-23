---
title: Java 注解笔记
date: 2024-05-23 12:32:57
categories:
- [编程语言, Java]
tags:
- Java
---
<!-- more -->
## 理解注解

用法：`@注解`

注解本身是添加在 Java 源程序上的，但注解本身并不会对程序产生影响，只是提供额外的信息。他需要额外的 **注解处理工具**（APT） 来读取注解信息，并根据注解做进一步的处理。

在极端情况下，对于同一个注解，在不同的注解处理工具中，可能产生不同的作用

## Java 内置常用注解

由于是 Java 本身提供的，因此 Java 编译器（javac）默认会提取并且处理这些注解。

### `@Override`

该注解要求被修饰的方法必须重写父类、实现方法，否则报错。

### `@Deprecated`

该注解用于标注某个类、某个方法、某个成员变量等过时。

该注解有两个重要的参数：

- `forRemoval`：指定该单元会在将来的版本中被移除；
- `since`：指定该单元从哪个版本开始被标记过时。

如果调用被标记过时的单元，在编译时会有警告。

### `@SuppressWarnings`

用于压制程序的警告。如果 Java 代码中有警告，而确定程序不存在问题，可以使用该注解压制警告。

滥用该注解可能导致负面影响。

### 堆污染警告和 `@SafeVarargs`

varargs 是个数可变的参数，个数可变的参数本质上是数组。

 Java 允许声明泛型数组，但不可以创建泛型数组。除非使用通配符。

如果方法中个数可变的参数带了泛型，可能引发 **堆污染**警告。

### `@FunctionalInterface`

要求被修饰的接口必须是函数式接口（只能有一个抽象方法），否则报错。


## 自定义注解

格式：

```java
[修饰符] @interface 注解名 {
	变量类型 变量名() [default 默认值];
}
```

### 标记注解（无任何成员变量的注解）

该注解没有定义任意成员变量，意味该注解不能指定额外的信息。

这种注解的唯一作用是根据是否出现来传递信息。

### 元数据注解（带成员变量的注解）

这种注解允许在使用时为成员变量指定值，这样一个注解可以传入多个数据。

当注解只要指定一个 `value` 成员变量值时，可以省略 `value` 名称。

## JDK 的元注解

元注解：用于修饰注解。当希望定义自己的注解时，程序使用元注解来修饰。

### `@Retention`

用于指定该注解可以保留到生命时候，`value` 属性为如下 3 个枚举值：

- `RetentionPolicy.SOURCE`：被修饰的注解只能保留在源代码中，编译后，该注解就被丢弃。该注解必须在编译时处理。
- `RetentionPolicy.CLASS`：被修饰的注解只保留在 class 代码中，被编译后，注解还存在，但程序运行时无法读取。该注解要么在编译时处理，要么去 class 文件读取。
- `RetentionPolicy.RUNTIME`：被修饰的注解将一直保留。该注解可以在任意时间处理。

### `@Target`

用于指定被修饰的注解只能用于修饰什么程序单元。

默认情况下，自定义注解可以修饰任何的程序单元。

### `@Documented`

用于指定被修饰的注解将会被 javadoc 工具提取到文档中。

### `@Inherited`

用于指定被修饰的注解自动具有继承性。

如，使用 `@Inherited` 修饰了 `@A`，`@A` 修饰了类 B，那么类 B 的子类自动具有 `@A` 注解。

### `@Repeatable`

格式：`@Repeatable(容器注解.class)`

在 Java 8 之前，如果需要重复一个注解修饰相同的程序单元，需要显式使用一个容器注解来包装这些重复的注解。

例如：

```
@interface Foo {
  String name();
}
@interface Foos {
  Foo[] value();
}
@Foos({
  @Foo(name="foo"),
  @Foo(name="bar")
})
class Main {
  // ...
}
```

使用 `@Repeatable` 后，即可变为如下代码

```
@Repeatable(Foos.class)
@interface Foo {
  String name();
}
@interface Foos {
  Foo[] value();
}

@Foo(name="foo")
@Foo(name="bar")
class Main {
  // ...
}
```

## 处理注解

处理注解大致可以分为

1. 编译时提取注解信息，根据信息作进一步的处理。为 javac 命令指定 `-processor` 选项指定自己的注解处理工具（APT）类。
2. 运行时程序通过反射提取注解信息（必须是 `RUNTIME` 保留期）。

### 运行时读取注解

Java 中所有可以被注解修饰的程序单元都实现了 `AnnotatedElement` 接口，该接口代表所有可接受注解的程序单元。

`AnnotatedElement` 接口提供如下常用方法：

- `isAnnotationPresent(注解类)`：判断某个注解是否存在
- `getAnnotation(注解类)`：获取某个注解
- `getAnnotations()`：获取该程序单元上所有的注解
- `getAnnotationsByType(注解类)`：获取该程序单元上指定类型的所有注解。主要针对 Java 8 的重复注解。

### 注解处理实例

TODO
