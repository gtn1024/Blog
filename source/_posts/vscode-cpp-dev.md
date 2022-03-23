---
title: VSCode 搭建 C++ 开发环境
date: 2022-01-23 12:54:48
categories:
- 实用技巧
tags:
- IDE
- VSCode
- C++
---
**VSCode**(Visual Studio Code)是一款由微软开发且跨平台的轻量级编辑器。可通过各种插件扩展实现各个编程语言的开发（如 C/C++、Python、Java 等）。

<!-- more -->

## 编译器安装

### Windows 系统

按照 [清华大学镜像源 msys2](https://mirrors.tuna.tsinghua.edu.cn/help/msys2/) 页面的方法，安装 MSYS2，并且可以根据提示配置相应的镜像源。**注意：安装过程中需要保证通畅的网络。**

{% asset_img 16308512143077.jpg %}

打开`C:\msys64\msys2_shell.cmd`，执行`pacman -Syu`

{% asset_img 16308525279806.jpg %}

重新打开`C:\msys64\msys2_shell.cmd`，输入`pacman -Su`，过程同上。

{% asset_img 16308526276557.jpg %}

再次执行`pacman -S --needed base-devel mingw-w64-x86_64-toolchain`，中途遇到提示直接全部按回车即可，耐心等待安装完成。

#### 环境变量配置

打开**高级系统设置**，点击**环境变量**

{% asset_img 16308516376436.jpg %}

{% asset_img 16308516645060.jpg %}

在`Path`变量中新建一项，设置为`C:\msys64\mingw64\bin`(如果修改过安装路径请对应修改一下)

{% asset_img 16308517461734.jpg %}

### macOS 系统

打开**终端**，输入`clang --version`，如果能够显示如下信息则无需操作。

{% asset_img 16308545298009.jpg %}

如果没有安装，输入`xcode-select --install`安装**Clang**编译器。

### Linux 系统

一般而言，Linux 系统是自带了 gcc 环境的，如未安装，可以手动安装 gcc、g++、gdb 等工具。

## VSCode 安装及配置

### VSCode 安装

打开 [VSCode 官网](https://code.visualstudio.com/)，下载安装即可。

### VSCode 插件安装

{% asset_img 16308503645361.jpg %}

打开 VSCode 后，点击**扩展**(**Extensions**)图标，依次安装 [C/C++ 扩展](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools) 、 [Code Runner](https://marketplace.visualstudio.com/items?itemName=formulahendry.code-runner) 扩展。如果看英文不顺眼的话，可以另外安装 [Chinese (Simplified) Language Pack for Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans) 中文语言包。

### VSCode 配置

#### 使用 Code Runner 插件（无法调试）

打开设置面板，找到**Run In Terminal**选项，将其打上勾（不开启将无法输入数据）。

{% asset_img 16308504905915.jpg %}

输入以下代码，保存为`hello.cpp`。

```cpp
#include <cstdio>

int main() {
    printf("Hello, world!\n");
    return 0;
}
```

点击右上角类似播放器的按钮，如果看到下方显示`Hello, world!`则表示安装成功。

{% asset_img 16429114514875.jpg %}

#### 使用 VSCode 对 C++ 程序进行调试

打开项目目录，点击**Run and Debug**选项卡，点击**Run and Debug**按钮。出现上方菜单选择**C++(GDB/LLDB)**，即使用 GDB/LLDB 工具链进行调试。

{% asset_img 16429124914878.jpg %}

在菜单中选择 `g++` 即可，如果你使用的是 mac，可以选择`clang++`。

{% asset_img 16429125670204.jpg %}

随后会出现一份配置文件，如果没有个性化需求可以直接关闭该配置。

{% asset_img 16429126495795.jpg %}

运行程序可以直接点击上方的调试按钮（<kbd>F5</kbd>），当然在此之前你可以在代码上打断点。

{% asset_img 16429128213147.jpg %}

**注意**：~~使用 Apple Silicon 芯片的 mac 用户截至 2022 年 1 月需要通过 [CodeLLDB](https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb) 插件进行调试，具体配置见插件页面。~~

**2022 年 3 月 24 日更**：根据 [ISSUE 6779](https://github.com/microsoft/vscode-cpptools/issues/6779) ，目前官方插件已支持 ARM 架构 mac，有兴趣的同学可以试试。
