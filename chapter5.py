#第五章 系列数据类型
#5.1 python系列数据概述
#a 数组
#b python内置的系列数据类型 元组tuple 列表list 字符串str 字节数据bytes bytearray
#其中，元组用小括号，列表用中括号
s1=(1,2,3)
print(s1[2])
s2=[1,2,3]
s2[2]=4
print(s2[2])#列表用于存储值可变的表

s1=b"abc"
print(s1.decode("utf-8"))

#5.2 系列数据的基本操作
# len(),max(),min()可以分别求长度，最大值最小值
#系列的切片操作s[i:j:k] i，j，k分别表示开始位置，结束位置，步长
#系列连接和重复操作 + * s1+s2 s1*n
#系列的成员关系操作
# x in s 返回bool值
# x not in s 返回bool值
# s.count(x)  返回x在s中出现的次数
# s.index(x,i,j) 返回x在[i,j)第一次出现的下标，范围可以省略
#系列的比较运算操作 == > <
#系列的排序操作 sorted(iterable,key=None,reverse=false) reverse=True 则反向排序
#内置函数 all() 所有值为true返回true,any()任意值为true返回true
#系列拆封 类似于集体赋值
a,b=(1,2)
print(a,b)
first,*middle,last=range(10)
print(middle)
record=('zhangsan','zhangsan@.com','021-12222220,','17854255105')
name,_,*phones=record
print(phones)

#5.3元组 tuple
t3=1,
print(t3)#元组只有一个项目时，后面的逗号不能省略

#5.4 列表
#列表的系列操作 s[下标]=x del s[下标]
#list对象的方法 append() clear() copy() extend() insert() pop() remove() reverse() sort()
#列表解析表达式
print([i**2 for i in range(10)])

#5.5 字符串
#字符串编码解码 decode encode
#字符串格式化 format

# 5.6 字节系列
#bytes 常量 使用字母b 加单引号或双引号括起来的常量
bytes((1,2,3))
bytearray((1,2,3))

