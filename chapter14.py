# 1.数值处理相关模块：
# numbers模块：数值抽象类
# math模块：数学函数
# cmath模块：复数运算数学函数
# decimal模块：高精度数值运算
# fractions模块：分数运算
# random模块：随机数
# 2.数值运算模块NumPy
# 3.科学计算模块SciPy
# datetime模块：日期和时间的处理
# calendar：处理日历的函数和类
# time模块：处理时间的函数

#2math模块和数学函数
#查阅文档

#3.camth模块和复数数学函数
#查阅文档

# #4.random模块和随机函数
# #种子和随机状态
# import random
# random.seed(1)
# for i in range(5):print(random.randint(1,5),end=',')
# for i in range(5):print(random.randint(1,5),end=',')
# random.seed(1)      #种子重新设置为1 ，接下来的两个输出同上一次一样
# for i in range(5):print(random.randint(1,5),end=',')
# for i in range(5):print(random.randint(1,5),end=',')
# random.seed(10)     #种子设置为10 ，输出结果改变
# for i in range(5):print(random.randint(1,5),end=',')
# for i in range(5):print(random.randint(1,5),end=',')
# #随机系列--输出系列中的数但是不会重复
# seq=[1,2,3,4,5]
# print(random.sample(seq,3))

#5.数值运算模块NumPy
#需要安装Numpy模块
#创建数组的方式：
#1.array函数，把序列转换为数组
# a=np.array([1,2,3])
#2.通过arange，linspace，logspace创建数组
# arange（开始值，终值，步长）
# linspace（开始值，终值，元素个数）
# logspace（开始值，终值，元素个数）--用于创建等比数列
#处理数组
#假设y为数组；y+1可以表示将数组中的每个元素加1


#6.日期和时间处理
#epoch（新纪元）：系统规定的起始时间点
#使用time模块的gettime函数可以获取当前系统的起始点
# import time
# print(time.gmtime(0))
#UTC 协调世界时
#DST 夏令时

#时间 对象
# import time
# st=time.gmtime()
# print(st.tm_year)#获取当前的年份

#测量程序运行时间
#process_time():返回当前进程处理器运行时间
#perf_counter():返回性能计数器
#monotonic():返回单向时钟
# import time
# def test():
#     sum=0
#     for i in range(0,999999):
#         sum+=i
#     return sum
#
# if __name__=='__main__':
#     t1=time.monotonic()
#     print(test())
#     t2=time.monotonic()
#     print(t2-t1)    #运行时间

#日期对象
#datetime包含两个常量：datetime.MINYEAR和datetime.MAXYEAR分别表示最小和最大年份
# import datetime
# print(datetime.date.today())#输出当前日期
# print(datetime.datetime.now())#输出当前时间

#获取当前日期时间
# import datetime
# dt=datetime.datetime.now()
# print(dt.year)#还可以用这种方法获取month，day，hour,minute,second

#日期时间格式化为字符串
# from time import *      #和import time是有区别的
# print(strftime("%c",localtime()))#Fri Nov 17 18:16:39 2017

# import datetime
# print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))#2017-11-17 Nov:18:31字母固定就是这几个

#日期字符串解析为日期时间对象
# import datetime
# print(datetime.datetime.strptime('2017-08-18','%Y-%m-%d'))









