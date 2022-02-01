---
title: 菜狗学算法——排序
date: 2021/08/29 10:46:24
categories:
- [数据结构与算法, 算法知识]
tags:
- 算法
---
排序在生活中随处可见，在程序中也是如此。

<!-- more -->

例如按照身高排序：

{% asset_img 身高排列.png %}

再例如你在购买商品时的顺序：

{% asset_img 16302493019615.jpg %}

下面将讲解几个比较常见的排序算法。

注意：在计算机中，对一组数据排序需要一个一个「**看**」里面的数据。就类似一组数据在一个「**箱子**」中，我们必须将箱子打开才能知道里面的数据。

{% asset_img 箱子原则.png %}

## 选择排序 (Selection Sort)

**选择排序**（**Selection sort**）是一种简单直观的排序算法。

它的工作原理如下：

1. 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置。
2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
3. 以此类推，直到所有元素均排序完毕。

### 例子

首先给出一组数：

{% asset_img 原始排序.png %}

**选择排序**开始，首先算法开始遍历整个数组，从左往右找最小的数，并且将当前找到的最小数记录下来。当遍历到最后一个数字`1`时，将 `1` 和数组中`0`号元素（`6`）交换位置。将1做出标记，表示它已经到达正确的位置，不再进行排序。

{% asset_img 选择排序1.png %}

后面的元素以类似的方法进行排序。

排序的动画如图所示：

{% asset_img 选择排序.gif %}

{% asset_img 选择排序2.gif %}

### 代码实现

**选择排序**对应的简易 Java 代码实现如下：

```java
import java.util.Arrays;

public class SelectionSort {
    public static void selectionSort(int[] array) {
        for (var i = 0; i < array.length; i++) {
            var min = i;
            for (var j = i + 1; j < array.length; j++) {
                if (array[j] < array[min]) {
                    min = j;
                }
            }
            if (i != min) {
                var temp = array[i];
                array[i] = array[min];
                array[min] = temp;
            }
        }
    }

    public static void main(String[] args) {
        final var arr = new int[]{6, 3, 8, 5, 2, 7, 4, 1};
        selectionSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
```

### 运行时间

**选择排序**算法共有 $n+(n-1)+(n-2)+...+2+1$ (即 $n^2/2 + n/2$ )步，通过**大*O*表示法**表示为***O*($n^2$)**。

## 冒泡排序 (Bubble Sort)

**冒泡排序**（**Bubble Sort**）是一种简单的排序算法。

它重复地走访过要排序的数列，一次比较两个元素，如果他们的顺序错误就把他们交换过来。走访数列的工作是重复地进行直到没有再需要交换，也就是说该数列已经排序完成。

这个算法的名字由来是因为越小的元素会经由交换慢慢“浮”到数列的顶端。

### 例子

首先给出一组数：

{% asset_img 原始排序.png %}

**冒泡排序**开始，首先将 0 号元素和 1 号元素进行比较，如果 0 号元素大于 1 号元素，则将这两个元素位置对调。依此类推。

{% asset_img 冒泡过程.png %}

排序的动画如图所示：

{% asset_img 冒泡排序.gif %}

{% asset_img 冒泡排序2.gif %}

### 代码实现

```java
import java.util.Arrays;

public class BubbleSort {
    public static void bubbleSort(int[] array) {
        for (var i = 0; i < array.length - 1; i++) {
            for (var j = 0; j < array.length - i - 1; j++) {
                var temp = 0;
                if (array[j] > array[j + 1]) {
                    temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        var arr = new int[]{6, 3, 8, 5, 2, 7, 4, 1};
        bubbleSort(arr);
        System.out.println(Arrays.toString(arr));
    }
}
```

### 运行时间

**冒泡排序**算法共有 $(n-1)*(n-1)$ (即 $n^2 - 2n + 1$ )步，通过**大*O*表示法**表示为***O*($n^2$)**。

## 归并排序 (Merge Sort)

**归并排序**（**Merge Sort**）是建立在归并操作上的一种有效，稳定的排序算法，该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。

### 例子

{% asset_img 归并排序.gif %}

{% asset_img 归并排序2.gif %}

## **大*O*表示法**性能分析

以上三种排序的对比可以见 [这个视频](https://www.youtube.com/watch?v=ZZuD6iUe3Pc) ，国内搬运： [Bilibili](https://www.bilibili.com/video/BV1ex411e7eb) 。

| 类型         | 算法               |
| ------------ | ------------------ |
| *O*($n^2$)   | 选择排序、冒泡排序 |
| *O*($nlogn$) | 归并排序           |
| *O*($n$)     | 顺序查找           |
| *O*($logn$)  | 二分查找           |
| *O*($1$)     |                    |

## 参考资料

- [维基百科 - 选择排序](https://en.wikipedia.org/wiki/Selection_sort)
- [维基百科 - 冒泡排序](https://en.wikipedia.org/wiki/Bubble_sort)
- [维基百科 - 归并排序](https://en.wikipedia.org/wiki/Merge_sort)
- [Comparison Sorting Algorithms](https://www.cs.usfca.edu/~galles/visualization/ComparisonSort.html)
- [CS50 2020 Letcure 3 - Algorithms](https://www.youtube.com/watch?v=gR6nycuZKlM)
