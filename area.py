import math

a = 3.0
b = 4.0
c = 5.0
h = (a + b + c) / 2
s = math.sqrt(h * (h - a) * (h - b) * (h - c))
print(s)
print('hello')
print(type(a))  # a的类型
print(123 // 12)  # 整除
print(a == b)
print(a is b)  # ==判断两个对象的值是否相同，is判断是否指向同一个对象
# help()#进行交互式查询
# dir(__builtins__)#可以显示内置函数
# python支持链式赋值  变量1=变量2=表达式
x = 1
del x  # 删除变量

a, b = 1, 2  # 系列变量赋值
a, b = b, a  # 优雅的实现a，b的制的互换
print(a, b)

# print(2**10)#2的10次方

# r=float(input("请输入半径r：")) #python中的输入语句
# print('22') #python 语句前面不能有空格
#a=0;b=0;c=0#python 中分号可以用于在一行书写多条语句

#python中复合语句及其缩进的形式
# sum=0
# for i in range(1,11):
#     sum=sum+i
#     print(i,end=' ')

#生成一个空的代码块
# def do_nothing():
#     pass

