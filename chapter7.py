#第七章 错误和异常处理

# 7.1 程序的错误 语法错误/运行时错误/逻辑错误
#7.2异常处理
# try:
#     f=open("t.txt","w")
#     f.write("这是一个测试文件，用于测试异常！！")
#     f1=open("t,txt","r")
# except IOError:
#     print("没有找到文件或读取文件失败")
# else:
#     print("文件写入成功")
# finally:                                                #finally块中的语句不论程序是否异常都会执行
#     f.close()

# try:
#     f=open('mytext.txt','w')
#     while True:
#         s=input('请输入字符串，q结束')
#         if s.upper()=='Q':break
#         f.write(s+'\n')
# except KeyboardInterrupt:
#     print('程序中断！（CTRL-c）')
# finally:
#     f.close()

#7.3 断言处理  用于调试程序
# 断言声明的两种形式 assert <布尔表达式>
#                    assert<布尔表达式>，<字符串表达式>
a=int(input("请输入整数a："))
b=int(input("请输入整数b："))
assert b!=0,'除数不能为0'
c=a/b
print(c)

