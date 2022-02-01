---
title: Java 8 Stream 知识整理
date: 2022-01-22 19:28:09
categories:
- [编程语言, Java]
tags:
- Java
- Stream
---
Java 8 的 Stream，又一个非常好用的特性。

<!-- more -->

## 综述

Java 8 新增了 **Stream API**。**Stream API**有点类似使用**SQL 语句**，可以将**集合**中的元素进行过滤。

与**Stream API**相关的接口有`Stream`、`IntStream`, `LongStream`, `DoubleStream`（因为 Java 的泛型不支持基本数据类型，而又因频繁的装箱、拆箱存在效率问题，故额外有后三者）。

使用`Stream`操作时，我们通常使用**链式操作**，即将多条代码合并成一条代码（事例将在**使用`Supplier`创建**中给出）。

## Java Collection 体系数据处理的演进

本小节用于测试的代码如下：

```java
public record User(Integer id, String name, Integer money) { }

final var users = Arrays.asList(
      new User(1, "张三", 200),
      new User(2, "李四", 200),
      new User(3, "王五", 10000),
      new User(4, "赵六", 20000),
      new User(5, "王强", 80000)
);
```

### 通过不同方法来过滤不同数据

我们过滤数据首先想到的方法是针对各个需求来定义一个个的方法。

例如，产品经理给了你一个**筛选出所有 id 大于 3 用户**的需求，可以定义如下`getIdGreaterThan3`的方法。

```java
public class CollectionStream {
    public static void main(String[] args) {
        // users 定义
        final var newUsers = getIdGreaterThan3(users);
        for (User user : newUsers) {
            System.out.println(user);
        }
    }
    public static List<User> getIdGreaterThan3(List<User> users) {
        final var newUsers = new ArrayList<User>();
        for (User user : users) {
            if (user.id() > 3) {
                newUsers.add(user);
            }
        }
        return newUsers;
    }
}

/*
  输出：
  User[id=4, name=赵六, money=20000]
  User[id=5, name=王强, money=80000]
*/
```

第二天，产品经理要求你**筛选出所有姓“王”的用户**的需求，定义`getAllWang`方法：

```java
public class CollectionStream {
    public static void main(String[] args) {
        // users 定义
        final var newUsers = getAllWang(users);
        for (User user : newUsers) {
            System.out.println(user);
        }
    }
    public static List<User> getAllWang(List<User> users) {
        final var newUsers = new ArrayList<User>();
        for (User user : users) {
            if (user.name().startsWith("王")) {
                newUsers.add(user);
            }
        }
        return newUsers;
    }
}

/*
  输出：
  User[id=3, name=王五, money=10000]
  User[id=5, name=王强, money=80000]
*/
```

第三天，产品经理要求你开发**所有钱大于 10000 的用户**的需求，你瞅了瞅他，写出了如下代码：

```java
public class CollectionStream {
    public static void main(String[] args) {
        // users 定义
        final var newUsers = getRichPeople(users);
        for (User user : newUsers) {
            System.out.println(user);
        }
    }
    public static List<User> getRichPeople(List<User> users) {
        final var newUsers = new ArrayList<User>();
        for (User user : users) {
            if (user.money() > 10000) {
                newUsers.add(user);
            }
        }
        return newUsers;
    }
}

/*
  输出：
  User[id=4, name=赵六, money=20000]
  User[id=5, name=王强, money=80000]
*/
```

此时此刻，你会发现我们似乎写了**很多**重复的方法...

### 使用接口来代替重复操作

在 Java 世界中，对于相似的操作我们通常使用接口定义，对于不同的操作我们相应的定义不同的实现类来实现不同的功能。

