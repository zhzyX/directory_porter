# directory_porter

一个基于 PyQt5 的 Windows 简易文件夹迁移小工具.

当某些硬盘出现空间紧张而又不能轻易卸载软件时, 可以使用这个小工具来迁移文件夹.

这个工具利用了软链接, 工作原理是将文件夹移动到另一个磁盘, 并在原地创建一个指向另一磁盘对应位置的软链接, 这样就能避免程序或快捷方式发生目标丢失.

## 如何使用

### 依赖:

请确保安装了 Python 及 PyQt5 (5.6 及以上版本), 你可以通过安装 Anaconda 5.1.0 或更新的版本来创建这个环境.

### 使用方式:

在控制台中切换至应用程序目录, 输入 `pythonw directory_porter_main.py` 来启动程序.

你也可以执行命令 `echo 'start pythonw directory_porter_main.py' > exec.bat` 来在程序目录下创建一个 `exec.bat`, 接下来你将能够通过双击这一文件来调用程序.

## 参考

[基于 PyQt 的文件夹迁移工具](http://zhzyx.me/2018/09/%E5%9F%BA%E4%BA%8E-PyQt-%E7%9A%84%E6%96%87%E4%BB%B6%E5%A4%B9%E8%BF%81%E7%A7%BB%E5%B7%A5%E5%85%B7/), 在这篇文章中, 我详细介绍了我的开发过程和思路, 仅供参考.
