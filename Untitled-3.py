print("Runoob") #Python 中单引号 ' 和双引号 " 使用完全相同。

if 2<8:   #使用缩进来表示代码块，不需要使用大括号 {}
    print("Yes!")  #缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数
else:
    print("No!")
str = "123456789"  #字符串切片 str[start:end]，其中 start（包含）是切片开始的索引，end（不包含）是切片结束的索引。
print(str)
print(str[0])
print(str[2])
print(str[8])
print(str[1:4]) #输出第二个到第五个字符之前的字符串，不包含第五个
print(str[2:6]) #输出第三个到第七个字符之间的字符串，不包含第七个
print(str[-1]) #输出最后一个字符
print(str[-5]) #输出倒数第五个字符
print(str[1:-1]) #输出第二个到倒数第一个字符之间的字符串，不包含倒数第一个
print(str[-5:-1])
print(str[-7:-3])
print(str[2:6:2]) #输出第三个到第七个字符之间的字符串，不包含第七个，每隔一个取一个，字符串的切片可以加上步长参数 step，语法格式如下：str[start:end:step]
print(str*2) #输出字符串两次
print(str+"houxinru") #输出字符串和字符串，+直接将两个字符串连接起来

print("hello\nworld") #输出字符串和字符串，\n换行
print(r"hello world") #输出字符串和字符串，r不转义字符串中的特殊字符，这里的 r 指 raw，即 raw string，会自动将反斜杠转义，即不会把 \n 当成换行符，而只是当成普通的字符
print('\n')
print('r\n') #r要在''外边，否则会连r一起输出
print(r'\n')
#Python 可以在同一行中使用多条语句，语句之间使用分号 ; 分割

#import的语法

#语法1： import 模块名1 [as 别名1], 模块名2 [as 别名2]，…
#使用这种语法格式的 import 语句，会导入指定模块中的所有成员（包括变量、函数、类等）。
#当需要使用模块中的成员时，需用该模块名（或别名）作为前缀，否则 Python 解释器会报错。

#语法2： from 模块名 import 成员名1 [as 别名1]，成员名2 [as 别名2]，…： 
#使用这种语法格式的 import 
#当程序中使用该成员时，无需附加任何前缀，直接使用成员名（或别名）即可。
#!/usr/bin/python3
import sys; x = 'runoob'; sys.stdout.write(x + '\n') # 输出变量 x的值

