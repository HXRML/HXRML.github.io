#缩进相同的一组语句构成一个代码块，我们称之代码组。
#像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
#我们将首行及后面的代码组称为一个子句(clause)。
if expression : 
   suite
elif expression : 
   suite 
else : 
   suite

#print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""
x='2'
y='3'
print('x')
print('y')
print(x)
print(y)
print(x,end="")
print(y,end="")
print(x,y)
print(x,y,end="")

#import 与 from...import

#在 python 用 import 或者 from...import 来导入相应的模块。
#将整个模块(somemodule)导入，格式为： import somemodule
#从某个模块中导入某个函数,格式为： from somemodule import somefunction
#从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#将某个模块中的全部函数导入，格式为： from somemodule import *


#在 Python 中，from somemodule import * 和 import somemodule 有一些重要的区别，主要体现在命名空间和可访问性上。
#import somemodule - 导入整个模块。
#使用模块中的内容时，需要使用模块名作为前缀。例如，如果 somemodule 中有一个函数 foo，你需要这样调用它：somemodule.foo()。
#优点是命名空间保持清晰，避免了与当前模块中的变量和函数名冲突。


#类似于 C/C++ 的 printf，Python 的 print 也能实现格式化输出，方法是使用 % 操作符，
# 它会将左边的字符串当做格式字符串，将右边的参数代入格式字符串：
print("100 + 200 = %d" % 300) #左边的%被替换成右边的300
print("A的小写是%s" % "a") #左边的%s被替换成右边的a
#如果要带入多个参数，则需要用 () 包裹代入的多个参数，参数与参数之间用逗号隔开，参数的顺序应该对应格式字符串中的顺序：
print("%d + %d = %d" % (100,200,300))
print("%s %s" % ("world","hello"))
# %s： 作为字符串
# %d： 作为有符号十进制整数
# %u： 作为无符号十进制整数
# %o： 作为无符号八进制整数
# %x： 作为无符号十六进制整数，a～f采用小写形式
# %X： 作为无符号十六进制整数，A～F采用大写形式
# %f： 作为浮点数
# %e，%E： 作为浮点数，使用科学计数法
# %g，%G： 作为浮点数，使用最低有效数位
