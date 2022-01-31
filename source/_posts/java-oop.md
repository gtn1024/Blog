---
title: Java 面向对象知识详解	
date: 2021-09-16 10:59:18
categories:
- [编程语言, Java]
tags:
- Java
- 面向对象
---
**目录**：

[TOC]

## TL;DR

面向对象 3 大类型：**类**、**接口**、**枚举**。

面向对象 4 大修饰符：`private` | `protected` | `public`(互斥)、`static`、`final`、`abstract`。

面向对象 5 大成员：**成员变量**、**方法**、**构造器**、**初始化块**、**内部类**。

## 总述

**面向对象编程**(Object-Oriented Programming, 简称 **OOP**)是一种编程范式。

在**面向对象编程**中，有两个重要的概念：

- **类**：一类事物的统称（例如**动物**类）
- **对象**：某个**类**中的实例（例如**狗**、**猫**）

在一个类中，有**成员变量**(**field**)、**方法**(**method**)、**构造器**(**constructor**)、**初始化块**、**内部类**(**nested class**)五大成员。

**牢记**：

**始终只定义你所关心的项目！**

**始终只定义你所关心的项目！**

**始终只定义你所关心的项目！**

举个例子：现定义一个**人类**(**Human**)，**成员变量**可以有**姓名**(**name**)、**性别**(**gender**)、**年龄**(**age**)、**身高**(**height**)、**体重**(**weight**)等，**方法**可以有**走**(**walk**)、**跑**(**run**)、**跳**(**jump**)、**吃**(**eat**)等。

