---
title: 菜狗学算法——基础知识
date: 2021/08/23 10:28:10
categories:
- [数据结构与算法, 算法知识]
tags:
- 算法
---

**算法**（**Algorithm**）是用来解决问题的方法。对于相同的问题，使用不同的算法，可能得到的结果是相同的，但在其背后所消耗的资源（时间、空间）也许千差万别。

<!-- more -->

## 二分查找

还记得 [CS50 撕书教授 David 撕电话薄的视频](https://www.youtube.com/watch?v=YoXxevp1WRQ)吗？

{% asset_img er-1.png %}

{% asset_img er-2.png %}

在该视频中，David 想要在电话薄中查找自己的姓名。他每次将电话薄从中间撕开，判断其姓名首字母`D`在该页的前面还是后面，丢掉无用的部分。这段视频生动的展示了「**二分查找**(**Binary Search**)」这种算法。

那么，**二分查找**究竟解决了什么痛点？

使用**顺序查找**(**Linear Search**)时，我们可能从前往后找所需的一个数据。

仍然以电话簿为例。假如整本电话薄有 1024 页，你最多需要找 1024 次才能找到你所需要的姓名。

而使用**二分查找**时，你最多只需要寻找 **$log_2 1024 = 10$** 次就可以找到你所需要的姓名。

如上所示的两种查找方式的时间增长趋势如下图：

{% asset_img 顺序二分增长趋势.png %}

## 运行时间

### 大 _O_ 表示法

**运行时间**(**Running time**)指一个算法执行所用的时间。有许多方式可以代表**运行时间**，其中最为广泛的是「**大_O_表示法**」。它使用斜体的_O_来表示。**大_O_表示法**表示了一个算法最差的情况所需的运行时间。

上面所示的增长趋势用**大_O_表示法**可以为以下图像：

{% asset_img BigO-1.png %}

为了表示某一算法的增长趋势，通常我们会省略一些**东西**（例如**系数**、**底数**等），故以上图像可以再次优化：

{% asset_img BigO-2.png %}

下面列举几个常见的**大_O_表示法**的表现形式：

- **_O_($n^2$)**
- **_O_(n log n)**
- **_O_(n)** (如**顺序查找**)
- **_O_(log n)** (如**二分查找**)
- **_O_(1)**

### 大 _Ω_(_Omega_) 表示法

与**大_O_表示法**相反，**大 _Ω_ 表示法**表示了最好的情况。

下面列举几个常见的**大_Ω_表示法**的表现形式：

- **_Ω_($n^2$)**
- **_Ω_(n log n)**
- **_Ω_(n)**
- **_Ω_(log n)**
- **_Ω_(1)** (如**顺序查找**、**二分查找**)

## 参考资料

- [CS50 2020 Letcure 0 - Scratch](https://www.youtube.com/watch?v=YoXxevp1WRQ)
- [CS50 2020 Letcure 3 - Algorithms](https://www.youtube.com/watch?v=gR6nycuZKlM)
- [《算法图解》](https://union-click.jd.com/jdc?e=&p=JF8BAMQJK1olXDYCV15YAUIVAF9MRANLAjZbERscSkAJHTdNTwcKBlMdBgABFksUA2oBElkWQl9HCANtFilwXRpyTAN2AVJ7CUQ8Xi8TS2xbXVcZbQcyVF9cC04VBWsBHGslXQEyAjBdCUoWAm4NH1wSbQcyVFlfCUsTB2cPGl4TWTYFVFdtUx55dQRLWCBQCXlcMgM9OHsnAF84K1slXjZAOlpaARhHU2dfHFkTXgNXBgxVXx4QAjwAG1wSXwBRB1tbOEkWAmsB)
