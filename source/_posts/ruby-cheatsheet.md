---
title: Ruby 小抄
date: 2023-06-23 17:40:35
categories:
- [编程语言, Ruby]
tags:
- Ruby
---
快速入门 Ruby 语法。

<!-- more -->

## Ruby 安装

- [RubyInstaller for Windows](https://rubyinstaller.org/)
- [RVM(Ruby Version Manager)](https://rvm.io/)
- [rbenv](https://github.com/rbenv/rbenv)

## 实用网站

- [Ruby China](https://ruby-china.org/)

## 标识符

一般习惯使用下划线进行单词分隔

## 注释

```ruby
# 单行注释

=begin
多行
注释
=end
```

## 变量/常量

```ruby
name = 'Ruby'     # 变量

VERSION = '3.2.1' # 常量
```

## 字符串

```ruby
lang = 'ruby'
msg = "I am using #{lang}"  # I am using ruby
msg = 'I am using #{lang}'  # I am using ${lang}

# 多行字符串
puts <<-S
  有
  多
  行
S
#  有
#  多
#  行

puts <<~MESSAGE
      自动
      删除
      缩进
     MESSAGE
# 自动
# 删除
# 缩进
```

## 数组

```ruby
a = ['a', 'b', 'c']
b = ['a', 1, 2, 3]

a + b    # ["a", "b", "c", "a", 1, 2, 3]
a - b    # ["b", "c"]
a | b    # ["a", "b", "c", 1, 2, 3]
a & b    # ["a"]
```

## 哈希表

```ruby
user = {
  id: 1,
  name: 'ruby'
}
user[:name]  # ruby
```

## 空判断

```ruby
# 当 a 为 nil 时，赋值为 100
a ||= 100
a     # 100
```

## 赋值

```ruby
a, b = [1, 2]
a   # 1
b   # 2
```

## 方法调用

```ruby
f1            # 无参省略小括号（推荐）
f1()          # 无参保留小括号

puts 'hi'     # 省略小括号
puts('hi')    # 保留小括号
```

## 类

```ruby
class Foo
  def initialize(name)
    @name = name
  end

  def say
    puts "Hi, #{@name}!"
  end

  def self.bar
    puts 'Foo, bar!'
  end
end

foo = Foo.new 'Jack'
foo.say   # Hi, Jack!

Foo.bar   # Foo, bar!
```

## 继承

```ruby
class Person
  def initialize(name)
    @name = name
  end

  def say
    puts "Hi, I am #{@name}"
  end
end

class Student < Person
  def initialize(name, grade)
    super(name)
    @grade = grade
  end

  def get_grade
    puts "I am grade #{@grade}"
  end
end

stu = Student.new('Jack', 2)
stu.say          # Hi, I am Jack
stu.get_grade    # I am grade 2
```

## 访问权限

```ruby
class Foo
  def public_method
    puts 'public method'
  end

  protected
  def protected_method
    puts 'protected method'
  end

  private
  def private_method
    puts 'private method'
  end
end

foo = Foo.new
foo.public_method      # public method
foo.protected_method   # ERROR! protected method `protected_method' called for #<Foo:0x00000001010316f8> (NoMethodError)
foo.private_method     # ERROR! private method `private_method' called for #<Foo:0x00000001032a61c0> (NoMethodError)
```
