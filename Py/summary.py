#!/usr/bin/python
# -*- coding=utf-8 -*-

####基础
#编码：utf-8
#标识符
#保留字
#注释：#或者三引号
#行与缩进：tab或者4空格（推荐）
#多行语句：“\”
#数字类型：int、bool、float、complex
#字符串
#空行
#输入
#同一行显示多条语句：“;”
#多个语句构成代码组
#print输出
#import和from …… import
#命令行参数

####基本数据类型
#多变量赋值
#数值
#字符串
#列表:[]
#元祖:()
#集合:{}
#字典:{key:value}

####解释器
#交互式编程
#脚本式编程

####运算符
#算术运算符
#比较（关系）运算符
#赋值运算符
#逻辑运算符：and、or、not
#位运算符
#成员运算符：in 和 not in
#身份运算符：is 和 is not
#运算符优先级

####条件控制
# if…elif…else

####循环语句
#while…else
#for…else
#break、continue、pass
#range()

####迭代器
#iter()和next()
#__iter__()和__next__()
#StopIteration

####生成器：返回迭代器的函数
#yield


####函数
#语法
#函数调用
#参数传递：分为可变对象（list、dict）和不可变对象（string、tuples、numbers）
#参数：必需参数、关键字参数、默认参数、不定长参数
#匿名函数： lambda x,y:x+y
#return语句

####高级函数
#回调函数：又称函数回调，将函数作为参数传入另一个函数中
#函数的递归和嵌套


#闭包：函数作为返回值，延长变量的作用时间和作用域;
#    一个函数定义引用函数外定义的变量，并且该函数可以在其定义环境外被执行
#    闭包函数中引用的父函数中local variable既不具有C++中全局变量的性质，也没有static变量行为
#    函数外的变量为闭包函数（内部函数）的一个自由变量
#    一个闭包实例对其自由变量的修改会传递到下一次该闭包实例的调用
#    同一闭包的不同实例中引用的自由变量相互没有影响
#    返回闭包中不要引用任何循环变量，或者后续会发生变化的变量，正确的做法是将父函数的local variable赋值给函数的形参
#    返回的函数中没有引用父函数中定义的local variable，返回的函数不是闭包函数
#    应用：记录闭包函数被调用的信息，以及闭包函数的一些计算结果中间值
#    装饰器


#yield


####数据结构
#列表：可变，字符串和元祖不能
#将列表当做“堆栈”使用：后进先出
#将列表当做“队列”使用：先进先出
#列表推导式：[3*x for x in [2,4,6]]
#嵌套列表解析：[[row[i] for row in matrix] for i in range(4)]
#del语句
#元祖和序列
#集合
#字典
#遍历技巧：item()、enumerate()、zip()


####模块
#.py文件：sys.argv 命令行输入参数
#import语句
#from…import 从模块中导入一个指定的部分到当前命名空间
#深入模块
#__name__=='__main__'
#dir()函数
#标准模块
#包：管理python模块命名空间，__init__.py
#from package import * 导入的是 __init__.py 文件中 __all__列表中的模块


####输入和输出
#输出格式美化：str()、repr()
#.format()
#旧式字符串格式化
#读取键盘输入
#读和写文件
#文件对象的方法
#pickle模块

####File
# open(file,mode='r',buffering=-1,encoding=None,errors=None,newline=None,closefd=True,opener=None)

####通用模块
# os sys

####错误和异常
#语法错误
#异常
#异常处理
# try…except…else…finally…
# raise
#自定义异常
#定义清理行为
#预定义的清理行为

####面向对象
#类：相同的属性（变量）和方法（函数），对象是类的实例
#方法：类中的函数
#类变量：定义在类中且在函数体之外，公用的，不作为实例变量使用
#数据成员：类变量或实例变量用于处理类及其实例对象的相关的数据
#方法重写：对继承父类的方法，覆盖或者重写
#局部变脸：定义在方法中的变量，只作用于当前实例的类
#实例变量：是用self修饰的变量
#继承
#实例化：创建类的一个实例，类的具体对象
#对象：通过类定义的数据结构实例，包含两个数据成员（类变量和实例变量）和方法


####类和对象
#类的定义
#类对象：属性引用和实例化
#__init__()，构造方法，实例化时自动调用
#self代表类的实例，而非类；是类的方法和普通函数的一个特别区别，self作为第一个参数名，self不是关键字，可以使用其他如runoob替换
#类的方法
#继承
#多继承
#方法重写
#类属性和方法：私有属性和方法
#类的专有方法：构造函数、析构函数等等


####命名空间和作用域
#内置名称、全局名称、局部名称，查找顺序从后到前
#作用域：Local-->Enclosing（閉包）-->Global-->Build-in
#Python中只有模块、类、函数才会引入新的作用域
#全局变量和局部变量
#global和nonlocal，当内部作用域修改外部作用域的变量时


####标准库概览
#操作系统接口 os
#文件通配符 glob
#命令行参数 sys.argv
#错误输出重定向和程序终止 sys.stderr.write
#字符串正则匹配 re
#数学 math
#访问互联网 urllib
#日期和时间 datetime
#数据压缩 zlib
#性能度量 timeit
#测试模块



###############################
##########高级应用##############
###############################


####正则表达式
#re.match(pattern,string,flag=0) 从起始位置匹配，返回groups()
#re.search(pattern,string,flag=0) 扫描整个字符串，返回groups()
#re.sub(pattern,repl,string,count=0,flags=0) repl可以是个函数
#compile(pattern)
#re.finditer(pattern,string,flags=0)
#re.findall()
#re.split(pattern,string[,maxsplit=0,flags=0])


#### MySQL连接

#### XML解析

#### json
#json.dumps()
#json.loads()

####日期和函数
#time
#calendar
#datetime

