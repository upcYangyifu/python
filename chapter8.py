# 第八章 函数
#8.1python 函数概述
#函数分类 内置函数、标准库函数、第三方库函数、用户自定义函数

#8.2 函数的声明和调用
# def print_star(n):          #打印“*”
#     print(("*"*n).center(50))
# lines=int(input("Lines:"))
# for i in range(1,2*lines,2):
#     print_star(i)
#8.2.3 作为对象的函数
# def computer(f,s):
#     return f(s)
# print(computer(min,(1,5,3,2)))
# print(computer(max,(1,5,3,2)))
#8.2.4 lamda表达式和匿名函数
# f=lambda x,y:x+y  #在同一行中定义函数 冒号后面为返回值
# type(f)
# print(f(12,34))

# for i in filter(lambda x:x>0,[1,0,-2,8,5]):    #输出列表中大于零的数
#     print(i)

#8.3 参数的传递
#8.3.2 python参数传递方法是传递对象引用，而不是传递对象的值
#8.3.3 传递不可变对象的引用——函数体内修改不可变对象的值是无法传出来的
# i=100
# def inc(j,n):
#     j+=n
# inc(i,10)
# print(i)  #输出的i还是100

# i=100
# def inc(j,n):
#     j+=n
#     return j
# i=inc(i,10)
# print(i)    #输出的i是110

#8.3.4 传递可变对象的引用--可以直接修改对象的值，例如list对象
#8.3.5 可选参数--为函数指定默认值
#8.3.6 位置参数和命名参数——实参默认按位置顺序传入，也可以通过名称指定
# def my_sum(mid,end,midrate=0.4):
#     score=mid*midrate+end*(1-midrate)
#     print(format(score,'.2f'))
# print(my_sum(88,79))
# print(my_sum(mid=88,end=79))
# print(my_sum(end=79,mid=88))  #三种方式输出的结果一样

#8.3.7 可变参数 “*”——被收集为一个元组  “**”——被收集为一个字典
# def my_sum3(a,b,*c):
#     total=a+b
#     for n in c:
#         total=total+n
#     return total
# print(my_sum3(1,2))
# print(my_sum3(1,2,3,4,5))
# print(my_sum3(1,2,3,4,5,6,7))

#8.3.8 强制命名参数 在“*”后面声明参数，在调用时必须使用参数名传递值
# def my_sum(*,mid,end,midr=0.4):
#     score=mid*midr+end*(1-midr)
#     print(format(score,'.2f'))
# print(my_sum(mid=88,end=79))
# print(my_sum(88,79))      #报错，必须显示使用命名参数传递值

#8.4 函数的返回值
#8.4.1 return语句和函数返回值
# def my_max(a,b,*c):                   #求若干数中的最大值
#     max_value=a
#     if max_value<b:
#         max_value=b
#     for n in c:
#         if max_value<n:
#             max_value=n
#     return max_value
# print(my_max(1,2))
# print(my_max(1,2,3,4,5,6,7))

#8.4.2 多条return语句
# def is_prime(n):                     #判断是不是素数
#     if n<2:return False
#     i=2
#     while i*i<=n:
#         if(n%i==0):return False
#         i+=1
#     return True
# for i in range(100):                    #输出小于100的素数
#     if is_prime(i):print(i,end=' ')

#8.4.3 返回多个值
# import random                       #输出一串随机数
# def randomarray(n):
#     a=[]
#     for i in range(n):
#         a.append(random.random())
#     return a
# b=randomarray(5)
# for i in b:print(i)

#8.5 变量的作用域  全局变量，局部变量和类型成员变量
#8.5.1 全局变量
#8.5.2 局部变量
#8.5.3 全局语句global
# m=100
# n=200
# def f():
#     global n                    #使用global在函数体中引用全局变量
#     print(m+90)
#     n+=10
# f()
# print(n)
#8.5.4 非局部语句nonlocal ——为定义在上级函数体中的局部变量赋值
# def out_f():
#     tax=0.17
#     print('out_f tax=',tax)
#     def inner_f():
#         nonlocal tax
#         tax=0.05
#         print('inner tax=',tax)
#     inner_f()
#     print('out_f tax=',tax)
# out_f()
#8.5.5 类成员变量
#8.5.6 输出局部变量和全局变量 ——使用内置函数globals（）和locals（）
# a=1
# b=2
# def f(a,b):
#     x='abc'
#     y='xyz'
#     for i in range(2):
#         j=i
#         k=i**2
#         print(locals())
# f(1,2)
# print(globals())

#8.6递归函数
# def factorial(n):
#     if n==1:return 1
#     return n*factorial(n-1)
# for i in range(1,10):
#     print(factorial(i))

# import sys
# print(sys.getrecursionlimit())
# sys.getrecursionlimit()           #获取和设置递归最大深度
# sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())

# def gcd(p,q):       #求最大公约数（）欧几里得算法
#     if(q==0):return p
#     return gcd(q,p%q)
# print(gcd(100,88))

# def hanoi(n,a,b,c):         #汉诺塔问题
#     if n==1:print(a,'->',c)
#     else:
#         hanoi(n-1,a,c,b)
#         hanoi(1,a,b,c)
#         hanoi(n-1,b,a,c)

#8.7 内置函数
