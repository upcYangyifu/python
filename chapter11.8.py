#1、字典
#1、1字典（dict或映射）是一组键/值对的数据结构，根据键可以查询到值
#字典的键必须是可hash的对象，而值都可
print(hash(100))
print(hash(1.23))
#1、2字典的定义
# {键1：值1，键2：值2.,,,,,,}
s={'a':'apple','b':'boy'}
print(s)
#1、3字典的访问操作
d={1:'food',2:'drink'}#初始化
print(d[1])
d[3]='fruit'#添加
print(d)
del d[2]#删除
print(d)
#1、4字典的视图对象
d={1:'food',2:'water',3:'fruit'}
print(d.keys()) #输出key的列表
print(d.values())   #输出value的值
print(d.items())    #输出（key，value）对
#1、5判断字典键是否存在
#key in d
#key not in d
#1、6字典对象的长度和比较
d1={1:'food',2:'water',3:'fruit'}
d2={1:'food',2:'water',3:'fruit'}
print(len(d1))
print(d1==d2)
#1、7字典对象的方法（查阅文档）
# iter(d)
# clear()
# copy()
# fromkeys()
# get(key[, default])
# items()
# keys()
# pop(key[, default])
# popitem()
# setdefault(key[, default])
# update([other])
# values()
#1、8 defaultdict对象
#可以指定键/值对应的类型
#实现了键不存在时返回值的类型
# dd={}
# s=[('r',1),('g',2),('b',3)]
# dd.setdefault(int,s)
# print(dd)
# print(dd['b'])
# print(dd['w'])
#1、9orderdict对象——能记录字典元素的插入顺序
#ordereddict保持插入的顺序，更新键的值时，不改变顺序，删除项在插入时置于末尾
#还有两个新增的方法：
# popitem(last=true):弹出最后一个元素
# move_to_end(key,last=True):移动key到最后
from collections import *
d={'banana':3,'apple':4,'pear':1,'orange':2}
print(d.items())
sorted(d.items())
od=OrderedDict(sorted(d.items()))
print(od)
od.popitem()
#1、10ChainMap对象
#collections.ChainMap对象可用于连接多个map，构造函数为ChainMap（*maps）
#chainmap对象m包含下列属性和方法
# m.maps :返回m包含的map的列表
# m.parents 返回包含其父map的新的chainmap对象
# m.new_child():返回新的chainmap对象
from collections import *
m1={'a':1,'b':2,}
m2={'a':2,'x':3,'y':4}
m=ChainMap(m1,m2)
print(m.maps)
print(m.parents)
print(m.new_child())
print(m['a'])
print(m['x'])
m['a']=99
m['x']=10
print(m)
#1、8Counter对象
# collections.Counter用于统计各元素的计数，结果为map
from collections import *
c1=Counter()    #创建空的counter对象
c2=Counter('banana')    #基于系列创建counter对象
c3=Counter({'red':4,'blue':2})  #基于字典创建counter对象
c4=Counter(cats=4,dogs=8)   #基于命名参数创建counter对象
#counter对象c还包含下列属性和方法
# c.elements():返回元素列表，多元素重复的次数为其计数
# c.most_common([n])：返回数值最大的n个元素的元组列表
# c.subtact();元素的计数值减去系列或字典中元素的计数值
from collections import *
c=Counter({'r':3,'g':2,'b':1,'y':4,'w':3})
print(c.elements())
print(list(c.elements())) #['r', 'r', 'r', 'g', 'g', 'b', 'y', 'y', 'y', 'y', 'w', 'w', 'w']
print(c.most_common(2))
print(c.subtract('red'));
print(c)

#统计文本文件中单词频率
import collections,re
path=r'D:\Program File\PyCharm\python\chapter11.8.py'
with open(path,encoding='utf8') as f:
    words=re.findall(r'\w+',f.read().lower())
    c=collections.Counter(words)
    print(c.most_common(5))

#2、collections模块的其他数据结构
#2、1 namedtuple对象
from collections import *
p=namedtuple('point',['x','y'])
print(p._source)    #打印类的代码
print(p._fields) #打印类的字段属性('x', 'y')
p.x=11;p.y=22
print(p.x+p.y) #33

from collections import *
p=namedtuple('point',['x','y'])
t=[3,4]
p1=p._make(t)   #从指定系列构建命名对象point(x=3, y=4)
print(p1)
print(p1._asdict())      #把命名元组对象转换为OrderedDict对象OrderedDict([('x', 3), ('y', 4)])
print(p1._replace(x=30))    #创建新的命名元组，替换指定字段point(x=30, y=4)
#2、2UserDict、UserList、UserString
from collections import *
us=UserString('abc')
print(us.data)  #UserDict、UserList、UserString存在属性data，用于存放内容