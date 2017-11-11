#第十一章 算法与数据结构基础
#11.1 算法及其性能分析
#11.1.1 算法概述
#算法性质：输入数据、输出结果、确定性、有限性
#算法性能分析：时间性能、空间性能
#11.1.2 算法的时间复杂度分析：每条语句的执行时间*每条语句的执行次数
#11.13增长量级 O（1/log2n/n/nlog2n/n2/n3）
#11.1.4算法的空间复杂度分析
# import sys
# print(sys.getsizeof(1010))#可以获得1010在系统中占用的字节数

#11.2 查找算法
#11.2.1 顺序查找法
# def sequentialsearch(alist,item):       #在列表中顺序查找特定值x
#     pos=0
#     found=False
#     while pos<len(alist) and not found:
#         if alist[pos]==item:
#             found=True
#         else:
#             pos+=1
#     return found
# def main():
#     testlist=[1,3,33,8,37,29,32,15,5]
#     print(sequentialsearch(testlist,3))
#     print(sequentialsearch(testlist,13))
# if __name__=='__main__':
#     main()

# def max1(alist):                #在列表中顺序查找最大值和最小值
#     pos=0
#     iMax=alist[0]
#     while pos<len(alist):
#         if alist[pos]>iMax:
#             iMax=alist[pos]
#         pos+=1
#     return iMax
# def min1(alist):
#     iMin=alist[0]
#     for item in alist:
#         if item<iMin:
#             iMin=item
#     return iMin
# def main():
#     testlist=[1,3,33,8,37,29,32,15,5]
#     print(max1(testlist))
#     print(min1(testlist))
# if __name__=='__main__':
#     main()

#11.2.2 二分查找法
# def _binarySearch(key,a,lo,hi):            #二分查找法的递归实现
#     if hi<=lo:return -1
#     mid=(lo+hi)//2
#     if a[mid]>key:
#         return _binarySearch(key,a,lo,mid)
#     elif a[mid]<key:
#         return _binarySearch(key,a,mid+1,hi)
#     else:
#         return mid
# def binarySearch(key,a):
#     return _binarySearch(key,a,0,len(a))
# def main():
#     a=[1,2,3,4,5,6,7,8,9]
#     print(binarySearch(3,a))
#     print(binarySearch(0,a))
# if __name__=='__main__':
#     main()

# def binarySearch(key,a):  #二分查找法的非递归实现
#     low=0
#     high=len(a)-1
#     while low<=high:
#         mid=(low+high)//2
#         if a[mid]<key:
#             low=mid+1
#         elif a[mid]>key:
#             high=mid-1
#         else:
#             return mid
#     return -1
#
# def main():
#     a=[1,2,3,4,5,6,7,8,9]
#     print(binarySearch(3,a))
#     print(binarySearch(0,a))
# if __name__=='__main__':
#     main()
#python语言提供的查找算法
#1.运算符 in ”x in alist“ 测试x是否在alist内
#2. 内置函数max min 查找列表的最大值最小值