对应的 [UML 图](https://en.wikipedia.org/wiki/Unified_Modeling_Language)为：

{% asset_img 16317985375578.jpg %}

## 初识面向对象

### 定义类

在 Java 中，定义**类**的统一格式如下：

```java
[修饰符] class 类名 {
    // ...
}
```

其中，**修饰符**（**可省略**）中的**访问权限**只能为`public`（**公开类**），其他**修饰符**只能为`final`或`abstract`(**抽象类**)。

**类名**则为**合法的标识符**，一般采用**大驼峰命名法**来表示。（详见 [驼峰命名法](https://en.wikipedia.org/wiki/Camel_case) ）

### 成员变量

在 Java 中，定义**成员变量**的统一格式如下：

```java
[修饰符] 类型 成员变量名 [= 初始值];
```

其中，**修饰符**（**可省略**）中的**访问权限**可以为`public`|`protected`|`private`。其他**修饰符**可以为`final`、`static`。

**类型**可以为任意的**基本类型**或**引用类型**。

**成员变量名**同样为**合法的标识符**，一般采用**小驼峰命名法**来表示。**成员变量名**通常为**名词**（如**身高**、**体重**）。

**初始值**可以省略，如不显式指定初始值则为该类型的默认值（数值型为`0`，布尔型为`False`，引用类型为`null`）。

### 方法

在 Java 中，**方法**必须定义在**类**中，不能单独存在。定义**方法**的统一格式如下：

```java
[修饰符] 返回值类型 方法名( [形参列表] ) {
    // ...
    // 如果声明了返回值类型，必须有 return 语句
}
```

其中，**修饰符**（**可省略**）中的**访问权限**可以为`public`|`protected`|`private`。其他**修饰符**可以为`final`|`abstract`、`static`。

**返回值类型**可以为任意的**基本类型**或**引用类型**，也可以为`void`（无返回值）。

**方法名**为**合法的标识符**，一般采用**小驼峰命名法**来表示。**方法名**通常为**动词**（如**走**、**跑**）。

### 构造器

**构造器**的作用是在`new`一个对象时自动执行的方法。如果没有为类创建构造器，Java 会**自动**创建一个**无参构造器**。

在 Java 中，定义**构造器**的统一格式如下：

```java
[修饰符] 类名( [形参列表] ) {
    // ...
}
```

**注意：构造器名只能与类名相同，且不能写返回值类型**

其中，**修饰符**（**可省略**）只能为`public`|`protected`|`private`。

## 关键字

### 访问控制

Java 面向对象中访问权限有 3 个（从小到大排序）：

- `private`：**类访问权限**，只能在该类中被访问（彻底隐藏）。
- **默认**(不写)：**包访问权限**，只能在该类和该类所在的包中被访问（部分隐藏）。
- `protected`：**子类访问权限**，只能在该类、该类所在的包及该类的子类中被访问（部分暴露）。
- `public`：**公共访问权限**，该类可以在任意地方来访问（彻底暴露）。

|        | `private` | 默认 | `protected` | `public` |
| :----: | :-------: | :--: | :---------: | :------: |
| 当前类 |    ✅     |  ✅  |     ✅      |    ✅    |
| 当前包 |    ❌     |  ✅  |     ✅      |    ✅    |
|  子类  |    ❌     |  ❌  |     ✅      |    ✅    |
|  任意  |    ❌     |  ❌  |     ❌      |    ✅    |

### static

有`static`的成员属于**类成员**，无`static`的成员属于**实例成员**。`static`只能修饰**成员变量**、**方法**、**初始化块**、**内部类**。

使用`static`修饰的成员，**通常**使用`类名.成员名`访问。

注意：

- Java 允许通过实例对象来访问`static`成员，但并**不推荐**这么做。
- **非`static`成员可以访问`static`成员，相反，`static`成员不能调用非`static`成员。**

### this

#### this 引用

`this`可以出现在非`static`的**方法**、**构造器**中。用于代表当前正在使用的对象（谁调用他就代表谁）。

例如：

```java
public class Flower {
  String color;
  public Flower() {
    this.color = "yellow"; // 创建对象时将颜色设置为 黄色
  }
  public void output() {
    System.out.println("已修改");
  }
  public void change() {
    this.color = "red";    // 将当前对象的颜色修改为 红色
    this.output();         // 调用当前对象中的 output 方法
  }
}
```

#### this 调用

可以通过`this(参数)`来调用该类的对应构造器，具体可见下方的**构造器重载**。

### super

#### super 限定

与**this 引用**类似，`super`用于限定访问父类的**实例变量**、**实例方法**。

```java
class Base {
  int foo = 20;
  public void bar() {
    System.out.println("Base中的foo方法");
  }
}
class Sub extends Base {
  int foo = 200;
  @Override
  public void bar() {
    System.out.println("Sub中的foo重写方法");
  }
  public void test() {
    System.out.println(foo);       // 200 (Sub类)
    System.out.println(this.foo);  // 200 (Sub类)
    System.out.println(super.foo); // 20 (Base类)

    bar();        // Sub中的foo重写方法 (Sub类)
    this.bar();   // Sub中的foo重写方法 (Sub类)
    super.bar();  // Base中的foo方法 (Base类)
  }
}
```

#### 调用父类构造器

与**this 调用**类似，用于调用父类构造器。

子类构造器**一定**要调用父类构造器**一次**。如果**子类构造器**没有显式调用**父类构造器**，系统将在**子类构造器**开头**自动调用**父类**无参构造**。

```java
class Fruit {
  private double weight;
  public Fruit(double weight) {
    this.weight = weight;
  }
}
class Apple extends Fruit {
  private String name;
  public Apple(double weight, String name) {
    super(weight);
    this.name = name;
  }
}
```

### final

`final`可以修饰**变量**（**成员变量**、**局部变量**）、**方法**、**类**。与`abstract`互斥。

#### `final`修饰变量

当`final`修饰**变量**时，必须为该变量赋初始值，且**无法重新赋值**（对象可以进行修改）。

- 当`final`修饰**实例变量**时，必须显式指定初始值，且只能在**定义时**、**实例初始化块**、**各构造器**其中的一个位置指定。
- 当`final`修饰**类变量**时，必须显式指定初始值，且只能在**定义时**、**类初始化块**其中的一个位置指定。

#### `final`的宏替换

当变量满足以下条件时，该变量出现的所有地方将会被替换成变量的值：

- 变量有`final`修饰
- 声明时指定了初始值
- 变量初始值可在编译时确定

{% asset_img 16323961305864.jpg %}

#### `final`修饰方法

`final`修饰方法指不允许被子类**重写**，避免该方法被子类破坏。

#### `final`修饰类

`final`修饰类以后该类**不允许**派生子类。

### abstract

`abstract`只能修饰**类**和**方法**，且与`final`互斥。

#### 抽象类

**抽象类**指使用`abstract`修饰的类，主要作用是**派生子类**。

**抽象类**有以下特性：

- 抽象类**可以有**抽象方法。
- 抽象类**无法**创建对象。

```java
public abstract class Test {}
```

#### 抽象方法

**抽象方法**指**只有方法签名，无方法体**的方法。**抽象方法必须被子类重写，否则不能被调用。**

```java
public abstract void test() // 不能有方法体
```

## 面向对象三大特征

### 封装

封装包含两方面含义：

- **隐藏**：将内部实现细节隐藏
- **暴露**：通过暴露的接口来操作对象。

封装的要求：**合理隐藏，合理暴露。**

封装主要是通过**访问控制修饰符**来实现

在 Java 中，**实例变量**通常使用`private`来修饰，将其隐藏。并提供相应的`getter`、`setter`方法，来控制该成员变量的访问。

如下代码所示，`User`类中有一个成员变量（`name`），要求`name`的长度在 10 位以内。

```java
class User {
  private String name;
  public void setName(String name){
    if (name.length > 10) {
      System.out.println("名称长度必须在10位以内！");
      return;
    }
    this.name = name;
  }
  public String getName() {
    return this.name;
  }
}
```

### 继承

继承最大好处是**代码复用**。

Java 中继承是**类与类**之间的关系（而非对象与对象之间的关系），是一种**由一般到特殊**的关系（如**苹果类**(**子类**、**派生类**)继承了**水果类**(**父类**、**超类**、**基类**)），**子类的实例可以当作父类的实例来使用**。

在 Java 中，**继承**通过如下语法定义：

```java
[修饰符] class 子类名 extends 父类 {
    // ...
}
```

**注意**：

- Java 是单继承父类，只能有 **1 个直接继承的父类**。
- 如果不显式继承父类，Java 默认继承`Object`类。

子类可以调用父类非`private`修饰的**成员变量**、**方法**（见上方**访问控制**表格）。

### 多态

**多态**是指同一个类型的多个实例，在执行同一个方法时，呈现出多种行为特征。

#### 变量的类型

**编译时类型**：声明该变量时指定的类型。在 Java 程序编译阶段，Java 编译器只认**编译时类型**。当调用子类有而父类没有的方法，且使用**向上转型**时，编译器将报错。

**运行时类型**：该变量实际所引用的类型。

#### 向上转型

子类的对象可以直接赋值给父类变量，其可以自动完成。

例如，**Ostrich 类**继承了**Bird 类**，那么定义**Ostrich**实例时可以进行如下定义：

```java
class Bird {
  public void fly() {
    System.out.println("飞咯~");
  }
}
class Ostrich extends Bird {
  @Override
  public void fly() {
    System.out.println("不会飞呀~");
  }
}
public class Test {
  public static void main(String[] args){
    Bird b1 = new Bird();
    Bird b2 = new Ostrich();

    b1.fly();  // 飞咯~
    b2.fly();  // 不会飞呀~
  }
}
```

#### 向下转型 (强制转换)

当使用**向上转型**特性时，想要调用子类方法时，需要强制转换成对应类型。

```java
class Bird {
  public void fly() {
    System.out.println("飞咯~");
  }
}
class Ostrich extends Bird {
  public void run() {
    System.out.println("跑得快呢");
  }
}
public class Test {
  public static void main(String[] args){
    Bird b1 = new Ostrich();

    // b1.run(); // 无法编译

    Ostrich b2 = (Ostrich) b1;
    b2.run(); // 正常编译
  }
}
```

**注意**：

- 强转运算符只能在编译类型具有继承关系的变量之间进行强转，否则编译将会报错（如`String`类型强转成`Integer`）。
- 如果在编译类型具有继承关系的变量之间转换时，如果被转变量的实际类型不是要转换的目标类型，程序就会引发`ClassCastException`异常。

#### instanceof

为了避免`ClassCastException`异常，Java 提供了`instanceof`运算符。格式是`变量名 instanceof 类型`，当变量所引用的对象是后面类或子类的实例时，返回`true`。

**instanceof 只能在具有继承关系的变量之间进行强转，否则编译将会报错，故当变量与类之间没有关系时，也不会返回`false`。**

例如：

```java
class Fruit {}
class Apple {}
public class Test {
  public static void main(String[] args){
    Fruit fruit = new Apple();
    if(fruit instanceof Apple) {
      Apple apple = (Apple)fruit;
    }
  }
}
```

从 Java 16 开始，instanceof 运算符得到了升级。见本文最后**Java 16 增强的 instanceof**。

## 面向对象重点

### 方法重载

**方法重载**(`Overload`)指**方法名相同，形参列表不同的方法**。Java 通过参数类型来判断该方法是否为重载方法。**修饰符不同或返回值类型不同的方法不能称为方法重载！**

例如：

```java
public void show() {
    System.out.println("哦吼？");
}
public void show(String name) {
    System.out.println("商品名："+ name);
}
public void show(String name, double price) {
    System.out.println("商品名：" + name + ", 价格：" + price);
}
public static void main(String[] args) {
    show();            // 哦吼？
    show("手机");       // 商品名：手机
    show("平板", 3000); // 商品名：平板, 价格：3000
}
```

### 构造器重载

**构造器重载**要求**形参列表不同**。

例如：

```java
class Dog{
  private String name;
  private int age;
  public Dog(){
    // 无参构造
  }
  public Dog(String name){
    this.name = name;
  }
  public Dog(String name, int age){
    this.name = name;
    this.age = age;
  }
}
```

这里有个问题，就是当需要为某个成员统一修改时，可能需要一一修改构造器。例如，需要在`name`成员前添加`Dog:`的前缀，需要一一修改构造器。

这里可以通过`this(参数)`来调用对应的构造方法。

```java
class Dog{
  private String name;
  private int age;
  public Dog(){
    // 无参构造
  }
  public Dog(String name){
    this.name = "Dog: " + name;
  }
  public Dog(String name, int age){
    this(name);  // 调用 `public Dog(String)` 构造器
    this.age = age;
  }
}
```

### 方法重写

**方法重写**(`Override`)是指**子类**将**父类**的方法重写。**方法重写**要求**方法名、形参列表相同，返回值类型、声明抛出的异常相同或更小(即子类)，访问权限相同或更大**。

**重写的方法**通常使用`@Override`注解来修饰（**避免重写错代码**）。

例如：

```java
class Bird {
  public void fly() {
    System.out.println("鸟飞咯");
  }
}
class Ostrich extends Bird {
  @Override
  public void fly() {
    System.out.println("鸵鸟不会飞……");
  }
}
```

### toString 与 equals 方法

`toString`方法是将当前对象以**文本的方式**来表示出来，Java 默认的`toString`方法是`类名@哈希码`的格式，通常我们重写该方法将其内部的成员变量表示出来。

`equals`方法则是用于比较两个对象是否相同，Java 默认通过比较两个引用变量是否指向同一个对象，通常我们重写该方法使用**该类的关键属性**来比较。

```java
class Person {
  private String name;
  private int age;
  // 有参构造
  public Person(String name, int age) {
    this.name = name;
    this.age = age;
  }
  // Getter / Setter 方法
  public void setName(String name) {
    this.name = name;
  }
  public void setAge(int age) {
    this.age = age;
  }
  public String getName() {
    return this.name;
  }
  public int getAge() {
    return this.age;
  }
  // toString 方法
  @Override
  public String toString() {
    return "Person[name=" + name
         + ", age=" + age
         + "]";
  }
  // equals 方法
  @Override
  public boolean equals(Object obj) {
    if (this == obj) return true;  // 同一个对象
    if (obj != null && obj.getClass() == Person.class) {
      // obj不为null且obj和当前对象的类相同
      Person target = (Person) obj;
      return this.name.equals(target.getName())
             // String类型需要使用equals方法比较
          && this.age == target.getAge();
    }
    return false;
  }
}

public class PersonTest {
  public static void main(String[] args) {
    Person p1 = new Person("王强", 18);
    Person p2 = new Person("王强", 18);
    Person p3 = new Person("张三", 30);

    System.out.println(p1);     // Person[name=王强, age=18]
    System.out.println(p2);     // Person[name=王强, age=18]
    System.out.println(p3.toString()); // Person[name=张三, age=30]

    if (p1.equals(p2))          // true
      System.out.println("p1和p2是同一个人");
  }
}
```

### 初始化块

**初始化块**的语法如下：

```java
[修饰符] {
  // ...
}
```

其中**修饰符**只能出现`static`，无`static`修饰的称为**实例初始化块**，有`static`修饰的称为**类初始化块**。

#### 实例初始化块

**实例初始化块**实际上是「**假象**」，块中所有代码在**编译**时将会被**还原到每个构造器的最前面**。左图为编译前的原始代码，右图为`class`文件反编译的代码。

{% asset_img 16322017907275.jpg %}

**实例初始化块**的作用是**将各个构造器前相同的代码抽离到实例初始化块，从而实现代码复用**。

#### 类初始化块

**类初始化块**负责对类进行初始化。当程序**第一次主动使用**(除了**仅使用该类声明变量**)该类时，系统会为该类分配内存空间，并调用类初始化块。程序运行时，该类初始化块只执行一次。

|              | 执行次数 | 执行先后 |        执行时间        |
| :----------: | :------: | :------: | :--------------------: |
|  类初始化块  |   1 次   |    先    | 第一次**主动**使用该类 |
| 实例初始化块 |   N 次   |    后    |     每次调用构造器     |

### 抽象类

见上面`abstract`关键字

### 接口

**接口**相当于一个彻底抽象的类，体现**一种规范**。接口中所有东西都使用`public`修饰（通常省略）。接口支持多继承。

#### 接口定义

接口的定义如下：

```java
[修饰符] interface 接口名 [extends 父接口1, 父接口2, ...] {
  // 成员变量（常量，自动使用`public static final`修饰）
  // 抽象方法：Java 8 后支持类方法、默认方法（带有方法体的抽象方法，与实例方法类似）。
}
```

其中，**修饰符**只能为`public`。**接口名**命名规范基本与类名系统，通常使用形容词来定义。

```java
public interface MyInterface {
  // 反编译后：
  // public static final int MAX_WEIGHT = 100;
  int MAX_WEIGHT = 100;

  void test();  // 抽象方法

  // Java 8 后的类方法
  static void staticMethod() {
    // ...
  }

  // Java 8 后的默认方法
  default void defaultMethod() {
    // ...
  }
}
```

#### 使用接口

使用接口中**成员变量**、**类方法**时，与调用类成员相似，即`接口名.成员名`。

例如：

```java
public class InterfaceTest {
  public static void main(String[] args) {
    System.out.println(MyInterface.MAX_WEIGHT); // 100
    MyInterface.staticMethod();
  }
}
```

#### 实现接口

**子类要么重写接口中所有抽象方法，要么定义为抽象类。**

实现接口的格式如下：

```java
[修饰符] class 类名 implements 父接口1 [, 父接口2, ...] {
  // 5大成员
}
```

以实现上方的接口为例：

```java
public class Test implements MyInterface {
  @Override
  public void test() {
    // ...
  }
}
```

**`private`方法本质是实例方法。**

### 内部类

**内部类**是在类体中定义的类。

```java
class 外部类 {
  [修饰符] class 内部类 [extends 父类] [implements 接口] {
    // ...
  }
}
```

**内部类**与**外部类**的区别如下：

- **内部类**与**外部类**相比可使用`static`、`private`、`protected`修饰符。
- 非静态内部类**不能**拥有静态成员（**常量除外**）。
- 内部类可以直接访问外部类私有成员，但静态内部类不能访问外部类的非静态成员。

**内部类的意义**：当某个类的实例必须依附于另一个类存在时，可使用内部类。且内部类可以提供更好的封装（可使用`private`修饰）。

内部类生成的文件名格式为：`外部类$内部类.class`

#### 内部类区分同名变量

```java
class Foo {
  int length = 20;
  class Bar {
    int length = 200;
    void foo() {
      int length = 2000;

      System.out.println(length);            // 2000
      System.out.println(this.length);       // 200
      System.out.println(Foo.this.length);   // 20
    }
  }
}
```

#### 使用内部类

**（1）在外部类中使用内部类**

基本与使用其他类相同，需要注意的是**静态成员不能使用非静态内部类创建实例**。

**（2）在外部类的外面使用静态内部类**

**该内部类不能使用`private`修饰**

```java
class Foo {
  public static class Bar {
    public static void test() {
      System.out.println("我来自Foo.Bar.test()");
    }
  }
}
public class Test {
  public static void main(String[] args) {
    Foo.Bar.test();  // 我来自Foo.Bar.test()
  }
}
```

**（3）在外部类的外面使用非静态内部类 (不常见)**

```java
class Foo {
  public class Bar {
    public void test() {
      System.out.println("非静态内部类");
    }
  }
}
public class Test{
  public static void main(String[] args) {
    Foo foo = new Foo();
    Foo.Bar fb = foo.new Bar();

    fb.test(); // 非静态内部类
  }
}
```

#### 局部内部类

定义在方法中的内部类，不常用，略。

#### 匿名内部类

**匿名内部类**指没有名字的类，无法复用。

匿名内部类的语法如下：

```java
new 父类构造器(参数)|接口() {
  // 除了构造器，其他都可以定义
  // 但一般只实现抽象方法
}
```

注意：

- 匿名内部类必须显式继承父类，或实现一个接口。
- 匿名内部类不能是抽象类，因此必须实现抽象父类或接口中的所有抽象方法。

例如：

```java
abstract class Foo {
  public abstract void test();
}
public class Bar {
  public static void main(String[] args) {
    Foo foo = new Foo() {
      @Override
      public void test() {
        System.out.println("匿名内部类");
      }
    };
    foo.test();  // 匿名内部类
  }
}
```

### 枚举

**枚举**的定义格式如下：

```java
[修饰符] enum 枚举名 {
  // 第一行列出所有实例
  // 可以定义 5 大成员
}
```

**修饰符**只能为`public`。

枚举类与普通类的区别：

- **枚举**默认已经继承`Enum`类，无法继承其他类。
- **枚举**要么是`final`类，要么是`abstract`类。且 Java 会自动判断该类为`final`类还是`abstract`类。
- **枚举**要求在开头列出所有实例

**枚举类**默认拥有以下方法：

- `static Weekday[] values()`: 返回所有枚举实例
- `static Weekday valueOf(String)`：根据枚举名返回枚举实例
- `String name()`：返回枚举实例的名称
- `int ordinal()`：返回枚举实例的序号

例如：

```java
enum Weekday {
    SUN, MON, TUE, WED, THU, FRI, SAT; // 所有实例

    Weekday() {
        System.out.println("我来自构造器");
    }

    public void foo() {
        System.out.println("我来自枚举中的foo方法");
    }
}

public class EnumTest {
    public static void main(String[] args) {
        System.out.println(Weekday.WED);    // WED
        System.out.println(Arrays.toString(Weekday.values())); // [SUN, MON, TUE, WED, THU, FRI, SAT]

        Weekday d1 = Weekday.SUN;
        System.out.println(d1.ordinal());   // 0
        System.out.println(d1.name());      // SUN
        d1.foo();  // 我来自枚举中的foo方法

        Weekday d2 = Weekday.valueOf("TUE");
    }
}
```

#### 枚举与`switch`

`switch`语句可以与枚举共同使用：

```java
enum Weekday {
    SUN, MON, TUE, WED, THU, FRI, SAT;

    public void info() {
        switch (this) {
            case MON:
            case TUE:
            case WED:
            case THU:
            case FRI:
                System.out.println("上班哦");
                break;
            case SAT:
            case SUN:
                System.out.println("放假哦");
                break;
        }
    }
}

public class EnumTest {
    public static void main(String[] args) {
        Weekday day = Weekday.SUN;
        day.info(); // 放假哦
    }
}
```

#### 枚举类与构造器

**枚举**定义后本质为`public static final`的常量：

```java
// 编译前：
public enum Weekday {
  SUN, MON, TUE, WED, THU, FRI, SAT;
}

// 编译后
public final class Weekday extends Enum {
  public static final Weekday SUN = new Weekday();
  public static final Weekday MON = new Weekday();
  public static final Weekday TUE = new Weekday();
  public static final Weekday WED = new Weekday();
  public static final Weekday THU = new Weekday();
  public static final Weekday FRI = new Weekday();
  public static final Weekday SAT = new Weekday();

  private Weekday() {}
}
```

当然，我们可以自己手动编写构造器，其使用方式与正常类相似：

```java
enum Weekday {
  SUN(false),
  MON(true),
  TUE(true),
  WED(true),
  THU(true),
  FRI(true),
  SAT(false);

  private final boolean isWorkday;

  Weekday(boolean isWorkday) {  // private 构造器
    this.isWorkday = isWorkday;
  }
}
```

## N More Things

### 记录类

**记录类**(**Record**)是从 Java 16 正式引入的类型( [JEP 395](https://openjdk.java.net/jeps/395) )。记录类会自动地为其添加**有参构造**、**Getter**、`toString`、`equals`和`hashCode`方法。

在 Java 16 之前，定义一个纯数据类可能需要如下代码：

```java
class Point {
  private final int x;
  private final int y;

  Point(int x, int y) {
    this.x = x;
    this.y = y;
  }

  int x() { return x; }
  int y() { return y; }

  public boolean equals(Object o) {
    if (!(o instanceof Point)) return false;
    Point other = (Point) o;
    return other.x == x && other.y == y;
  }

  public int hashCode() {
    return Objects.hash(x, y);
  }

  public String toString() {
    return String.format("Point[x=%d, y=%d]", x, y);
  }
}
```

而引入`Record`类以后，该类可以简化为如下代码：

```java
record Point(int x, int y) {}
```

当然，`Record`类能做的事不止这些。具体可以阅读 [JEP 395](https://openjdk.java.net/jeps/395) 。

### 形参个数可变方法

在 Java 中，方法可以有**可变长**参数。该参数位于某一方法的最后一位。

例如，如下定义了一个**形参个数可变方法**：

```java
public void test(String... sites){
  // ...
}
```

该方法中，定义了一个`String`类型的可变长参数。可变长参数本质上是一个**数组**。**可变长参数只能位于形参列表的最后一位！**

该方法可以通过如下方式调用：

```java
test(new String[]{"GitHub", "Google", "Bing"}) // 方法 1
test("GitHub", "Google", "Bing")  // 方法2
```

**使用`Type...`和`Type[]`的区别：前者可以通过两种方法调用，后者只能由方法 1 调用**

### Java 8 函数式编程

见 [Java 函数式编程知识整理](/archives/java-functional-program) 。

### Java 9 接口的 private 方法

Java 8 中`default`方法本质是**实例方法**。在 Java 9 之前定义默认方法时，如果某些方法有公共部分，需要多次编写相同的代码。Java 9 以后，可以将重复的代码抽离出来，独立成`private`方法，同时实现隐藏。

例如：

```java
public interface PrivateMethod {
  default void foo() {
    System.out.println("foo");
    common();
  }
  default void bar() {
    System.out.println("bar");
    common();
  }
  // 工具方法只被本类默认方法使用，并不希望暴露出去
  private void common() {
    for(var i = 0; i < 10; i++) {
      System.out.println("公共部分");
    }
  }
}
```

### Java 16 增强的 instanceof

在 [JEP 394](https://openjdk.java.net/jeps/394)中，`instanceof`运算符得到了升级。

从 Java 16 开始，可以通过`变量名 instanceof 类名 新变量名`判断该变量是否属于某个类的实例。如果属于，Java 将自动将其强制转换，并赋值到新的变量中。

```java
Object obj = "test";

// Java 16 之前
if (obj instanceof String) {
    String s = (String) obj;
    // ...
}

// Java 16 及以后
if (obj instanceof String s) {
    // ...
}
```

当然，Java 16 增强的 instanceof 功能远远不止这些。具体阅读 [JEP 394](https://openjdk.java.net/jeps/394) 。

## 参考资料

- [《疯狂 Java 讲义 · 第 5 版》](https://union-click.jd.com/jdc?e=&p=JF8BAMUJK1olXDYCV1pdAUoUB19MRANLAjZbERscSkAJHTdNTwcKBlMdBgABFksUB28BGlgRQl9HCANtdUpkA2twQgV1PE59KjxDcCNISg1pXVcZbQcyVF9cC04VBWsBHGslXQEyAjBdCUoWAm4NG14WbQcyVFlfC0oTAmYNGVoTWTYFVFdtUx55dQRLWCBQCXlcMgM9OHsnAF84K1slXjZAOlhYARtHBTtaHgsRXwNXA1cNC0hHBTwJGFkSDVJRB1ddOEkWAmsBKw)
- [跟着李刚老师学 Java（视频）](https://bfw.h5.xeknow.com/s/1YClVz)
