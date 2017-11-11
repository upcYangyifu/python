#第四章 常用内置数据类型
#4.1 python内置数据类型：数值数据/序列数据/集合数据/字典数据/NoneType、NotImplement、EllipsisType/其他数据类型
#4.2 int 数据类型
#a 整数位数可以为任意长度
#b 基本形式 int(x=0) int(x,base=10)指明进制数
#int i 包含的主要方法：i.bit_length() 返回i的二进制位数

#整数运算实例（需要命令配合操作）
# import sys
# a=int(sys.argv[1])
# b=int(sys.argv[2])
# sum=a+b
# print(sum)

#4.3 float类型
#特殊字符串'Infinity' '-Infinity'和'NaN'分别表示正无穷大，负无穷大和非数值
#float对象包含的主要方法：
#as_integer_ratio()  转换为分数
#hex()  转换为十六进制字符串
#fromhex(string)  十六进制字符串转换为浮点数
#is_integer()  判断是否为int类型

#4.4 complex类型（复数）
#complex对象属性和方法
#real   复数的实部
#imag   复数的虚部
#conjugate   共轭复数

#4.5 bool数据类型
#逻辑运算符 not and or

#4.6 str数据类型
#python中没有独立的字符数据类型
#注意：两个紧邻的字符串如果中间只有空格，自动拼接为一个字符串
#内置函数： ord() 把字符串转换为对应的Unicode码
#           chr() 把十进制数转换为对应的字符
#转义字符
#str对象的属性和方法 str.upper(s)  将字符串s变为大写输出
#字符串长度 str.len(s)
#repr(s) 返回一个对象的更精确的字符串表示形式
#字符串的格式化 str.format()

#4.7 比较关系运算和条件表达式
#is/is not 判断是不是同一个对象
#in/ not in 判断是不是成员

#4.8 算数运算符和位运算符
#4.9 混合运算和数值类型转换
#强制转换 int(1.23) 将1.23转换为int 类型

#4.10 内置标准数学函数
#abs(x) 求x的绝对值
#divmod(a,b) 返回a除以b的商和余数
#pow(x,y[[,z]) x的y次幂 或者pow(x,y)%z
#round(number[,ndigits]) 四舍五入取整 如果指定ndigits，则保留ndigits小数
#sum(iterable[,start]) 求以start为初值的和
#bin hex oct 分别转换为二进制，十六进制，八进制