---
title: Java IO 笔记
date: 2024-05-22 17:20:24
categories:
- [编程语言, Java]
tags:
- Java
---
文件 IO：用于处理数据。将数据保存到文件等其他物理设备上，保证数据可以在断电后持久保存。

## File 类

`File` 代表了文件或者目录，用于操作文件或目录本身，不能读取文件内容。

## IO流

### 流的分类

按照 **方向** 分：

- 输入流：读取数据；
- 输出流：写出数据。

按照 **数据单元** 分：

- 字节流：每次读写一个字节，可以读写任意文件（以 `Stream` 结尾）；
- 字符流：每次读写一个字符，可以方便地读写文本文件（以 `Reader/Writer` 结尾）。

按照 **角色** 分：

- 节点流：直接关联代表数据源的 IO 节点
- 处理流（包装流、过滤流）：建立在其他流的基础之上，用于对其他流进行包装。

输入流的基本方法：

- `read()`：读取一个单位；
- `int read(Object[] buff)`：读取N个单位到数组中，返回实际读取的单位数。

输出流的基本方法：

- `write(int)`：输出一个单位；
- `void write(Obejct[] buff)`：输出数组中所有数据。

**节点流** 主要如下：

|     | `InputStream` | `OutputStream` | `Reader` | `Writer` |
| --- | ----------- | ------------- | ------- | ------- |
| 文件 | `FileInputStream` | `FileOutputStream` | `FileReader` | `FileWriter` |
| 数组 | `ByteArrayInputStream` | `ByteArrayOutputStream` | `CharArrayReader` | `CharArrayWriter` |
| 字符串 |  |  | `StringReader` | `StringWriter` |

**处理流** 主要如下：

|     | `FilterInputStream` | `FilterOutputStream` | `FilterReader` | `FilterWriter` |
| --- | ----------- | ------------- | ------- | ------- |
| 缓冲流 | `BufferedInputStream` | `BufferedOutputStream` | `BufferedReader` | `BufferedWriter` |
| 打印流 |  | `PrintStream` |  | `PrintWriter` |
| 转换流 |  |  | `InputStreamReader` | `OutputStreamWriter` |
| 特殊流 | `DataInputStream` | `DataOutputStream` |  |  |
| 对象流 | `ObjectInputStream` | `ObjectOutputStream` |  |  |

### 缓冲流

内存速度 > 外设速度

如果让内存输出一个数据单元，然后外设处理一个数据单元，必须等外设处理好数据单元之后，内存才会在此输出下一个单元。此时必然会造成性能浪费。

使用缓冲流，内存首先将所有数据输出到缓冲区，缓冲区中的数据留给外设慢慢处理。

使用缓冲流时，需要使用 `flush()` 方法将数据冲到外设中。

如果使用 `close()` 关闭流，程序保证会先执行 `flush()`。

###  打印流

`System.out`、`System.err` 均为 `PrintStream` 对象。

**总结**：

一般而言，输入使用 `BufferedReader`，输出使用 `PrintStream`。

### 转换流

将字节流转换成字节流。很多情况下，程序拿到的是字节流，但确认数据只可能为字符，此时将字节流转换为字符流。

### 特殊流

`DataInputStream` 提供一系列 `readXxx()` 方法用于读取不同类型的数据。

`DataOutputStream` 提供一系列 `writeXxx()` 方法用于写出不同类型的数据。

`DataInputStream` 和 `DataOutputStream` 是使用 Java 内部格式来记录数据的，因此 `DataOutputStream` 输出的数据应该使用 `DataInputStream` 来读取。

### 重定向标准输入输出

标准输出默认为屏幕。`System.setOut(PrintStream out)` 方法可以将输出重定向到另一个流。

标准输入默认为键盘。`System.setIn(InputStream in)` 方法可以将输入重定向到另一个流。

### 读取其他进程的数据

`Runtime` 类中的 `exec()` 方法可用于运行平台上的程序，该方法返回运行的 `Process` 对象。

`Process` 提供如下当法：

- `InputStream getErrorStream()`：返回进程错误的输入流。
- `InputStream getInputStream()`：返回进程标准输入流。
- `OutputStream getOutputStream()`：返回进程的标准输出流。

### `RandomAccessFile`

`RandomAccessFile` 指任意访问，只能读写文件。

输出流不能追加内容，但 `RandomAccess` 可以。

`RandomAccessFile` 通常可用于实现多线程、断点下载工具。

### 对象序列化

序列化：将内存中的 Java 对象转换成字节文件（二进制文件），该二进制文件内容既可以保存到磁盘，也可以通过网络传输。
反序列化：将二进制数据恢复为原始的 Java 对象。

广义上来说，Java 序列化还包括 XML 序列化、JSON 序列化。

`Serializable`：标志接口，实现该接口的对象即可被序列化。

####  `transient` 关键字

有些时候，程序希望将某些 field 排除在序列化机制之外，可使用 `transient` 关键字修饰。

Java 不会序列化：

- 方法
- `transient` 修饰的实例变量
- `static` 变量

#### 自定义序列化

类可以通过实现如下方法实现自定义序列化：

```java
 private void writeObject(java.io.ObjectOutputStream out)
	 throws IOException
 private void readObject(java.io.ObjectInputStream in)
     throws IOException, ClassNotFoundException;
```

#### 序列化版本

当程序要反序列化时，需要两个东西才能反序列化成功：

- 序列化的数据
- 类文件

Java 序列化机制识别一个类是否发生了改变，依赖的是 Java 类的序列化版本。

一个可序列化的 Java 类，总有一个序列化版本号：

1. 如果没有显式指定，系统会为他分配一个序列化版本号。只要 Java 源程序发生修改，编译后会重新生成一个新的版本号。
2. 显式指定一个序列化版本号。

序列化版本号可以使用 `serialver` 命令查看。

推荐开发者为自己的类指定序列化版本号，只有当增加、删除实例变量时才需要增加版本号。

## NIO

NIO 的出现，进一步简化了 IO 操作

### `Path`

`Path` 代表一条路径（既可是文件的路径，也可是目录的路径）

可以通过 `Path.of()` 方法获取 `Path` 对象。

### `Files` 工具类

`Files` 类为文件 IO 的工具类。文件复制、移动、删除、重命名等操作都可以实现。

可以使用 `Files.walk()` / `Files.walkFileTree()` 方法遍历目录。
