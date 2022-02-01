---
title: Java 多线程快速入门
date: 2022-01-30 09:57:56
categories:
- [编程语言, Java]
tags:
- Java
- 多线程
---

多线程对于提高程序的并发有着十分重要的影响，本篇侧重于多线程的入门知识。

<!-- more -->

## 几个概念

### 进程

当一个程序运行时，该程序就变成操作系统中的一个**进程**。

进程一般包含以下特征：

- **独立性**：进程时操作系统中独立存在的实体，它可以拥有自己独立的资源。每一个进程都拥有自己私有的地址空间。在没有经过进程本身允许的情况下，一个用户进程不可以直接访问其他进程的地址空间。
- **动态性**：进程与程序的区别在于，程序知识一个静态的指令集合，而进程是一个正在系统中活动的指令集合。在进程中加入了时间的概念。进程具有自己的生命周期和不同的状态，这些概念在程序中都是不具备的。
- **并发性**：多个进程可以在单个处理器上并发执行，多个进程之间不会相互影响。

### 并发（concurrent）

多个任务在单个 CPU 上**快速轮换**执行，任意时刻，CPU 只能执行其中一个任务。但由于 CPU 会**快速轮换**地执行多个任务，因此用户感觉多个任务在同时执行 —— 用户的假象。

### 并行（parallel）

多 CPU 并行，多个任务真正的、同时在多个 CPU 同时执行。任意时刻，多个 CPU 能同时执行多个任务。并行是真正多任务同时执行。

### 线程

线程是进程里的并发执行流，被称为**轻量级进程**。

Java 中的多线程有如下特点：

- 线程不拥有独立的内存资源，只拥有栈、程序计数器，因此创建成本较小。
- 多线程共享进程的内存，因此多线程通信非常容易。

## 创建线程

### 继承 Thread 类

第一种方法是继承`Thread`类。主要有如下步骤：

1. 继承`Thread`类，重写`run()`方法。
2. 创建实例，并调用`start()`方法来启动线程。（**注意不要调用`run()`方法！**）

```Java
class MyThread extends Thread {
  @Override
  public void run() {
    for (int i = 0; i < 1000; i++) {
      System.out.println(
        Thread.currentThread().getName() + "-->" + i
      );
    }
  }
}

public class ThreadTest {
  public static void main(String[] args) {
    new MyThread().start();
      for (int i = 0; i < 1000; i++) {
        System.out.println(
          Thread.currentThread().getName() + "-->" + i
        );
      }
   }
}
```

执行结果如图所示（线程之间交替执行）：

{% asset_img 16362104651004.jpg %}

### 实现 Runnable 接口

第二种方法是实现`Runnable`接口，效果与方法一一致。主要有如下步骤：

1. 实现`Runnable`接口，重写`run()`方法。
2. 创建实例。
3. 以第二步的实例为 target，创建`Thread`对象，调用`start()`方法启动线程。

```Java
class MyThread implements Runnable {
  @Override
  public void run() {
    for (int i = 0; i < 1000; i++) {
      System.out.println(
        Thread.currentThread().getName() + "-->" + i
      );
    }
  }
}

public class ThreadTest {
  public static void main(String[] args) {
    final var t = new MyThread();
    new Thread(t).start();
    for (int i = 0; i < 1000; i++) {
      System.out.println(
        Thread.currentThread().getName() + "-->" + i
      );
    }
  }
}
```

