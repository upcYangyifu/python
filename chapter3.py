#第三章 程序流程控制
#1 顺序结构
#2 选择结构
#条件表达式的python评价方法：如果表达式的结果为;数值类型（0），空字符串（""）,空元组(()),空列表（[]）,空字典（{}）。
#则其布尔值为false，否则为true
a=0;b=0
print(str.format("{0},{1}",a,b))# 可以使用str.format()控制输出格式
#python提供下列表达式来等价于其他语言的三元条件表达式：
#条件为真时的值 if （条件表达式） else条件为真实的值。例如： y=x if(x>=0) else 0   如果下>=0则y=x,否则y=0
#多分支结构 if elif else

#使用calendar模块的isleap函数可以判断是否是闰年
import calendar
y=2000
if(calendar.isleap(y)):print("isleap")
else:print("is not leap")

#range对象 range(start,stop[,step]) 从start开始到stop结束，可选择步长step

#循环结构
# for i in range(1,10):
#     s=""
#     for j in range(1,10):
#         s+=str.format("{0:1}*{1:1}={2:<2} ",i,j,i*j)#冒号限定宽度
#     print(s)

#else子句：
#for，while可以附带一个else子句，如果for，while子句没有被break终止，则执行else子句，否则不执行。



