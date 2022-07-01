---
title: Java 多线程——线程安全
date: 2022-06-30 13:12:14
categories:
- [编程语言, Java]
tags:
- Java
- 多线程
---
本文主要介绍 Java 多线程安全问题的内容。

<!-- more -->

## 线程安全问题引入

银行取钱问题：假设允许在同一时间多个人从统一账户上取钱。

正如在 [上一篇](mweblib://16325470651261) 中所讲：

> 多个任务在单个 CPU 上 **快速轮换** 执行，任意时刻，CPU 只能执行其中一个任务。但由于 CPU 会 **快速轮换** 地执行多个任务，因此用户感觉多个任务在同时执行 —— 用户的假象。

CPU 在某一时刻只能执行一个任务，多个任务之间快速切换。那么就可能出现一种情况：

A、B 同时去银行取 800 元，银行卡上的余额为 1,000 元。

1. 两人同时进入银行取钱
2. 系统判断要取的钱都是够的
3. CPU 处理 B 的请求：吐 800 块钱、扣余额，完成
4. CPU 继续处理 A 的请求。因为已经完成了余额的判断，所以直接进行吐钱、扣余额。

到这里，整个流程就完成了。但是有问题：

- 吐了 1,600 块钱
- 余额剩下 -600 元了

这便是一个典型的线程安全问题。

对应出来的代码可以如下：

```java
public class ConcurrentSafety {
  public static void main(String[] args) {
    var account = new Account(1000);
    new MyThread(account, 800).start();
    new MyThread(account, 800).start();
  }
}

class MyThread extends Thread {
  private final Account account;
  private final int amount;

  public MyThread(Account account, int amount) {
    this.account = account;
    this.amount = amount;
  }

  @Override
  public void run() {
    if (account.getBalance() >= amount) {
      System.out.printf("[%s] Withdraw %d\n", Thread.currentThread(), amount);
      account.withdraw(amount);
      System.out.printf("[%s] Balance is now %d\n", Thread.currentThread(), account.getBalance());
    } else {
      System.out.printf("[%s] Not enough money\n", Thread.currentThread());
    }
  }
}

class Account {
  private int balance;

  public Account(int balance) {
    this.balance = balance;
  }

  public int getBalance() {
    return balance;
  }

  public void withdraw(int amount) {
    balance -= amount;
  }
}
```

输出：

```text
[Thread[Thread-0,5,main]] Withdraw 800
[Thread[Thread-0,5,main]] Balance is now 200
[Thread[Thread-1,5,main]] Withdraw 800
[Thread[Thread-1,5,main]] Balance is now -600
```

## 同步代码块

同步代码块常常用于维护数据的一致性。其机制是给共享资源上锁，只有拿到锁的线程才能够访问共享资源。该锁是隐式的，不需要我们进行维护。同步代码块的处理是由 JVM 进行完成。

同步代码块的定义如下：

```java
synchronized (同步监视器) {
  // ...
}
```

其中，同步监视器需要设置为 **多个线程之间相互争抢的资源**，在如上的例子中即为 `account`。

将线程的 `run` 方法改为如下：

```java
@Override
public void run() {
  synchronized (account) {
    if (account.getBalance() >= amount) {
      System.out.printf("[%s] Withdraw %d\n", Thread.currentThread(), amount);
      account.withdraw(amount);
      System.out.printf("[%s] Balance is now %d\n", Thread.currentThread(), account.getBalance());
    } else {
      System.out.printf("[%s] Not enough money\n", Thread.currentThread());
    }
  }
}
```

此时结果永远是：

```text
[Thread[Thread-0,5,main]] Withdraw 800
[Thread[Thread-0,5,main]] Balance is now 200
[Thread[Thread-1,5,main]] Not enough money
```

注意：无论在同步代码块中执行什么语句，都必须等到语句块结束才会将锁释放。

## 同步方法

同步方法是使用 `synchronized` 修饰的方法，整个该方法都是同步代码。

如果该方法是实例方法，那么同步监视器是当前对象。如果是类方法，同步监视器则为类本身。

同步方法与同步代码块的区别：同步代码块需要显式指定同步监视器，同步方法不需要。

仍然以取钱例子为例，因为同步方法的同步监视器是该类实例或者类本身，我们可以将取钱的业务逻辑直接修改到类中。

故代码可以改为如下：

```java
public class ConcurrentSafety {
  public static void main(String[] args) {
    var account = new Account(1000);
    new MyThread(account, 800).start();
    new MyThread(account, 800).start();
  }
}

class MyThread extends Thread {
  private final Account account;
  private final int amount;

  public MyThread(Account account, int amount) {
    this.account = account;
    this.amount = amount;
  }

  @Override
  public void run() {
    account.withdraw(amount);
  }
}

class Account {
  private int balance;

  public Account(int balance) {
    this.balance = balance;
  }

  public synchronized void withdraw(int amount) {
    if (balance >= amount) {
      System.out.printf("[%s] Withdraw %d\n", Thread.currentThread(), amount);
      balance -= amount;
      System.out.printf("[%s] Balance is now %d\n", Thread.currentThread(), balance);
    } else {
      System.out.printf("[%s] Not enough money\n", Thread.currentThread());
    }
  }
}
```

执行后的结果与同步代码块相似：

```text
[Thread[Thread-0,5,main]] Withdraw 800
[Thread[Thread-0,5,main]] Balance is now 200
[Thread[Thread-1,5,main]] Not enough money
```

## 使用 Lock

同步代码块、同步方法都是由 JDK 来自动管理锁。当然，我们也可以自己使用 Lock 来管理锁。

Java 在 `java.util.concurrent.locks` 包下有个 `Lock` 接口，主要有 3 个实现类：`ReentrantLock`、`ReentrantReadWriteLock.ReadLock`、`ReentrantReadWriteLock.WriteLock`。在这里我们以 `ReentrantLock` 作为演示。

在 `Account` 类中，我们可以添加一个 Lock 的成员变量，作为锁。在进行取钱操作之前，我们首先对其进行锁定。操作完成后，即可对锁进行释放。注意，为保证锁一定被释放，可以将解锁的语句放在 `try` 的 `finally` 块中。

```java
class Account {
  private int balance;
  private Lock lock = new ReentrantLock();

  public Account(int balance) {
    this.balance = balance;
  }

  public void withdraw(int amount) {
    lock.lock();
    try {
      if (balance >= amount) {
        System.out.printf("[%s] Withdraw %d\n", Thread.currentThread(), amount);
        balance -= amount;
        System.out.printf("[%s] Balance is now %d\n", Thread.currentThread(), balance);
      } else {
        System.out.printf("[%s] Not enough money\n", Thread.currentThread());
      }
    } finally {
      // 确保永远释放锁
      lock.unlock();
    }
  }
}
```

执行结果与之前完全一致。