```java
public class CollectionStream {
    public static void main(String[] args) {
        // users 定义
        for (User user : getUsers(users, new JudgeIdGreaterThan3())) {
            // 判断ID是否大于3
            System.out.println(user);
        }

        for (User user : getUsers(users, new JudgeIsWang())) {
            // 判断是否姓王
            System.out.println(user);
        }

        for (User user : getUsers(users, new JudgeIsRich())) {
            // 判断是否有钱
            System.out.println(user);
        }
    }

    public static List<User> getUsers(List<User> users, Judge condition) {
        final var newUsers = new ArrayList<User>();
        for (User user : users) {
            if (condition.test(user)) {
                newUsers.add(user);
            }
        }
        return newUsers;
    }

    public static class JudgeIdGreaterThan3 implements Judge {
        @Override
        public boolean test(User user) {
            return user.id() > 3;
        }
    }

    public static class JudgeIsWang implements Judge {
        @Override
        public boolean test(User user) {
            return user.name().startsWith("王");
        }
    }

    public static class JudgeIsRich implements Judge {
        @Override
        public boolean test(User user) {
            return user.money() > 10000;
        }
    }

    public interface Judge {
        boolean test(User user);
    }
}
```

当然，我们也可以使用**匿名内部类**来实现同样的功能。

### 使用 Java 8 提供的`Predicate`接口

事实上，从 Java 8 开始，JDK 提供了一个名为`Predicate`的**接口**，其作用与上方自己写的`Judge`接口类似。同时，因为它是**函数式接口**，我们可以很轻松地使用 Lambda 表达式。

{% asset_img 16374142332314.jpg %}

```java
public class CollectionStream {
    public static void main(String[] args) {
        // users 定义
        for (User user : getUsers(users, user -> user.id() > 3)) {
            // 判断ID是否大于3
            System.out.println(user);
        }

        for (User user : getUsers(users, user -> user.name().startsWith("王"))) {
            // 判断是否姓王
            System.out.println(user);
        }

        for (User user : getUsers(users, user -> user.money() > 10000)) {
            // 判断是否有钱
            System.out.println(user);
        }
    }

    public static List<User> getUsers(List<User> users, Predicate<User> condition) {
        final var newUsers = new ArrayList<User>();
        for (User user : users) {
            if (condition.test(user)) {
                newUsers.add(user);
            }
        }
        return newUsers;
    }
}
```

### 总结

从最初编写一个一个独立的方法，到后面自行开发接口逐步地通用化，再到使用 Lambda 表达式，我们重复的工作被逐步逐步地简化。

