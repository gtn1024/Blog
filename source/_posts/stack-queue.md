---
title: 栈、队列、单调栈、单调队列例题分析
date: 2022-03-02 20:31:08
categories:
- [数据结构与算法, 算法知识]
tags:
- 数据结构
---
**栈**、**队列**、**单调栈**、**单调队列** 是算法中十分常见的数据结构。

<!-- more -->

## 栈

栈是一种 FILO （先入后出）的数据结构。关于 **栈** 相关的知识参见 [本篇文章](https://getaoning.com/archives/data-structure-stack-queue/#栈-stack) 。

### 栈例 1

> 有 n 个人，按照 1, 2, 3, 4, …, n 的顺序依次进栈。判断是否能够以所给序列出栈。
>
> 第一行为样例个数 t，第二行为人数 n。

**输入**：

```text
4
4
4 3 2 1
1 2 3 4
1 3 2 4
1 4 2 3
```

**输出**：

```text
YES
YES
YES
NO
```

**样例说明**：

样例 1：1 进，2 进，3 进，4 进，4 出，3 出，2 出，1 出。

样例 2：1 进，1 出，2 进，2 出，3 进，3 出，4 进，4 出。

样例 3：1 进，1 出，2 进，3 进，3 出，2 出，4 进，4 出。

样例 4：1 进，1 出，2 进，3 进，4 进，4 出。此时由栈底到栈顶元素为 2、3，出去的元素只能为 3。故该情况不成立。

**题目分析**：

使用 j 变量来存储当前判断的输入元素（即 a 数组的下标），持续判断栈顶元素是否等于当前判断元素，如果相等则将该元素从栈中弹出，同时将 j 加一。否则继续向栈中添加元素，重复前面的判断过程。

**参考代码**：

C++ 实现：

```cpp
#include <ios>
#include <iostream>
#include <stack>
#define endl '\n'
typedef long long ll;
using namespace std;

int T, n;
int a[60010];
stack<int> st;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);
  cin >> T >> n;
  while (T--) {
    for (int i = 1; i <= n; ++i) cin >> a[i];
    int j = 1;
    for (int i = 1; i <= n; ++i) {
      st.push(i);
      while (!st.empty() && a[j] == st.top()) {
        st.pop();
        j++;
      }
    }
    if (st.empty())
      cout << "YES" << endl;
    else
      cout << "NO" << endl;
  }
  return 0;
}
```

Java 实现：

```java
import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    int T = sc.nextInt();
    int n = sc.nextInt();
    int[] a = new int[60010];
    ArrayDeque<Integer> st = new ArrayDeque<>();
    while (T-- != 0) {
      for (int i = 1; i <= n; i++)
        a[i] = sc.nextInt();
      int j = 1;
      for (int i = 1; i <= n; i++) {
        st.push(i);
        while (!st.isEmpty() && a[j] == st.peek()) {
          st.pop();
          j++;
        }
      }
      if (st.isEmpty())
        System.out.println("YES");
      else
        System.out.println("NO");
    }
    sc.close();
  }
}
```

### 栈例 2 —— 栈和排序

题目来源：[NC14893](https://ac.nowcoder.com/acm/problem/14893)

> 给你一个1->n的排列和一个栈，入栈顺序给定
>
> 你要在不打乱入栈顺序的情况下，对数组进行从大到小排序
>
> 当无法完全排序时，请输出字典序最大的出栈序列

**输入描述**:

> 第一行一个数n
>
> 第二行n个数，表示入栈的顺序，用空格隔开，结尾无空格

**输出描述**：

> 输出一行n个数表示答案，用空格隔开，结尾无空格

**样例输入**：

```text
5
2 1 5 3 4
```

**样例输出**：

```text
5 4 3 1 2
```

**样例说明**：

2 入栈；1 入栈；5 入栈；5 出栈；3 入栈；4 入栈；4 出栈；3 出栈；1 出栈；2 出栈

**题目分析**：

该题首先将输入数据存入数组 a，并使用数组来存放当前所在元素及其右侧最大的元素。当栈顶元素大于右侧元素时，则可以出栈。

**参考代码**：

C++ 实现：

```cpp
#include <algorithm>
#include <ios>
#include <iostream>
#include <stack>
#define endl '\n'
typedef long long ll;
using namespace std;

stack<int> st;
int n;
int a[6000010], maxn[6000010];

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> n;
  for (int i = 1; i <= n; ++i) cin >> a[i];
  for (int i = n; i >= 1; --i) maxn[i] = max(maxn[i + 1], a[i]); // 记录右侧最大值
  for (int i = 1; i <= n; ++i) {
    st.push(a[i]);
    while (!st.empty() && st.top() > maxn[i + 1]) {
      cout << st.top() << ' ';
      st.pop();
    }
  }
  while (!st.empty()) {
    cout << st.top() << ' ';
    st.pop();
  }
  return 0;
}
```

### 栈例 3 —— 牛牛与后缀表达式

题目来源：[NC212914](https://ac.nowcoder.com/acm/problem/212914)

>给定牛牛一个后缀表达式s，计算它的结果，例如，1+1对应的后缀表达式为`1#1#+`，`#`作为操作数的结束符号。
>
>其中，表达式中只含有`+`、`-`、`*`三种运算，不包含除法。
>
>本题保证表达式一定合法，且计算过程和计算结果的绝对值一定不会超过 $10^{18}$

**参数**：

```text
"1#1#+"
"12#3#+15#*"
```

**返回值**：

```text
2
225
```

**样例说明**：

样例 1：`1#1#+`这个后缀表达式表示的式子是$1+1$，结果为$2$

样例 2：`12#3#+15#*`这个后缀表达式表示的式子是$(12+3)*15$，结果为$225$

**题目分析**：

该题使用 **栈** 这种数据结构来存储。将数字丢入栈中，如果遇到运算符则将栈顶的两个元素拿出来运算后将结果再次丢入栈中。最终栈中的元素即为结果。

==注意：减法时需要注意正负号==

**参考代码**：

Java 实现：

```java
import java.util.ArrayDeque;

public class Solution {
  public long legalExp(String str) {
    ArrayDeque<Long> st = new ArrayDeque<>();
    long tmp = -1;
    for (char c : str.toCharArray()) {
      if (c == '#') {
        st.push(tmp);
        tmp = -1;
      } else if (c == '+' || c == '-' || c == '*') {
        Long a = st.pop();
        Long b = st.pop();
        switch (c) {
          case '+':
            st.push(a + b);
            break;
          case '-':
            st.push(-a + b);
            break;
          case '*':
            st.push(a * b);
            break;
        }
      } else {
        if (tmp == -1) {
          tmp = (int) (c - '0');
        } else {
          tmp *= 10L;
          tmp += (int) (c - '0');
        }
      }
    }
    return st.pop();
  }
}
```

### 栈例 4 —— 好串

题目来源：[NC21874](https://ac.nowcoder.com/acm/problem/21874)

> 牛牛喜欢跟字符串玩耍，他刚刚学会了一个新操作，将一个字符串x插入另一个字符串y中（包括放在开头和结尾）
>
> 牛牛认为如果一个串是好的当这个串能按照如下方法被构造出来：
>
> 一开始，有一个空串，然后执行0次或者若干次操作，每次操作将`ab`插入当前的字符串
>
> 根据上面的定义，`ab`, `aabb`, `aababb`都是好串，`aab`,`ba`,`abbb`并不是好串
>
> 现在给你一个字符串s，判断s是否是好串

**输入描述**：

> 输入一行包含一个字符串，长度不超过 50

**输出描述**：

> 输出 `Good` 或者 `Bad`

**样例输入**：

```text
ab
aab
abaababababbaabbaaaabaababaabbabaaabbbbbbbb
```

**样例输出**：

```text
Good
Bad
Bad
```

**备注**：

> 子任务1：n <= 10
>
> 子任务2：n <= 20
>
> 子任务3：无限制

#### 使用栈进行操作

使用栈进行实现，如果字符为 `a`，则将该字符投入栈中。如果字符为 `b`，则判断栈顶元素是否为 `a`。

**参考代码**：

C++ 实现：

```cpp
#include <bits/stdc++.h>

using namespace std;
stack<char> st;
bool solve(string s) {
  for (int i = 0; i < s.length(); ++i) {
    if (s[i] == 'a') {
      st.push(s[i]);
    } else if (s[i] == 'b') {
      if (!st.empty() && st.top() == 'a') {
        st.pop();
      } else {
        return false;
      }
    }
  }
  return st.empty();
}
int main() {
  string s;
  cin >> s;
  cout << (solve(s) ? "Good" : "Bad") << endl;
  return 0;
}
```

Java 实现：

```java
import java.util.ArrayDeque;
import java.util.Scanner;

public class Main {
  static ArrayDeque<Character> st = new ArrayDeque<>();

  static boolean solve(String s) {
    for (char c : s.toCharArray()) {
      if (c == 'a') {
        st.push(c);
      } else if (c == 'b') {
        if (!st.isEmpty() && st.peek() == 'a') {
          st.pop();
        } else {
          return false;
        }
      }
    }
    return st.isEmpty();
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String st = sc.nextLine();
    sc.close();
    System.out.println(solve(st) ? "Good" : "Bad");
  }
}
```

#### 字符串操作

该题也可以直接通过字符串替换进行。

```java
import java.util.Scanner;

public class Main {
  static boolean solve(String s) {
    while (s.contains("ab")) {
      s = s.replace("ab", "");
    }
    return s.equals("");
  }

  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    String st = sc.nextLine();
    sc.close();
    System.out.println(solve(st) ? "Good" : "Bad");
  }
}
```

## 队列

待更新

## 单调栈

待更新

## 单调队列

待更新
