---
title: 牛客小白月赛 45 解题记录
date: 2022-03-04 23:20:15
categories:
  - [数据结构与算法, 算法题解]
tags:
  - 算法竞赛
mathjax: true
---

2022 年 3 月 4 日晚 7:00 - 9:00。[比赛链接](https://ac.nowcoder.com/acm/contest/11222) [官方题解链接](https://ac.nowcoder.com/discuss/854301)

<!-- more -->

## A - 悬崖

[题目直达](https://ac.nowcoder.com/acm/contest/11222/A)

最长跳的距离即为秒数 n 与每次跳跃长度的乘积，如果跳跃长度小于两墙之间的距离，则最大长度为跳跃长度。

```cpp
#include <ios>
#include <iostream>
#define endl '\n'
typedef long long ll;
using namespace std;

ll x, n;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> x >> n;
  if (n > x) {
    cout << x << endl;
  } else {
    cout << n * x << endl;
  }

  return 0;
}
```

## B - 数数

[题目直达](https://ac.nowcoder.com/acm/contest/11222/B)

**法 1**：

直接在递归中加入停止条件及计数器即可。

```cpp
#include <ios>
#include <iostream>
#define endl '\n'
typedef long long ll;
using namespace std;

ll n, flg, ans;

void dfs(int cnt) {
  flg++;
  if (flg > n) return;
  for (int i = 1; i <= cnt; ++i) ans++;
  dfs(cnt + 2);
}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> n;
  dfs(1);
  cout << ans << endl;

  return 0;
}
```

**法 2**：

| `i` | `dfs(i)` |
| :-: | :------: |
|  1  |    1     |
|  3  |    3     |
|  5  |    5     |
|  7  |    7     |
|  9  |    9     |

公式：

$$ (1+2*n-1)*n/2 = n^{2}$$

```cpp
#include<iostream>
using namespace std;
int main(){
  long long n;
  cin >> n;
  cout << n * n << "\n";
}
```

## C - 山楂

[题目直达](https://ac.nowcoder.com/acm/contest/11222/C)

| `a[n]`糖果个数 | 增加积分数 | 积分表达式  | `a[i+1]`添加数 |
| :------------: | :--------: | :---------: | :------------: |
|       0        |     0      |      0      |       0        |
|       1        |     0      |      0      |       0        |
|       2        |     0      |      0      |       0        |
|       3        |     3      |      3      |       1        |
|       4        |     4      |      4      |       1        |
|       5        |     4      |      4      |       1        |
|       6        |     6      |     3+3     |       2        |
|       7        |     7      |     3+4     |       2        |
|       8        |     8      |     4+4     |       2        |
|       9        |     9      |    3+3+3    |       3        |
|       10       |     10     |    3+3+4    |       3        |
|       11       |     11     |    3+4+4    |       3        |
|       12       |     12     |   3+3+3+3   |       4        |
|       13       |     13     |   3+3+3+4   |       4        |
|       14       |     14     |   3+3+4+4   |       4        |
|       15       |     15     |  3+3+3+3+3  |       5        |
|       16       |     16     |  3+3+3+3+4  |       5        |
|       17       |     17     |  3+3+3+4+4  |       5        |
|       18       |     18     | 3+3+3+3+3+3 |       6        |

该题尽可能地加入 3 的组数。因为任意数模 3 只能为 1 和 2，若模为 1 的话则有 1 个 4，否则为 2 个 4。

对于任意数（除 1、2、5）而言，增加的积分数都为 `a[n]` 的个数。 故 1、2、5 三个数需要特判。

```cpp
#include <algorithm>
#include <ios>
#include <iostream>
#define endl '\n'
typedef long long ll;
using namespace std;

ll a[10];
ll ans;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  for (int i = 1; i <= 8; ++i) cin >> a[i];
  for (int i = 1; i <= 8; ++i) {
    if (a[i] == 1 || a[i] == 2) {
      continue;
    } else if (a[i] == 5) {
      a[i + 1] += 1;
      ans += i * 4;
    } else {
      ans += i * a[i];
      a[i + 1] += a[i] / 3;
    }
  }
  cout << ans << endl;

  return 0;
}
```

## D - 切糕

[题目直达](https://ac.nowcoder.com/acm/contest/11222/D)

合法括号：左右括号的个数一样多，且每个右括号左边的左括号始终不小于右括号数量。

```cpp
#include <algorithm>
#include <ios>
#include <iostream>
#include <string>
#define endl '\n'
typedef long long ll;
using namespace std;

const ll MOD = 1e9 + 7;

string s;
ll cnt, lft;
ll ans = 1;
int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  cin >> s;
  for (int i = 0; i < s.length(); ++i) {
    if (s[i] == '(') {
      lft++;
    } else if (s[i] == ')') {
      lft--;
      if (lft < 0) {
        cout << -1 << endl;  // 左括号数小于右括号数
        return 0;
      } else if (lft == 0) {  // 剩余左括号为 0，切割点增加
        cnt++;
      }
    }
  }

  if (lft != 0) {
    cout << -1 << endl;
    return 0;
  }

  for (int i = 0; i < cnt - 1; ++i) ans = ans * 2 % MOD;
  cout << ans % MOD << endl;

  return 0;
}
```

## E - 筑巢

[题目直达](https://ac.nowcoder.com/acm/contest/11222/E)

待更新

## F - 交换

[题目直达](https://ac.nowcoder.com/acm/contest/11222/F)

待更新
