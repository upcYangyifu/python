#1、集合
#集合数据类型是没有顺序的简单对象的聚集，且元素不重复，包括可变集合对象和不可变集合对象（set/frozenset）
#1、1集合的定义
#可变集合set 通过花括号中用逗号分隔的项目定义：{x1,x2,x3,x4}
#所有内置不可变对象（bool,int,float,complex,str,tuple,frozenset）都是可hash对象
#所有内置可变对象都是非hash对象（list,dict,set）
#集合中可以包含内置不可变对象，不能包含内置可变对象
#用set（）创建空集
# print(set())
# print({1,1,2})
# print(set('hello'))
#1、2判断集合元素是否存在
# x in s
# x not in s
# s=set('hello')
# print('o' in s)
#1、3集合的运算：并集，交集，差集，对称差集
# s1=set('123')
# s2=set('234')
# print(s1|s2)
# print(s1&s2)
# print(s1-s2)
# print(s1^s2)
#集合的对象方法，查阅文档
#1、4集合的比较运算：相等，子集，超集
# s1=set('123')
# s2=set('21')
# print(s1==s2)
# print(s1!=s2)
# print(s1>s2)
#1、5集合的长度，最大值，最小值，元素和
# s1={1,2,3}
# print(len(s1))
# print(max(s1))
# print(min(s1))
# print(sum(s1))
#1、7可变集合的方法：查阅文档
