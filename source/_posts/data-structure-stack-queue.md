---
title: 菜狗学数据结构——栈和队列
date: 2021/08/25 10:34:53
categories:
- [数据结构与算法, 算法知识]
tags:
- 数据结构
---
## 栈 (Stack)

**栈**(**Stack**)是一种线性的数据结构，栈中的元素遵循**先入后出**(**FILO**，First In Last Out)的原则。最早进入栈的元素位置称为**栈底**，最后进入站的元素位置成为**栈顶**。

{% asset_img 栈2.png %}

### 操作栈

{% asset_img 栈.png %}

#### 入栈 (push)

**入栈**(**push**)是将一个新的元素放入栈中，新元素的位置称为**栈顶**。

#### 出栈 (pop)

**出栈**(**pop**)是将栈顶的元素从栈中弹出，原栈顶前一个元素位置成为新的**栈顶**。

#### 代码实现

使用**数组**实现栈的代码如下：

```java
import java.util.Arrays;

public class MyArrayStack {
    private int[] arr;
    private int size;

    public MyArrayStack(int length) {
        arr = new int[length];
    }

    /**
     * 入栈
     *
     * @param data 数据
     */
    public void push(int data) {
        if (size >= arr.length) arr = Arrays.copyOf(arr, 2 * arr.length);
        arr[size] = data;
        size++;
    }

    /**
     * 出栈
     */
    public void pop() {
        arr[size - 1] = 0;
        size--;
    }

    /**
     * 输出
     */
    public void output() {
        System.out.println(Arrays.toString(arr));
    }

    public static void main(String[] args) {
        final var stack = new MyArrayStack(6);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        stack.push(6);
        stack.push(7);
        stack.push(8);
        stack.output();
        stack.pop();
        stack.output();
    }
}
```

使用**链表**实现栈的代码如下：

```java
public class MyLinkedStack {
    private Node head;
    private Node last;
    private int size;

    /**
     * 入栈
     *
     * @param data 数据
     */
    public void push(int data) {
        final var newNode = new Node(data);
        if (size == 0) {
            // 空链表
            head = newNode;
        } else {
            newNode.prev = last;
            last.next = newNode;
        }
        last = newNode;
        size++;
    }

    /**
     * 出栈
     */
    public void pop() {
        final var prevNode = last.prev;
        prevNode.next = null;
        last = prevNode;
        size--;
    }

    /**
     * 输出
     */
    public void output() {
        var temp = this.head;
        for (int i = 0; i < size; i++) {
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
        System.out.println();
    }

    private static class Node {
        Node prev;
        int data;
        Node next;

        Node(int data) {
            this.data = data;
        }
    }

    public static void main(String[] args) {
        final var stack = new MyLinkedStack();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(5);
        stack.push(6);
        stack.push(7);
        stack.push(8);
        stack.output();
        stack.pop();
        stack.output();
    }
}
```

进行**入栈**、**出栈**操作的时间复杂度均为`O(1)`。

## 队列 (Queue)

**队列**(**Queue**)也是一种线性数据结构，队列中的元素遵循**先入先出**(**FIFO**，First In First Out)的原则。队列的出口端称为**队头**，入口端称为**队尾**。

{% asset_img 队列.png %}

### 操作队列

#### 入队 (enqueue)

**入队**(**enqueue**)是将新的元素放入队列中，新元素下一个位置成为新的队尾。

#### 出队 (dequeue)

**出队**(**dequeue**)是将队头的元素移出队列，出队元素的后一个元素成为新的队头。

#### 代码实现

使用**数组**与**链表**实现队列的方式有所不同。

##### 数组实现

在不考虑扩容的情况下，队列的**容量**(**capacity**)是有限的，不断出队会使得队头前的空间逐渐失去作用。此时我们可以使用**循环队列**来保证队列容量的恒定，即使用已经出队的空间，来存放新的元素。

当`(队尾下标 + 1) % 数组长度 = 队头下标`时，表明该队列已满。（可结合单步调试进行理解）

{% asset_img 队列2.png %}

```java
public class MyArrayQueue {
    private int[] array;
    private int front;
    private int rear;

    public MyArrayQueue(int capacity) {
        this.array = new int[capacity];
    }

    /**
     * 入队
     *
     * @param element 入队的元素
     */
    public void enQueue(int element) throws Exception {
        if ((rear + 1) % array.length == front)
            throw new Exception("队列已满");
        array[rear] = element;
        rear = (rear + 1) % array.length;
    }

    /**
     * 出队
     */
    public void deQueue() throws Exception {
        if (rear == front) throw new Exception("队列已空");
        front = (front + 1) % array.length;
    }

    public void output() {
        for (int i = front; i != rear; i = (i + 1) % array.length) {
            System.out.println(array[i]);
        }
    }

    public static void main(String[] args) throws Exception {
        final var queue = new MyArrayQueue(5);
        queue.enQueue(1);
        queue.enQueue(2);
        queue.enQueue(3);
        queue.enQueue(4);
        queue.deQueue();
        queue.deQueue();
        queue.enQueue(5);
        queue.enQueue(6);
        queue.output();
    }
}
```

**循环队列**的意义在于，其不仅**充分利用了数组的空间**，还**避免了数组元素移动带来的性能损失**。其入队与出队的时间复杂度为`O(1)`

##### 链表实现

```java
public class MyLinkedQueue {
    private Node head;
    private Node last;
    private int size;

    /**
     * 入栈
     *
     * @param data 数据
     */
    public void enQueue(int data) {
        final var newNode = new Node(data);
        if (size == 0) {
            // 空队列
            head = newNode;
        } else {
            last.next = newNode;
            newNode.prev = last;
        }
        last = newNode;
        size++;
    }

    /**
     * 出栈
     */
    public void deQueue() {
        final var nextNode = head.next;
        nextNode.prev = null;
        head = nextNode;
        size--;
    }

    /**
     * 输出
     */
    public void output() {
        var temp = head;
        for (int i = 0; i < size; i++) {
            System.out.println(temp.data);
            temp = temp.next;
        }
    }

    private static class Node {
        Node prev;
        int data;
        Node next;

        public Node(int data) {
            this.data = data;
        }
    }

    public static void main(String[] args) {
        final var queue = new MyLinkedQueue();
        queue.enQueue(1);
        queue.enQueue(2);
        queue.enQueue(3);
        queue.enQueue(4);
        queue.deQueue();
        queue.deQueue();
        queue.enQueue(5);
        queue.enQueue(6);
        queue.output();
    }
}
```

## 参考资料

- [《漫画算法：小灰的算法之旅》](https://union-click.jd.com/jdc?e=&p=JF8BAMQJK1olXDYCV1pdCk0TA19MRANLAjZbERscSkAJHTdNTwcKBlMdBgABFksUB28KHV8VQl9HCANtQDt-V2dwXyt2LVZGMQsHDB8UWmlOXVcZbQcyVF9cC04VBWsBHGslXQEyAjBdCUoWAm4NG14WbQcyVFleAE0eB2gLElIRXzYFVFdtUx55dQRLWCBQCXlcMgM9OHsnAF84K1slXjZAOlxbXB5HCzhaGl4SDwMBB15UCx4TC2kMT1lADw9RUVwIOEkWAmsB)