事实上，在 Java 推出`Predicate`接口，开源世界早已对于集合操作有了简化。例如以 [Google Guava](https://guava.dev/) 为代表的第三方框架，以及以 [Groovy](http://www.groovy-lang.org/) 、 [Scala](https://scala-lang.org/) 、 [Kotlin](https://kotlinlang.org/) 为代表的编程语言。

## Steam 核心知识

### 创建 Stream

#### 使用 Stream.of() 创建

最简单的方法是使用`Stream.of()`来创建 Stream：

```java
Stream<String> foo = Stream.of("Java", "Python", "Kotlin", "JavaScript");
foo.forEach(System.out::println);
```

以上代码创建了一个由 4 个编程语言组成的流，并使用`forEach()`方法将其打印出来（`forEach`方法的参数为`Consumer<T>`函数式接口，可直接使用 [Lambda 表达式](https://www.getaoning.com/archives/258) ）

#### 使用数组创建

使用数组创建 Stream 可以使用`Arrays.stream()`方法来创建。

```java
String[] foo = new String[]{"Java", "Python", "Kotlin", "JavaScript"};
Stream<String> bar = Arrays.stream(foo);
bar.forEach(System.out::println);
```

#### 使用集合框架创建

同样，Stream 也可以基于集合框架来创建，`Collection`接口提供了`stream()`的抽象方法，使得`Set`、`List`、`Map`等集合拥有创建 Stream 的能力。

这里以 `List`为例：

```java
List<String> foo = List.of("Java", "Python", "Kotlin", "JavaScript");
Stream<String> bar = foo.stream();
bar.forEach(System.out::println);
```

#### 使用`Supplier`创建

我们也可以通过`Stream.generate(Supplier<? extends T> s)`方法来创建 Stream。这里参数要求为`Supplier`，它同样是个函数式接口。

```java
// 以下事例均使用`链式操作`
Stream.generate(() -> new Random().nextInt(100))
      .limit(10)   // 此处使用`limit`来闲置元素个数
      .forEach(System.out::println);
```

### 中间操作

**中间操作**是指调用方法以后，仍然返回`Stream`对象。Java Stream 中，允许有多个**中间操作**。

#### map

`Stream.map(Function<? super T,​? extends R> mapper)`是将一个某个操作映射到 Stream 中每个元素上。同样，`map`的参数为函数式接口。

例如，如下代码实现了对于每个元素进行平方：

```java
Stream.of(1, 2, 3, 4, 5)
      .map(i -> i * i)
      .forEach(System.out::println);   // 1, 4, 9, 16, 25
```

`map`方法也可以对于元素中的对象进行操作，例如：

```java
List.of("Java", "Kotlin", "JavaScript")
    .stream()
    .map(String::toUpperCase)     // 将元素转为大写
    .forEach(System.out::println);
```

#### filter

`Stream.filter​(Predicate<? super T> predicate)`可以对于 Stream 中元素进行过滤。

例如，以下代码将一组数字中所有偶数打印出来：

```java
IntStream.of(1, 2, 3, 4, 5, 6, 7, 8, 9)
         .filter(i -> i % 2 == 0)
         .forEach(System.out::println);
```

如果 Stream 中元素为对象，同样可以进行过滤。例如，如下代码实现了将年龄为 18 岁以下的未成年人过滤：

```java
record Person(String name, int age) { } // 需要使用 Java 16 及以上版本

List<Person> peoples = List.of(
    new Person("张三", 30),
    new Person("李四", 16),
    new Person("王五", 18),
    new Person("王强", 22),
    new Person("小宋", 8)
);
peoples.stream()
       .filter(it -> it.age() >= 18)
       .forEach(System.out::println);

/*
输出：
Person[name=张三, age=30]
Person[name=王五, age=18]
Person[name=王强, age=22]
*/
```

#### parallel

通常情况下，对 Stream 的元素进行处理是单线程的，即一个一个元素进行处理。但是很多时候，我们希望可以并行处理 Stream 的元素，因为在元素数量非常大的情况，并行处理可以大大加快处理速度。

```java
record Person(String name, int age) { } // 需要使用 Java 16 及以上版本

List<Person> peoples = List.of(
    new Person("张三", 30),
    new Person("李四", 16),
    new Person("王五", 18),
    new Person("王强", 22),
    new Person("小宋", 8)
);
peoples.stream()
       .parallel()  // 将普通 stream 转换为并行 stream
       .filter(it -> it.age() >= 18)    // 并行筛选
       .forEach(System.out::println);
```

#### sorted

`Stream.sorted()`可以实现对 Stream 中元素进行排序，所排序的元素必须实现`Comparable`。当然也可以在参数中填入自己的`Comparator`。

如下代码对随机数进行从小到大的排序：

```java
IntStream.of(5, 7, 3, 2, 6, 0, 9)
         .sorted()
         .forEach(System.out::println);

// 输出：0 2 3 5 6 7 9
```

#### distinct

`Stream.distinct()`可以对于 Stream 中的元素进行去重：

```java
IntStream.of(5, 8, 3, 4, 5, 3, 6, 9, 5, 3, 7)
         .distinct()
         .forEach(System.out::println);

// 输出：5 8 3 4 6 9 7
```

#### skip

`Stream.skip()`可以对于 Stream 中前几个元素进行跳过

```java
IntStream.of(1, 2, 3, 4, 5, 6, 7, 8, 9)
         .skip(3)
         .forEach(System.out::println);

// 输出：4 5 6 7 8 9
```

#### limit

`Stream.limit()`可以只保留前几个元素：

```java
IntStream.of(1, 2, 3, 4, 5, 6, 7, 8, 9)
         .limit(5)
         .forEach(System.out::println);

// 输出：1 2 3 4 5
```

#### concat

`Stream.concat()`用于将两个 Stream 合并：

```java
IntStream foo = IntStream.of(1, 2, 3);
IntStream bar = IntStream.of(4, 5, 6);
IntStream.concat(foo, bar)
         .forEach(System.out::println);

// 输出：1 2 3 4 5 6
```

### 终结操作

**终结操作**是指调用方法后，返回非`Stream`的操作，包括`void`。Java Stream 中，**只允许有一个终结操作**。

**终结操作**主要有如下方法：

- `forEach`：对于`Stream`中每个元素进行遍历，常见用途如打印元素。
- `count`/`max`/`min`：返回**元素个数**/**最大值**/**最小值**。
- `anyMatch`/`allMatch`/`noneMatch`：**任意一个符合**/**全部符合**/**都不符合**给定的`Predicate`条件返回`true`。
- `findFirst`/`findAny`：返回流中**第一个**/**任意一个**元素。
- 🌟`collect`：**几乎**可以将一个`Stream`对象转换为任何内容，例如以下代码可以将姓王的用户筛选出来，并转换为 List 集合。

    ```Java
    final var ls = users.stream()
         .filter(it -> it.name().startsWith("王"))
         .collect(Collectors.toList());
    ```

    因为`collect`方法较为复杂，有兴趣可以自行阅读 JDK 文档。

## IDEA 流调试器

IDEA 中内置了一个名为**Java Stream Debugger**插件（如果没有请确保自己为最新版的 IDEA，或者尝试前往 IDEA 插件市场安装），该插件可以通过可视化的方式直观地看到 Stream 的处理过程。

使用方式：

1. 在 Stream 流中打上断点；
2. 启动 Debug 模式；
3. 断点暂停后，点击 Debug 面板上的**Trace Current Stream Chain**按钮（如图所示）

   {% asset_img 16373728293511.jpg %}

该插件可以分步地将 Stream 操作以可视化的形式呈现出来（当然也可以通过下方的**Flat Mode**按钮在同一个窗口中看到所有操作）

{% asset_img 16373728823304.jpg %}

{% asset_img 16373729705219.jpg %}

### 演示 1 - filter

```java
public class CollectionStream {
    public record User(Integer id, String name, Integer money) { }

    public static void main(String[] args) {
        final var users = Arrays.asList(
                new User(1, "张三", 200),
                new User(2, "李四", 200),
                new User(3, "王五", 10000),
                new User(4, "赵六", 20000),
                new User(5, "王强", 80000)
        );
        users.stream()
                .filter(it -> it.money() > 10000)
                .collect(Collectors.toList());
    }
}
```

{% asset_img 16373731272913.jpg %}

### 演示 2 - distinct

```java
public class CollectionStream {
    public static void main(String[] args) {
        final var list = Arrays.asList(1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 2);
        list.stream()
                .distinct()
                .forEach(System.out::println);
    }
}
```

{% asset_img 16373734336456.jpg %}

### 演示 3 - sorted

```java
public class CollectionStream {
    public static void main(String[] args) {
        final var list = Arrays.asList(6, 4, 3, 5, 6, 7, 8, 2);
        list.stream()
                .sorted()
                .forEach(System.out::println);
    }
}
```

{% asset_img 16373736982517.jpg %}

### 演示 4 - map

```java
public class CollectionStream {
    public record User(Integer id, String name, Integer money) { }

    public static void main(String[] args) {
        final var users = Arrays.asList(
                new User(1, "张三", 200),
                new User(2, "李四", 200),
                new User(3, "王五", 10000),
                new User(4, "赵六", 20000),
                new User(5, "王强", 80000)
        );
        users.stream()
                .filter(it -> it.name().startsWith("王"))
                .map(User::name)
                .forEach(System.out::println);
    }
}
```

{% asset_img 16373757675756.jpg %}

## 参考资料

- [使用 Stream —— 廖雪峰](https://www.liaoxuefeng.com/wiki/1252599548343744/1322402873081889)
- [Collection 与 Stream 的前世今生](https://xiedaimala.com/tasks/1a1a8ea8-4c7a-4bb1-9337-b10296004f05/video_tutorials/fb2ecfc0-216c-41d8-9bb4-04a744f31f39)
