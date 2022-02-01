---
title: 菜狗学数据结构——数组和链表
date: 2021/08/28 10:42:37
categories:
- [数据结构与算法, 算法知识]
tags:
- 数据结构
---
数据结构的存储方式只有两种：**数组**和**链表**，这两个是其他数据结构实现的基础。

<!-- more -->

在编写程序的过程中，我们常常需要「找到」一个位置来存放「中间数据」。此时，我们常常定义**变量**来存储他们。当创建变量时，计算机会为其创建一个单独的「空间」来存放特定类型的数据。

如下所示，我们创建了一个`score`变量来存放一位同学的成绩。

```java
var score = 80;
```

计算机会在内存中单独开辟一片空间来存放数据，并且告诉程序相应的内存地址。如图所示，该变量的内存地址是`0x00000005`。

{% asset_img 变量内存.png %}

当我们需要存储多个相同类型的数据时，似乎使用变量就显得不太「靠谱」了

```java
var score1 = 80;
var score2 = 90;
var score3 = 59;
var score4 = 66;
var score5 = 11;
var score6 = 99;
var score7 = 55;
var score8 = 73;
```

如果有 200 个学生，难不成定义 200 个变量来存储学生成绩？这时可以使用**数组**和**链表**来存储。

## 数组

使用数组时，计算机会在内存中开辟一整段连续的空间用于存放数据。依然以学生成绩为例。

```java
var scores = new int[]{80, 90, 59, 66, 11, 99, 55, 73};
```

{% asset_img 数组内存.png %}

如图所示，计算机为学生成绩分别开辟了 8 份空间用来分别存放 8 位学生的考试成绩。然而这里又出现了一个问题，如果想要添加第 9 位学生成绩时会怎么样？

答案就是，计算机会重新在内存中找一份空间用于存放这 9 位学生成绩。这也是为什么数组一旦创建就不可变。

### 数组的操作

在数组中，针对一个元素的位置有一个专业术语称为**索引**（又称**下标**）。我们通常通过**索引**（**下标**）来获取、修改数组元素

{% asset_img 数组索引.png %}

数组的**索引**由 0 开始，最大值为`数组元素总数 - 1`。

#### 数组元素数据的获取

数组元素数据通过`数组名[索引]`来获取。如以下代码展示了如何遍历一个数组。

```java
var scores = new int[]{80, 90, 59, 66, 11, 99, 55, 73};
for(var i = 0; i < scores.length; i++){
    System.out.println(scores[i]);
}
```

#### 数组元素数据的修改

数组元素数据可以通过`数组名[索引] = 新数据`来修改。如以下代码展示了将`scores`数组中第 4 号元素（`11`分）修改为`81`分。

```java
var scores = new int[]{80, 90, 59, 66, 11, 99, 55, 73};
scores[4] = 81;
```

#### 数组元素的插入

如果需要在数组之间的某个位置插入一个元素，则需要将其后面的元素整体向后挪一位。当数组空间不足时，你需要重新创建一个空间来存放新的数组。

{% asset_img 数组元素插入.png %}

#### 数组元素的删除

数组中一个元素删除时，通常使得其右边的元素向左挪一位。

{% asset_img 数组元素删除.png %}

## 链表

与**数组**不同，**链表**中的**元素**可以在任意的内存位置中。

依然以上面的学生成绩为例，其在内存中如图所示。

{% asset_img 链表内存.png %}

一个简易链表的实现如下：

### 链表的操作

在链表中，我们通常将元素称为一个**节点**(**node**)，一个节点保存了其**上下节点**的地址。

通常节点的设计如下：

```java
class Node {
    int score;
    Node prev;
    Node next;

    public Node(int score) {
        this.score = score;
    }
}
```

{% asset_img 一个链表节点.png %}

#### 链表元素数据的获取

在链表中，一个元素数据需要由上一个元素逐步向下寻找。具体代码实现可以参照下面的`get(int index)`方法。

#### 链表元素数据的修改

在链表中，想要修改一个元素的数据首先要找到该元素，然后对其进行修改。具体代码实现可以参照下面的`update(int index, int newData)`方法。

#### 链表元素的插入

在链表中，想要插入一个元素可以将上一个节点的`next`对象以及下一个节点的`prev`对象指向新的元素。具体代码实现可以参照下面的`insert(int index, int data)`方法。

#### 链表元素的删除

在链表中，想要删除一个元素只需要确保没有任何一个元素指向该节点即可。具体代码实现可以参照下面的`remove(int index)`方法。

### 简易链表的实现

