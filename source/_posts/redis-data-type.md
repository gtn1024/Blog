---
title: Redis 入门 —— Redis 数据类型及其命令
date: 2024-07-14 13:27:36
tags:
- Redis
---

Redis 是一个 key-value 数据库，key 一般为 String 类型，value类型多种多样。

部分 Redis 数据结构如下：

|数据类型|举例|类型|
|---|---|---|
|String|Hello world|基本类型|
|Hash|{name: "gtn1024", age: 18}|基本类型|
|List|[A -> B -> C -> C]|基本类型|
|Set|{A, B, C}|基本类型|
|SortedSet|{A: 1, B: 2, C: 3}|基本类型|
|GEO|{A: (120.3, 30.5) }|特殊类型|
|BitMap|110110101110101000|特殊类型|
|HyperLog|110110101110101000|特殊类型|

<!-- more -->

## Redis 通用命令

### KEYS

```txt
KEYS pattern
summary: Returns all key names that match a pattern.
since: 1.0.0
group: generic
```

```shell
redis> KEYS *
1) age
2) name
redis> KEYS n*
1) name
```

### DEL

```txt
DEL key [key ...]
summary: Deletes one or more keys.
since: 1.0.0
group: generic
```

```shell
redis> KEYS *
1) age
2) k1
3) name
4) k3
5) k2
redis> DEL name
1
redis> DEL k1 k2 k3
3
redis> KEYS *
1) age
```

### EXISTS

```txt
EXISTS key [key ...]
summary: Determines whether one or more keys exist.
since: 1.0.0
group: generic
```

```shell
redis> KEYS *
1) age
redis> EXISTS name
0
redis> EXISTS age
1
```

### EXPIRE / TTL

```txt
EXPIRE key seconds [NX|XX|GT|LT]
summary: Sets the expiration time of a key in seconds.
since: 1.0.0
group: generic

TTL key
summary: Returns the expiration time in seconds of a key.
since: 1.0.0
group: generic
```

```shell
redis> EXPIRE age 20
1
redis> TTL age
16
redis> TTL age
13
redis> TTL age
13
redis> KEYS *
1) age
redis> TTL age
5
redis> TTL age
-2
redis> KEYS *
(empty array)
redis> set name gtn1024
OK
redis> TTL name
-1
```

## String

根据格式的不同，可以分为三类：

- string：普通字符串
- int：整数类型，可以做自增、自减操作
- float：浮点类型，可以做自增、自减操作

常用命令：

- SET：添加或者修改已经存在的一个 String 类型的键值对
- GET：根据 key 获取 String 类型的 value
- MSET：批量添加多个 String 类型的键值对
- MGET：根据多个 key 获取多个 String 类型的 value
- INCR：让一个整型的 key 自增 1
- INCRBY：让一个整型的 key 自增并指定步长，例如：`INCRBY num 2` 让 num 值自增 2
- INCRBYFLOAT：让一个浮点类型的数字自增并指定步长
- SETNX：添加一个 String 类型的键值对，前提是这个 key 不存在，否则不执行
- SETEX：添加一个 String 类型的键值对，并且指定有效期

key 的层级

```shell
redis> SET a:b:1 ok
OK
redis> SET a:b:2 ok2
OK
redis> SET a:c:1 ok3
OK
redis> SET a:c:2 ok4
OK
redis> KEYS *
1) a:b:2
2) a:c:1
3) a:c:2
4) a:b:1
```

使用 Redis 相关 GUI 客户端时，能够自动为其分为层级。

{% asset_img 20240714114857.png %}

## Hash

String 类型可以将对象序列化为 JSON 字符串后存储，当需要修改对象里某一个字段的时候很不方便。

{% asset_img 20240714120350.png %}

常用命令：

- HSET key field value：添加或者修改 hash 类型 key 的 field 的值
- HGET key field：获取一个 hash 类型 key 的 field 的值
- HMSET：批量添加多个 hash 类型 key 的 field 的值
- HMGET：批量获取多个 hash 类型 key 的 field 的值
- HGETALL：获取一个 hash 类型的 key 中的所有的 field 和 value
- HKEYS：获取一个 hash 类型的 key 中的所有的 field
- HVALS：获取一个 hash 类型的 key 中的所有的 value
- HINCRBY：让一个 hash 类型 key 的字段值自增并指定步长
- HSETNX：添加一个 hash 类型的 key 的 field 值，前提是这个 field 不存在，否则不执行

## List

Redis 中的 List 类型与 Java 中的 `LinkedList` 类似，可以看作是一个双向链表的结构。既可以支持正向检索也可以支持反向检索。

特征也与 `LinkedList` 类似：

- 有序
- 元素可以重复
- 插入和删除快
- 查询速度一般

常用命令：

- LPUSH key element ...：向列表左侧插入一个或多个元素
- LPOP key：移除并返回列表左侧的第一个元素，没有则返回 nil
- RPUSH key element ...：向列表右侧插入一个或多个元素
- RPOP key：移除并返回列表右侧的第一个元素
- LRANGE key starend：返回一段角标范围内的所有元素
- BLPOP 和 BRPOP：与 LPOP 和 RPOP 类似，只不过在没有元素时等待指定时间，而不是直接返回 nil

## Set

Redis 的 Set 结构和 Java 中的 HashSet 类似。

特征也与 `HashSet` 类似：

- 无序
- 元素不可重复
- 查找快
- 支持交集、并集、差集等功能

常用命令：

- SADD key member ...：向 set 中添加一个或多个元素
- SREM key member ...：移除 set 中的指定元素
- SCARD key：返回 set 中元素的个数
- SISMEMBER key member：判断一个元素是否存在于 set 中
- SMEMBERS：获取 set 中的所有元素
- SINTER key1 key2 ...：求 key1 与 key2 的交集
- SDIFF key1 key2 ...：求 key1 与 key2 的差集
- SUNION key1 key2 ...：求 key1 和 key2 的并集

## SortedSet

Redis 的 SortedSet 是一个可排序的 set 集合，与 Java 中的 TreeSet 有点类似，但是底层的数据结构差别很大。

SortedSet 中的每一个元素都带有一个 score 属性，可以基于 score 属性对于元素进行排序，底层实现是一个跳表 + hash 表。

SortedSet 具有下列特征：

- 可排序
- 元素不重复
- 查询速度快

因为 SortedSet 可排序的特性，经常用来实现排行榜这样的功能。

常用命令：

- ZADD key score member：添加一个或多个元素到 sorted set，如果已经存在则更新其 score 值
- ZREM key member：删除 sorted set 中的一个指定元素
- ZSCORE key member：获取 sorted set 中的指定元素的 score 值
- ZRANK key member：获取 sorted set 中的指定元素的排名
- ZCARD key：获取 sorted set 中的元素个数
- ZCOUNT key min max：统计 score 值在给定范围内的所有元素的个数
- ZINCRBY key increment member：让 sorted set 中的指定元素自增，步长为指定的 increment 值
- ZRANGE key min max：按照 score 排序后，获取指定排名范围内的元素
- ZRANGEBYSCORE key min max：按照 score 排序后，获取指定 score 范围内的元素
- ZDIFF、ZINTER、ZUNION：求差集、交集、并集