当然，因为`Runnable`接口是一个函数式接口，我们也可以直接使用[匿名内部类](/archives/java-oop#匿名内部类)、[Lambda 表达式](/archives/java-functional-program)创建线程，效果依然与方法一一致。这里以 Lambda 表达式为例：

```Java
public class ThreadTest {
  public static void main(String[] args) {
    new Thread(() -> {
      for (int i = 0; i < 1000; i++) {
        System.out.println(
          Thread.currentThread().getName() + "-->" + i
        );
      }
    }).start();

    for (int i = 0; i < 1000; i++) {
      System.out.println(
        Thread.currentThread().getName() + "-->" + i
      );
    }
  }
}
```

### 实现 Callable 接口

`Callable`接口是`Runnable`接口的增强版，同样是函数式接口，与`Runnable`接口的区别如下：

- `Callable`接口的`call()`方法有返回值；
- `Callable`接口的`call()`方法声明抛出 checked 异常，重写时亦可抛出异常。

第三种实现`Callable`接口创建线程主要有如下步骤：

1. 实现`Callable`接口，并重写`call()`方法；
2. 创建实现类的实例；
3. 将实例包装成`FutureTask`对象
4. 以`FutureTask`实例为 target，创建`Thread`对象，调用`start()`方法启动线程。

另外，可以使用`FutureTask`实例的`get()`方法来获取

```Java
import java.util.concurrent.Callable;
import java.util.concurrent.FutureTask;

class MyThread implements Callable<Integer> {
  int i = 0;

  @Override
  public Integer call() throws Exception {
    for (int j = 0; j < 100; j++) {
      if (j % 2 == 0) {
        System.out.println(Thread.currentThread().getName() + "-->" + j);
        i++;
      }
    }
    return i;
  }
}

public class ThreadTest {
  public static void main(String[] args) throws Exception {
    final var t = new MyThread();
    final var ft = new FutureTask<>(t);
    new Thread(ft).start();

    for (int i = 0; i < 1000; i++) {
      System.out.println(Thread.currentThread().getName() + "-->" + i);
    }
    System.out.println(ft.get()); // 获取返回值
  }
}
```

**注意**：

1. Callable、FutureTask 的泛型必须一致，它们都指定了线程执行体（call 方法）的返回值。
2. 如果程序要获取线程执行体（call 方法）的返回值，可调用`FutureTask`的`get()`方法来获取。**一旦调用 get()方法，程序会要求先把该线程执行完成——线程体（call 方法）完成后才能得到返回值。**

### 三种线程创建方式的对比

三种创建线程（可分为 2 类：一类是继承 Thread，另一类是实现接口）方式的对比：

实现接口主要有如下优势：

1. 实现接口之后，线程体还可以继承其他父类；但如果已经继承 Thread，不能继承其他父类。
2. 实现接口方式创建的线程，可以方便地使用线程池，性能更好。
3. 对于继承 Thread 的方式创建线程类，每个线程都需要创建一个线程类的实例，从而造成数据逻辑与业务逻辑混杂。对于实现接口的方式，多个线程可共用同一个 target，数据逻辑与业务逻辑是分离的。

继承`Thread`创建有下列优势：编程简单，适合初学者。

## 线程的生命周期

线程主要有如下生命周期：

| 生命周期          | 备注                                                                         |
| :---------------- | :--------------------------------------------------------------------------- |
| **新建**(new)     | 创建`Thread`类实例后，线程对象只是一个普通的 Java 对象，并不表现任何动态特征 |
| **就绪**(ready)   | 调用线程对象的`start()`方法，线程处于就绪状态                                |
| **运行**(running) | 得到 CPU，线程开始执行。线程在执行过程中，会一直在**就绪**和**运行**之间切换 |
| **阻塞**(blocked) | 阻塞状态的线程无法继续执行                                                   |
| **死亡**(dead)    | 线程死亡                                                                     |

{% asset_img thread.drawio.png %}

**注意**：在正常开发过程中，**不要**使用`suspend`、`resume`、`stop`控制线程，否则可能引发**死锁**！

## join 线程与线程 sleep

### join

当一条线程执行到某个点，必须等待另外一个线程完成后才能继续向下执行时，应使用`join`来等待线程执行。

```Java
public class JoinThreadTest {
  public static void main(String[] args) throws Exception {
    final var t = new Thread(() -> {
      for (int i = 0; i < 100; i++) {
        System.out.println(Thread.currentThread().getName() + " ---> " + i);
      }
    });
    t.start();

    for (int i = 0; i < 100; i++) {
      System.out.println(Thread.currentThread().getName() + " ---> " + i);
      if (i == 20) {
        // 当 i 为 20 时，等待线程执行
        t.join();
      }
    }
  }
}
```

执行效果如下：

```text
...
main ---> 18
main ---> 19
Thread-0 ---> 12
main ---> 20 // 注意此处
Thread-0 ---> 13
Thread-0 ---> 14
Thread-0 ---> 15
(Thread 执行)...
Thread-0 ---> 97
Thread-0 ---> 98
Thread-0 ---> 99
main ---> 21
main ---> 22
(main 执行)...
main ---> 97
main ---> 98
main ---> 99
```

### sleep

使得**当前运行的线程**暂停、进入阻塞一段时间，`sleep`常常用于控制程序的暂停，十分可靠。

`Thread.sleep(long)`在哪个线程中执行，就让哪个线程暂停。

```Java
public class SleepThreadTest {
  public static void main(String[] args) throws Exception {
    for (int i = 0; i < 100; i++) {
      System.out.println(i);
      if (i == 20) {
        Thread.sleep(5000); // 暂停 5 秒
      }
    }
  }
}
```

执行效果如下：

```text
main ---> 0
main ---> 1
...
main ---> 19
main ---> 20
(暂停 5 秒)
main ---> 21
main ---> 22
...
main ---> 98
main ---> 99
```

## 后台进程

**后台线程**（**Daemon Thread**，又称**守护线程**）主要是为其他线程提供服务。前台线程全部死亡时，那么后台线程会自动死亡。JVM 中 GC 线程是典型的后台线程。

```java
public class DaemonThreadTest {
    public static void main(String[] args) {
        Thread t = new Thread(() -> {
            int i = 0;
            while (true) {
                System.out.println(Thread.currentThread().getName() + " ------> " + ++i);
            }
        });
        t.start();
    }
}
```

以上代码未将线程`t`设为后台线程，运行该程序时，程序将一直运行（无限循环）。

```text
Thread-0 ------> 1
Thread-0 ------> 2
Thread-0 ------> 3
Thread-0 ------> 4
Thread-0 ------> 5
...无限循环
```

主要有两种方式来产生后台线程：

- 后台线程启动的线程默认为后台线程。
- 调用`setDaemon`方法。

    在启动线程（即调用`start`方法）之前调用`setDaemon`方法后，该线程即被设置为守护线程。

    ```java
    public class DaemonThreadTest {
        public static void main(String[] args) {
            Thread t = new Thread(() -> {
                int i = 0;
                while (true) {
                    System.out.println(Thread.currentThread().getName() + " ------> " + ++i);
                }
            });
            t.setDaemon(true);  // 将线程设为后台线程
            t.start();
        }
    }
    ```

    运行该程序，程序无任何输出即停止。（或者看到很少的输出……）

## 线程优先级

如果一个线程的优先级越高，那么该线程可以获得更多的执行机会。

执行`setPriority(int)`方法即可改变该线程的优先级。参数值范围为 1 - 10，但并不是所有操作系统都支持 10 个优先级。通常只使用`MIN_PRIORITY`（1）、`NORM_PRIORITY`（5）、`MAX_PRIORITY`（10）这三个优先级。

## 参考资料

- [《疯狂 Java 讲义 · 第 5 版》](https://union-click.jd.com/jdc?e=&p=JF8BAMUJK1olXDYCV1pdAUoUB19MRANLAjZbERscSkAJHTdNTwcKBlMdBgABFksUB28BGlgRQl9HCANtdUpkA2twQgV1PE59KjxDcCNISg1pXVcZbQcyVF9cC04VBWsBHGslXQEyAjBdCUoWAm4NG14WbQcyVFlfC0oTAmYNGVoTWTYFVFdtUx55dQRLWCBQCXlcMgM9OHsnAF84K1slXjZAOlhYARtHBTtaHgsRXwNXA1cNC0hHBTwJGFkSDVJRB1ddOEkWAmsBKw)
- [跟着李刚老师学 Java（视频）](https://bfw.h5.xeknow.com/s/1YClVz)