```java
public class MyLinkedList {
    /**
     * 头节点指针
     */
    private Node head;
    /**
     * 尾节点指针
     */
    private Node last;
    /**
     * 链表实际长度
     */
    private int size;

    /**
     * 链表插入元素
     *
     * @param data  插入元素
     * @param index 插入位置
     */
    public void insert(int index, int data) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("超出链表节点范围！");
        }
        final var insertedNode = new Node(data);
        insertedNode.prev = last;
        if (size == 0) {
            // 空链表
            head = insertedNode;
            last = insertedNode;
        } else if (index == 0) {
            // 插入头部
            insertedNode.next = head;
            head = insertedNode;
        } else if (size == index) {
            // 插入尾部
            last.next = insertedNode;
            last = insertedNode;
        } else {
            // 插入中间
            final var prevNode = get(index - 1);
            insertedNode.next = prevNode.next;
            prevNode.next = insertedNode;
        }
        size++;
    }

    /**
     * 修改数据元素
     *
     * @param index    修改元素索引
     * @param newData  修改值
     */
    public void update(int index, int newData) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("超出链表节点范围！");
        }
        final var node = get(index);
        node.data = newData;
    }

    /**
     * 链表删除元素
     *
     * @param index 删除位置
     */
    public Node remove(int index) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("超出链表节点范围！");
        }
        Node removedNode = null;
        if (index == 0) {
            // 删除头节点
            removedNode = head;
            head = head.next;
            head.prev = null;
        } else if (index == size - 1) {
            // 删除尾节点
            final var prevNode = get(index - 1);
            removedNode = prevNode.next;
            prevNode.next = null;
            last = prevNode;
        } else {
            // 删除中间节点
            final var prevNode = get(index - 1);
            final var nextNode = prevNode.next.next;
            removedNode = prevNode.next;
            nextNode.prev = prevNode;
            prevNode.next = nextNode;
        }
        size--;
        return removedNode;
    }

    /**
     * 链表查找元素
     *
     * @param index 查找位置
     */
    public Node get(int index) {
        if (index < 0 || index > size) {
            throw new IndexOutOfBoundsException("超出链表节点范围！");
        }
        var temp = this.head;
        for (int i = 0; i < index; i++) {
            temp = temp.next;
        }
        return temp;
    }

    /**
     * 输出链表
     */
    public void output() {
        var temp = this.head;
        while (temp != null) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }

    /**
     * 链表节点
     */
    private static class Node {
        Node prev;
        int data;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }

    public static void main(String[] args) throws Exception {
        final var myLinkedList = new MyLinkedList();
        myLinkedList.insert(0, 3);
        myLinkedList.insert(1, 7);
        myLinkedList.insert(2, 9);
        myLinkedList.insert(3, 5);
        myLinkedList.output();
        System.out.println("--------------");
        myLinkedList.update(3, 8);
        myLinkedList.remove(0);
        myLinkedList.output();
    }
}
```

## 数组和链表的优劣

如下是**数组**和**链表**操作运行所需的时间：

|      | 数组   | 链表   |
| ---- | ------ | ------ |
| 读取 | `O(1)` | `O(n)` |
| 插入 | `O(n)` | `O(1)` |
| 删除 | `O(n)` | `O(1)` |

## 参考资料

- [《算法图解》](https://union-click.jd.com/jdc?e=&p=JF8BAMQJK1olXDYCV15YAUIVAF9MRANLAjZbERscSkAJHTdNTwcKBlMdBgABFksUA2oBElkWQl9HCANtFilwXRpyTAN2AVJ7CUQ8Xi8TS2xbXVcZbQcyVF9cC04VBWsBHGslXQEyAjBdCUoWAm4NH1wSbQcyVFlfCUsTB2cPGl4TWTYFVFdtUx55dQRLWCBQCXlcMgM9OHsnAF84K1slXjZAOlpaARhHU2dfHFkTXgNXBgxVXx4QAjwAG1wSXwBRB1tbOEkWAmsB)
- [《漫画算法：小灰的算法之旅》](https://union-click.jd.com/jdc?e=&p=JF8BAMQJK1olXDYCV1pdCk0TA19MRANLAjZbERscSkAJHTdNTwcKBlMdBgABFksUB28KHV8VQl9HCANtQDt-V2dwXyt2LVZGMQsHDB8UWmlOXVcZbQcyVF9cC04VBWsBHGslXQEyAjBdCUoWAm4NG14WbQcyVFleAE0eB2gLElIRXzYFVFdtUx55dQRLWCBQCXlcMgM9OHsnAF84K1slXjZAOlxbXB5HCzhaGl4SDwMBB15UCx4TC2kMT1lADw9RUVwIOEkWAmsB)
