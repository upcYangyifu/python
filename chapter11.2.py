#1、常用数据结构
#1.1、数据结构概述
#数据结构通常由以下三个部分组成：
#数据的逻辑结构：反应数据元素之间的逻辑关系（线性/树/图/集合）
#数据的物理结构：反应数据的逻辑结构在计算机存储空间的存放形式（顺序/链接/索引/散列）
#数据的运算结构：反应在数据的逻辑结构上定义的方法
#1.2、常用的数据结构：数组、线性表、栈、队列、链表、树、图、堆、散列表
#1.3 python的collections模块——实现了许多常用的数据结构

#2、数组
#2.1 列表和数组：python没有直接提供数组数据类型，通常用列表作为数组
#列表支持数组的4种核心操作：创建数组，索引访问，索引赋值和迭代遍历
#2.2array.array对象和数组
#array模块包含一个array对象，用于实现其他编程语言中的数组数据结构
#array对象的构造函数： array(typecode[,initializer])
# import array
# a=array.array('b',(1,2,3,4,5))
# print(a[1])
# a[1]=22
# print(a[1:])