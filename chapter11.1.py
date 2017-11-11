#第十一章 算法与数据结构基础——排序算法
#11.3.1 冒泡排序法
#1、从第一个元素开始，相邻两个元素进行比较若不满足升序关系则交换，最大的会跑到表的最后
#2、第二轮，对前n-1个元素进行两两比较，倒数第二大跑到倒数第二位置
#3、n-1轮以后，所有元素按升序排序
# def bubbleSort(a):
#     for i in range(len(a),-1,-1):           #range各种用法可以查文档
#         for j in range(i):
#             if a[j]>a[j+1]:
#                 a[j],a[j+1]=a[j+1],a[j]

#11.3.2选择排序法
#1、从n个元素中寻找最小值与列表的第一个元素交换
#2、从剩下的n-1个元素寻找最小值与第二个元素交换
#3、重复以上步骤
# def selectionSort(a):
#     for i in range(0,len(a)):
#         m=i
#         for j in range(i+1,len(a)):
#             if a[j]<a[m]:
#                 m=j
#         a[i],a[m]=a[m]=a[i]

#11.3.3插入排序法
#1、第二个元素与列表中第一个元素比较若A[0]>A[1]交换位置
#2、第三个元素与其左侧的元素比较，插入到相应的位置
#3、进行第n-1轮以后，所有元素按升序排序
# def insertSort(a):
#     for i in range(1,len(a)):
#         j=i
#         while (j>0) and (a[j]<a[j-1]):
#             a[j],a[j-1]=a[j-1],a[j]
#             j -=1

#11.3.4 归并排序法
#1、将包含n个元素的列表分成两个n/2元素的子列表
#2、对两个子列表递归调用归并排序
#3、合并两个已排序好的子列表
# def merge(left,right):          #合并两个列表
#     merged=[]
#     i,j=0,0
#     left_len,right_len=len(left),len(right)
#     while i<left_len and j<right_len:
#         if left[i]<=right[j]:
#             merged.append(left[i])
#             i+=1
#         else:
#             merged.append(right[j])
#             j+=1
#     merged.extend(left[i:])     #归并做子列表剩余元素
#     merged.extend(right[j:])    #归并右子列表剩余元素
#     return merged
# def mergeSort(a):       #归并排序
#     if len(a)<=1:
#         return a
#     mid =len(a)//2
#     left=mergeSort(a[:mid])
#     right=mergeSort(a[mid:])
#     return merge(left,right)

#11.3.5快速排序
#1、设置两个变量i和j，分别为首末元素的下标，即i=0，j=n-1
#2、设置列表的第一个元素为关键数据 key=A[0]
#3、从j开始向前搜索，找到第一个小雨可以key的值A[j],将A[j]和A[i]交换
#4、从i开始向后搜索，找到第一个小于key的值A[i],将A[j]和A[i]交换
#5、重复3和4，知道i==j
# def quickSort(a,low,high):
#     i=low
#     j=high
#     if i>=j:
#         return a
#     key=a[i]
#     while i<j:
#         while i<j and a[j]>=key:   #j向前搜索
#             j=j-1
#         a[i]=a[j]
#         while i<j and a[i]<=key:        #i向后搜索
#             i=i+1
#         a[j]=a[i]
#     a[i]=key
#     quickSort(a,low,i-1)       #递归调用
#     quickSort(a,j+1,high)

#11.3.6python语言提供的排序算法
#1、内置数据类型list中的sort()，把列表的项按升序排序
#2、内置函数sorted()保持元列表不变，返回一个新的包含升序排序的项的列表
