# 第九章 类和对象
# 9.1 面向对象概念——三个基本特征：封装、继承、多态
# 9.2 类对象和实例对象
# class Person1:   #类名的第一个首字母大写
#     pass
# p1=Person1()
# print(p1)
# 9.3 属性
# 9.3.1 实例属性
# class Person2:                     # 实例变量在类的内部通过self访问，在类的外部通过对象实例访问
#     def __init__(self,name,age):   #使用__init__方法初始化
#         self.name=name
#         self.age=age
#     def say_hi(self):
#         print('你好，我叫',self.name)
# p1=Person2('张三',25)
# p1.say_hi()
# print(p1.age)
# 9.3.2 类属性
# class Person3:  #类属性定义：必须赋初值、类名和对象名都可以调用
#     count=0
#     name="Person"
# 9.3.3 私有属性和公有属性
# class A:
#     __name='class A'    #以两个下划线开头，但是不以两个下划线结束的属性是私有的，不能直接访问私有属性
#     def getname():
#         print(A.__name)
# A.getname()
# print(A.__name) #会出现错误
# 9.3.4@property 装饰器
# class Person1:
#     def __init__(self, name):
#         self.__name = name
#
#     @property                                     #用@property 定义访问私有属性的函数
#     def name(self):
#         """"I'm the'x' property"""
#         return self.__name
#
#
# p = Person1('王五')
# print(p.name)
#
# class Personl2:
#     def __init__(self,name):
#         self.__name=name
#     @property
#     def name(self):
#         """"I'm the 'x' property"""
#         return self.__name
#     @name.setter
#     def name(self,value):
#         self.__name=value
#     @name.deleter
#     def name(self):
#         del self.__name
#
# p=Personl2('张三')
# p.name='王一一'
# print(p.name)
# 9.3.5 特殊属性——以双下划线开始和结束的属性
# print(int.__dict__)#对象的属性字典
# print(int.__class__)#对象所属的类
# print(int.__bases__)#类的基类
# print(int.__name__)#类的名称
# print(int.__qualname__)#类的限定名称
# print(int.__mro__)#基类元组
# print(int.__subclasses__())#子类列表
#
# 9.3.6自定义属性
# class C1:
#     pass
# o=C1()
# o.name='sss'  #自定义属性
# print(o.name)
# print(o.__dict__)
#
# 9.4 方法
# 9.4.1 实例方法
# class Personl4:
#     def say_hi(self,name):  #self 指的是调用方法的本身
#         self.name=name
#         print('你好，我叫',self.name)
#
# p4=Personl4()
# p4.say_hi('Alice')
#
# 9.4.2静态方法
# 声明
# @staticmethod       #静态方法不对特定实例进行操作
# def 静态方法名([形参列表]):
#     函数体
# 调用
# 类名.静态方法名([实参列表])
# 9.4.3 类方法
# @classmethod       #静态方法不对特定实例进行操作
# def 静态方法名(cla,[形参列表]):
#     函数体
# 调用
# 类名.静态方法名([实参列表])
# 9.4.4 __init__方法和__new__方法
# __new__   创建对象时调用，无需显式调用
# __init__ 执行类的初始化工作
# 9.4.5 __del__ 方法(析构函数) 用来销毁对象
# 9.4.6 私有方法与公有方法
# 与私有属性类似，以两个下划线开始但不以两个下划线结束的方法为私有方法，其他为公有方法
# def __check_name(self):
#     函数体
# 9.4.7方法重载 python对象方法不需要重载既可以实现重载功能(python是动态语言)
# class Person21:
#     def say_hi(self,name=None):
#         self.name=name
#         if name==None:print('你好！')
#         else:print('你好！',self.name)
#
# p=Person21()
# p.say_hi()
# p.say_hi('威尔逊')
#
# 9.5继承
# class 派生类名(基类1,[基类2]):         #如果没有指定基类，则其默认为object
#     类体                               #必须在构造函数中声明基类的构造函数  基类名.__init__(self,参数列表)
# 派生类继承基类中除构造方法之外的所有成员
#
# 9.6对象的特殊方法
# 9.6.1 对象的特殊方法概述
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __str__(self):
#         return '{0},{1}'.format(self.name,self.age)
# p=Person('张三',23)
# print(p)
# 9.6.2 运算符重载与对象的特殊方法
# class MyList:
#     def __init__(self, *args):
#         self.__mylist = []
#         for arg in args:
#             self.__mylist.append(arg)
#
#     def __add__(self, n):
#         for i in range(0, len(self.__mylist)):
#             self.__mylist[i] += n
#
#     def __sub__(self, n):
#         for i in range(0, len(self.__mylist)):
#             self.__mylist[i] -= n
#
#     def __mul__(self, n):
#         for i in range(0, len(self.__mylist)):
#             self.__mylist[i] *= n
#
#     def __truediv__(self, n):
#         for i in range(0, len(self.__mylist)):
#             self.__mylist[i] /= n
#
#     def __len__(self):
#         return (len(self.__mylist))
#
#     def __repr__(self):
#         str1 = ''
#         for i in range(0, len(self.__mylist)):
#             str1 += str(self.__mylist[i]) + ' '
#         return str1
# m = MyList(1, 2, 3, 4, 5)
# m + 2;print(repr(m))
# m - 1;print(repr(m))
# m * 4;print(repr(m))
# m / 2;print(repr(m))
# print(len(m))
# 9.6.3 @functools.total_ordering装饰器
# import functools
# @functools.total_ordering
# class Student:
#     def __init__(self,firstname,lastname):
#         self.firstname = firstname
#         self.lastname = lastname
#     def __eq__(self, other):
#         return ((self.lastname.lower(),self.firstname.lower())==(other.lastname.lower(),other.firstname.lower()))
#     def __lt__(self, other):
#         return ((self.lastname.lower(), self.firstname.lower())<(other.lastname.lower(), other.firstname.lower()))
# if __name__=='__main__':
#     s1=Student('Mary','Clinton')
#     s2 = Student('Mary', 'Clinton')
#     s3 = Student('Mawry', 'Clinton')
#     print(s1==s2)
#     print(s1>s3)
# 9.6.4__call__方法和可调用对象 定义了call方法的对象成为可调用对象，该对象可以像函数一样被调用
# class GDistance:
#     def __init__(self, g):
#         self.g = g
#
#     def __call__(self, t):
#         return (self.g * t ** 2) / 2
#
#
# if __name__ == '__main__':  # *****还没搞明白这句话
#     e_gdist = GDistance(9.8)
#     for t in range(11):
#         print(format(e_gdist(t), "0.2f"), end=' ')
#
# 9.7 对象的引用，浅拷贝、和深拷贝
# 9.7.1 对象的引用
# acc10=['Charlie',['credit',0.0]]
# acc11=acc10
# print(id(acc10))
# print(id(acc11)) #id返回值保持一致
# 9.7.2 对象的浅拷贝——拷贝对象时，对象中包含的子对象并不拷贝，而是引用同一个子对象
# import copy
# acc1=['Charlie',['credit',0.0]]
# acc2=acc1[:]            #切片式拷贝
# acc3=list(acc1)         #对象实例化
# acc4=copy.copy(acc1)    #copy模块的copy函数。各个对象的id不一样
# 9.7.3 对象的深层拷贝——子对象也要变化
# import copy
# acc1=['Charlie',['credit',0.0]]
# acc4=copy.deepcopy(acc1)