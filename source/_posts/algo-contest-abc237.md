---
title: 菜狗写题解——AtCoder ABC 237 题解
date: 2022-01-31 14:39:50
categories:
- [数据结构与算法, 算法题解]
tags:
- 算法竞赛
mathjax: true
---
2022 年 1 月 30 日晚 8:00 - 9:40。[比赛链接](https://atcoder.jp/contests/abc237)

<!-- more -->

## A - Not Overflow

[题目链接](https://atcoder.jp/contests/abc237/tasks/abc237_a)

### 题面翻译

给出一个整数 $ N $，如果 $ N $ 在 $ -2^{31} $ 和 $ 2^{31} - 1 $ 之间，打印 `Yes`，否则打印`No`。

**数据范围：**

- $$ -2^{63} \leq N < 2^{63} $$

### 题意理解

签到题，数据范围在 8 字节整数以内，使用 C++ 时注意数据类型开到`long long`即可。

### AC 代码

```python
n = int(input())
if (-2**31 <= n <= 2**31 - 1):
  print('Yes')
else:
  print('No')
```

## B - Matrix Transposition

[题目链接](https://atcoder.jp/contests/abc237/tasks/abc237_b)

### 题面翻译

给了一个 $ H - W $ 的矩阵 $ A $，矩阵 $ B $ 是 $ W - H $ 的矩阵。使矩阵 $ B $ 是矩阵 $ A $ 的转置，并打印出 $ B $。

**数据范围：**

- $$ 1 \leq H, W \leq 10^{5} $$
- $$ H \times W \leq 10^{5} $$
- $$ 1 \leq A_{i, j} \leq 10^{9} $$

### 题意理解

签到题，随便写写也就过了。

### AC 代码

```cpp
#include <bits/stdc++.h>
using namespace std;
int main() {
  int H, W;
  cin >> H >> W;
  int ls[H][W];
  int new_ls[W][H];
  for (int i = 0; i < H; i++) {
    for (int j = 0; j < W; j++) {
      cin >> ls[i][j];
      new_ls[j][i] = ls[i][j];
    }
  }
  for (int i = 0; i < W; i++) {
    for (int j = 0; j < H; j++) {
      cout << new_ls[i][j] << ' ';
    }
    cout << endl;
  }
  return 0;
}
```

## C - kasaka

[题目链接](https://atcoder.jp/contests/abc237/tasks/abc237_c)

### 题面翻译

给出一个只包含小写字母的字符串 $ S $，判断是否可以在 $ S $ 前面添加一些 `a`（可能为 0 个）使他构成回文字符串。

**数据范围：**

- $$ 1 \leq \lvert S \lvert \leq 10^{6} $$

### 题意理解

从左往右数有 `l` 个 `a`，然后从右往左数有 `r` 个 `a`，如果 $ r > l $，则在 $ S $ 左边加入 `r - l` 个 `a`，判断是否构成回文字符串（将字符串反转即可判断是否为回文字符串）。

### AC 代码

```python
def deter(s):
  return s == ''.join(reversed(s))


s = input()
l = 0
r = 0
for i in range(len(s)):
  if s[i] == 'a':
    l += 1
  else:
    break

for i in range(len(s) - 1, -1, -1):
  if s[i] == 'a':
    r += 1
  else:
    break

if r >= l and deter((r - l) * 'a' + s):
  print('Yes')
else:
  print('No')
```

## D - LR insertion

[题目链接](https://atcoder.jp/contests/abc237/tasks/abc237_d)

### 题面翻译

有个序列 $A$ 只含有一个 $ 0 $，给出一个长度为 $ N $ 只含有`L`和`R`的字符串 $ S $。

对于任意 $ i = 1, 2, ..., N $，遵循以下原则：

- 如果 $ S_{i} $ 是 `L`，在 $ A $ 中 $ i - 1$ 的左边插入 $ i $
- 如果 $ S_{i} $ 是 `R`，在 $ A $ 中 $ i - 1$ 的右边插入 $ i $

打印出最终的 $ A $。

**数据范围：**

- $$ 1 \leq N \leq 5 \times 10^{5} $$
- $$ \lvert S \lvert = N $$

### 题意理解

这题可以使用 **动态数组** 进行实现，并使用 **迭代器** 来确定欲添加的数据位置。

**注意：**

- C++ STL 中，`vector` 基于数组实现，`list` 基于链表实现。`vector` 可以通过下标进行随机访问，而 `list` 不行。因为链表的特性，需要进行大量数据插入时，使用 `list` 时效率更高。
- 无论是 `vector` 还是 `list` 的 `insert` 方法都返回 **新的迭代器位置**，需要将迭代器重新赋值为返回值！（否则 `Segmentation fault` 到怀疑人生……）
- 别想着不停地用 `std::find()` ，TLE 把你送回家。

### AC 代码

```cpp
#include <cstdio>
#include <list>
using namespace std;
int main() {
  int n;
  scanf("%d", &n);
  list<int> ls;
  ls.push_back(0);
  auto it = ls.begin();
  getchar();  // ignore \n
  char op;
  for (int i = 1; i <= n; i++) {
    scanf("%c", &op);
    if (op == 'L') {
      it = ls.insert(it, i);
    } else {
      it++;
      it = ls.insert(it, i);
    }
  }
  for (auto &&i : ls) {
    printf("%d ", i);
  }
  return 0;
}
```
