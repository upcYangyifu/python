#1、栈和队列
#1.1 栈的实现：使用列表（向列表最后位置添加和移除元素非常高效）
# class Stack:
#     def __init__(self,size=16):
#         self.stack=[]
#     def push(self,obj):
#         self.stack.append(obj)
#     def pop(self):
#         try:
#             return self.stack.pop()
#         except IndexError as e:
#             print("stack is empty")
#     def __str__(self):
#         return str(self.stack)
# def main():
#     stack=Stack()
#     stack.push(1)
#     stack.push(2)
#     print(stack)
#     stack.pop()
#     stack.pop()
#     stack.pop()
# main()

#1.2depue对象
#collections.deque支持从任意一端增加和删除元素，两段追加和弹出都非常快
#构造函数： deque([iterable[,maxlen]])
#deque对象dq支持下列方法：
# dq.append(x)  ——右端添加元素x
# dq.appendleft(x) ——左端添加元素
# dq.pop()  ——右端弹出
# dq.popleft()——左端弹出
# dq.extend(iterable)——右端添加系列iterable中的元素
# dq.extendleft(x)  ——左端
# dq.remove(value)——移除第一个找到的元素
# dq.count(x) ——返回元素x在队列中出现的个数
# dq.clear()  ————删除所有元素
# dq.reverse()  ——反转队列中的所有元素
# dq.rotate(n)————所有元素右移n个位置

# import collections
# def tail(filename,n=10):
#     'return the last n lines of a file'
#     with open(filename,'rb') as f:  #课本实例中缺少rb
#         return collections.deque(f,n)
# if __name__=='__main__':
#     path=r'chapter11.3.py'
#     dq=tail(path,n=2)
#     print(dq.popleft())
#     print(dq.popleft())

#1.3 deque 作为栈
# from collections import *
# dq =deque()
# dq.append(1);dq.append(2);dq.append(3)
# print(dq.pop(),dq.pop(),dq.pop())

#1.4 deque作为队列
# from collections import *
# dq =deque()
# dq.append(1);dq.append(2);dq.append(3)
# print(dq.popleft(),dq.popleft(),dq.popleft())

