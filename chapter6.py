#第六章 输入和输出

#6.1 输入和输出概述
#实现交互功能的方式：a命令行参数 b标准输入和输出函数 c文件输入和输出 d图形化用户界面

#6.2 命令行参数
#6.2.1 sys.argv与命令行参数
# import sys,random
# n=int(sys.argv[1])
# for i in range(n):
#     print(random.randrange(0,100))
#6.2.2 argparse模块与命令行参数
# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument('--length',default=10,type=int,help='长度')
# parser.add_argument('--width',default=5,type=int,help='宽度')
# args=parser.parse_args()
# area=args.length*args.width
# print('面积=',area)

#6.3 标准输入和标准输出函数
#6.3.1 输入和输出函数
# print(1,2,3)#采用空格作为分隔符
# print(1,2,3,sep=',',end='.\n')#采用逗号分隔，以点结束并换行
# for i in range(5):
#     print(i,end=' ')#输出时使用空格代替换行符
# import datetime
# sName =input("请输入您的姓名：")
# birthyear=int(input("请输入您的出生年份："))
# age=datetime.date.today().year-birthyear
# print("您好！{0}.您{1}岁".format(sName,age))
#6.3.2 交互式用户输入
#6.3.3 运行时提示输入密码
# import getpass
# username =input("用户名：")
# passwd = getpass.getpass("密码：")#getpass在pycharm里无效，可以用python自带的ide
# if username=='jianghong' and passwd=='password':
#     print('登录成功')
# else:
#     print('登录失败')

#6.4 文件和文件对象
#6.4.1 文件对象和open函数
# try:                               #open函数放在try块中无法执行
#     f = open(r'D:\1.txt','rt')
# except:
#     print(1)
# finally:
#     f.close()

# f=open(r'D:\a.txt','w') #文件位置前边要加一个r
# f.print(f.read())
# f.write('sss')
# f.close()

#6.4.2 文件的打开、写入、读取和关闭
#import sys
#filename =sys.argv[0]

# f=open(r'D:\a.txt','r',encoding='utf8')
# line_no=0
# while True:
#     line_no+=1
#     line =f.readline()
#     if line:
#         print(line_no,":",line) #显示行号和该行内容
#     else:
#         break
# f.close()

#6.4.3 with语句和上下文管理协议
# import sys
# filename=sys.argv[0]

# line_no=0                                #可以实现与上一代码相同的作用
# with open(r'D:\a.txt','r',encoding='utf8') as f:
#     for line in f:
#         line_no+=1
#         print(line_no,":",line)
# f.close()

#6.5 标准输入输出和错误流
# import sys        #标准输入流是缓冲的，标准输出流和错误输出流是非缓冲的
# print(sys.stdin)
# print(sys.stdout)
# print(sys.stderr)
#6.5.2 读取任意长度的输入流
# import sys             #计算输入流中数据的平均值（）下列程序用cmd可以运行，在pycharm无法运行
# total=0.0
# count=0
# for line in sys.stdin:
#     count+=1
#     total +=float(line)
# avg=total/count
# print("平均值：",avg)
#6.5.3 标准输入输出和错误流重定向
# import sys                          #在pycharm中无法运行，需要cmd
# n=int(sys.argv[1])
# power=1
# i=0
# f=open('out.log','w')
# sys.stdin=f
# while i<=n:
#     print(str(i),' ',str(power))
#     power=2*power
#     i=i+1
# sys.stdout=sys.__stdout__
# print('done!')

#6.6 重定向和管道
#重定向标准输出到一个文件  程序>输出文件
#重定向文件到标准输入    程序<输入文件
#管道 程序1|程序2  程序1 的标准输出作为程序2 的标准输入