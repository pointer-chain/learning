# Python入门

## 目录

- [1 环境搭建](#1)
    - [1.1 Python下载](#1.1)
    - [1.2 Python安装](#1.2)
    - [1.3 第一个执行程序](#1.3)
- [2 Python基础语法](#2)
    - [2.1 Python保留字符](#2.1)
    - [2.2 Python逻辑语法（行与缩进）](#2.2)
    - [2.3 Python注释](#2.3)
- [3 常见数据类型](#3)
    - [3.1 数字类型](#3.1)
        - [3.1.1 整型](#3.1.1)
        - [3.1.2 长整型](#3.1.2)
        - [3.1.3 浮点型](#3.1.3)
        - [3.1.4 复数](#3.1.4)
    - [3.2 字符串](#3.2)
    - [3.3 列表](#3.3)
    - [3.4 元组](#3.4)
    - [3.5 字典](#3.5)
    - [3.6 集合](#3.6)
    - [3.7 布尔](#3.7)
- [4 运算符](#4)
    - [4.1 常见的数据运算符](#4.1)
    - [4.2 比较运算符](#4.2)
    - [4.3 赋值运算符](#4.3)
    - [4.4 位运算符](#4.4)
    - [4.5 逻辑运算符](#4.5)
    - [4.6 成员运算符](#4.6)
    - [4.7 身份运算符](#4.7)
    - [4.8 运算符优先级](#4.8)
- [5 条件语句](#5)
    - [5.1 if else elif](#5.1)
    - [5.2 match case](#5.2)
- [6 循环语句](#6)
    - [6.1 for循环](#6.1)
    - [6.2 while循环](#6.2)
    - [6.3 continue](#6.3)
    - [6.4 break](#6.4)
    - [6.5 pass](#6.4)
- [7 Python异常处理](#7)
    - [7.1 try/except语句](#7.1)
    - [7.2 Python的标准异常](#7.2)
    - [7.3 raise抛出异常](#7.3)
    - [7.4 判定是否抛出异常](#7.4)

<h2 id="1">1 环境搭建</h3>
<h3 id="1.1">1.1 Python下载</h3>
python下载地址前往官网下载 https://www.python.org/  
个人开发使用推荐版本 3.10.1 项目内根据项目版本需要 BLM 为 Python 3.4  
开发环境根据需要选择对应安装包，例如：Windows、Linux、MacOs  
工具类开发exe可执行文件，Windows需要区分32位与64位  
<h3 id="1.2">1.2 Python安装</h3>
以Windows版本为例： 在C盘（推荐C盘），根目录新建文件夹C:\\python3  
双击运行安装包，选择自定义安装（尽量避免使用默认安装）  
点击勾选Add python 3.xx.x To path（必勾选，否则要自己配置环境变量）  
剩下的配置可以根据需要进行勾选，于安装路径页面选择自己新建的C:\\python3文件夹内 安装完成后  
Windows键盘输入 WIN+S 或者 WIN+R 输入 CMD打开命令行  
输入python 进入页面会显示如下

```
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

则python安装成功
<h3 id="1.3">1.3 第一个执行程序</h3>
在命令行内输入

```python
print("Hello Word!!!")
```

因当前输入为交互式命令，Enter后会返回以下数据

```
Hello Word!!!
```

<h2 id="2">2 Python基础语法</h3>
<h3 id="2.1">2.1 Python保留字符</h3>
所有语言都有着自己的保留字符，在使用这些关键字作为变量名是不被允许的，下面是python语言的30个常用保留字符

||||
|-----|-----|-----| 
|and|exec|not|
|assert|finally|or|
|break|for|pass|
|class|from|print|
|continue|global|raise|
|def|if|return|
|del|import|try|
|elif|in|while|
|else|is|with|
|except|lambda|yield|
|-----|-----|-----| 

<h3 id="2.2">2.2 Python逻辑语法（行与缩进）</h3>
Python语言逻辑实现是由上到下，自左向右  
她没有Java、Go语言的大括号来规定代码块，而是采用了缩进的方式进行编译  
例如： 我们现在需要在循环语句加入变量输出时，缩进不同，结果不同

```python
arg = 5
for arg in range(1):
    print(arg)
print(arg)
```

输出为：

```
0
5
```

很明显对于print对齐位置不同，输出结果也完全不同  
同样的代码，我们来看一下Go语言是如何实现

```GoLang
arg := 5
for arg:=0;arg<1;arg++{
   fmt.Println(arg)
}
fmt.Println(arg)
```

输出为：

```
0
5
```

结论：Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。  
python 最具特色的就是用缩进来写模块
<h3 id="2.3">2.3 Python注释</h3>
在日常编写代码过程中，为了方便后续对代码的理解，我们采用注释的方式对代码进行必要性的诠释  
Python注释有两种形式：单行注释与块注释  
当我们编写代码时，某行代码不需要，使用井号“#”对代码进行注释；例如：

```python
# print("this day is happy day")
```

而块注释，也就是多行注释，我们采用三对双引号的形式进行注释；例如：

```python
"""
print("this day is happy day")
print("this day is happy day")
print("this day is happy day")
"""
```

这里为了让大家更好的理解块注释及Python的基本运作，请查看以下代码：

```python
import pymysql


########连接数据库###############
def connection(hostname='localhost', pointer=3306, username='root', password='123456',
               database='database',
               charset='utf8'):
    db = pymysql.Connect(
        host=hostname,
        port=pointer,
        user=username,
        passwd=password,
        db=database,
        charset=charset
    )
    return db


#######执行sql语句###############
def select(select_sql):
    db = connection()  # 连接数据库
    cursor = db.cursor()
    try:
        cursor.execute(select_sql)
        data = cursor.fetchone()
        return data
    except Exception as error:
        print(error)
        return False
    finally:
        db.close()  # 关闭数据库连接


if __name__ == '__main__':
    sql = """SELECT USERNAME FROM TABLE_NAME WHERE USERNAME IS NOT NULL"""
    select(sql)
```

Python是面向对象的语言，对于块注释内容，并非绝对性的不可使用，而是由语法判断是否使用。   
请思考，以下输出代码，是否有输出，如果有，输出是多少？如果没有，原因是什么？

```python
print("" "这是一个问题" "")
```

<h2 id="3">3 常见的数据类型</h3>
<h3 id="3.1">3.1 数字类型</h3>
<h4 id="3.1.1">3.1.1 整型</h4>
特征：Python2 整型范围(-2**31~2**31-1)
Python3 当范围超出限制时，自动转换为长整型 关键字：int  
例：123，456
<h4 id="3.1.1">3.1.2 长整型</h4>
特征：只存在于Python2.x版本内，没有长度限制，根据内存大小决定长度最大上限，直至内存耗尽 关键字：long  
例：123456L
<h4 id="3.1.1">3.1.3 浮点型</h4>
特征：存在小数点，与整型可以混合运算 关键字：float  
例：123.，122.1
<h4 id="3.1.1">3.1.4 复数</h4>
特征：实部、虚部都是浮点型 关键字：complex  
例：6+3j，complex(6, 3)
<h3 id="3.2">3.2 字符串</h3>  
特征：表示文本的数据类型，通常使用成对的"双引号"/'引号'包含，有序，不可变  
关键字：str   
例："这是一个字符串"， '这是一个字符串'，"""这是一个字符串"""
<h3 id="3.3">3.3 列表</h3>
特征：支持字符、数字、字符串、嵌套，通常使用中[括号]包含，元素用逗号隔开，有序，可变    
关键字：list  
例：[1, 2, 3, 4]
<h3 id="3.4">3.4 元组</h3>
特征：通常使用(括号)包含，元素用逗号隔开，相当于一个只读列表，有序，不可变  
关键字：tuple  
例：(1， 2， 3，4)  
<h3 id="3.5">3.5 字典</h3>
特征：对象集合，以key:value对形式存在，通常使用{大括号包含}，通过键存储，无序，可变   
关键字：dict  
例：{a:1, b:2}
<h3 id="3.5">3.5 集合</h3>
特征：通常使用{大括号}包含，集合内不存在重复数据，无序，可变   
关键字：set  
例：{1, 2, 3, 4}
<h3 id="3.5">3.5 布尔</h3>
特征：只有两种存在形式，True/False  
关键字：bool  
例：True/False
<h2 id="4">4 运算符</h2>
<h3 id="4.1">4.1 算数运算符</h3>

||||
|-----|-----|-----| 
|符号|描述|实例|
|+|加|1+1=2|
|-|减|1-1=0|
|*|乘|1*2=2|
|/|除|4/2=2|
|%|取模|5%3=2|
|**|幂|3**2=9|
|//|整除|5%3=1|

<h3 id="4.2">4.2 比较运算符</h3>

|||||
|-----|-----|-----|-----| 
|符号|条件描述|满足|不满足|False|
|<|小于比较|True|False|
|＞|大于比较|True|False|
|<=|小于等于比较|True|False|
|=＞|大于等于比较|True|False|
|==|等于比较|True|False|
|!=|不等于比较|True|False|
|<>|不等于比较|True|False|

<h3 id="4.3">4.3 赋值运算符</h3>

||||
|-----|-----|-----| 
|运算符|描述|实例|
|=|简单的赋值运算符|a=1|
|+=|加法赋值运算符|a+=1 等同于 a=a+1|
|-=|减法赋值运算符|a-=1 等同于 a=a-1|
|*=|乘法赋值运算符|a*=1 等同于 a=a*1|
|/=|除法赋值运算符|a/=1 等同于 a=a/1|
|%=|取模赋值运算符|a%=1 等同于 a=a%1|
|**=|幂赋值运算符|a**=1 等同于 a=a**1|
|//=|取整除赋值运算符|a//=1 等同于 a=a//1|

<h3 id="4.4 ">4.4 位运算符</h3>
a = 60  
b=13  
二进制：  
a=0011 1100  
b=0000 1101

|||||
|-----|-----|-----|-----| 
|运算符|描述|实例|结果|
|&|按位与运算符，数据转换为二进制，同位都为1时，结果为1|a&b|12 00001100|
|丨|按位或运算符，数据转换为二进制，同位有一个为1，结果为1|a丨b|61 001101101|
|^|按位异或运算符，同位不同，结果为1|a^b|49 00110001|
|~|按位取反运算符，对每个二进制位取反，类似-a-1|~a|-61 11000011|
|＜＜|左移动运算符，对数据个二进制位都左移两个位数，高位丢弃，低位补零|a＜＜2|240 11110000|
|＞＞|右移动运算符，对数据个二进制位都右移两个位数，低位丢弃，高位补零|a＞＞2|15 00001111|

<h3 id="4.5">4.5 逻辑运算符</h3>

||||
|-----|-----|-----|
|运算符|描述|实例|
|and|布尔“与”|a and b|
|or|布尔“或”|a or b|
|not|布尔“非”|not(a and b)|

<h3 id="4.6">4.6 成员运算符</h3>

||||
|-----|-----|-----|
|运算符|描述|实例|
|in|在序列中找到对应的值，返回True|a in b|
|not in|在序列中未找到对应的值，返回True|a not in b|

<h3 id="4.7">4.7 身份运算符</h3>

||||
|-----|-----|-----|
|运算符|描述|实例|
|is|判定两个标识符是否引用自同一个对象|a is b|
|is not|判定两个标识符是否引用自不同对象|a is not b|

<h3 id="4.8">4.8 运算符优先级</h3>

|||
|-----|-----|
|运算符|描述|
|**|指数 (最高优先级)|
|~ + -|按位翻转, 一元加号和减号 (最后两个的方法名为 +@ 和 -@)|
|* / % //|乘，除，取模和取整除|
|+ -|加法减法|
|> > <<|右移，左移运算符|
|&|位 'AND'|
|^ |位运算符|
|<= < > >=|比较运算符|
|<> == !=|等于运算符|
|= %= /= //= -= += *= **=|赋值运算符|
|is is not|身份运算符|
|in not in|成员运算符|
|not and or|逻辑运算符|

<h2 id="5">5 条件语句</h2>
<h3 id="5.1">5.1 if/else/elif</h3>
JJ有一首脍炙人口的歌曲，《可惜没如果》，反应了多少小青年分手后的遗憾。  
感情上，很多“如果”是不存在的，但是，Python里别说“如果”了，我们还能如果1，如果2，如果3；  
那便是if elif else  
首先说一个简单的程序猿的段子

```
小王和小刘是一对情侣，小王是一家公司的程序猿，这天小王出门去上班  
出门前，小刘对小王说：”你晚上回来在你公司楼下，买一斤梨子回来“  
小王回答好，小刘补充道：”如果看到有橘子，买两斤回来“  
于是乎，到了晚上，小王回到家中，手里提溜着两斤梨。
```

这里完完整整诠释了程序的思维是如何做到完美的契合生活的，用我们的Python把对话翻译一下

```
eyes = None
hand = buy 500g pear
if orange in eyes:
    hand = buy 1000g pear
```

这里的如果，就是我们的条件语句if  
我们在使用if时，往往无法满足层层筛选的条件  
例如：今天一位女生要去相亲，女生就对男主有要求了  
（1）有房  
（2）有车  
然而女生又是个颜值控，于是就多了下面的情况：  
（1）长得帅就可以了  
但是谁都无法拒绝王校长的追求，于是又多了一种情况：  
（1）男生是王校长  
但是如果一个都不满足，那就只能孤独终老了  
这里我们用python的条件语句去做诠释的时候，单纯使用一个if，已经满足不了我们了，我们就引入了elif 和 else

```
if man have car and man have house:
    print('it is ok')
elif man is Handsome:
    print('it is ok')
elif man is "王思聪":
    print('it is ok')
else:
    print('i will be alone')
```

言归正传，我们对于平时程序中的条件，其实应用起来会有很多种情况；  
我们简单的用Python语句实现一个学生成绩的筛选逻辑：  
0~59分为差，60~84为良，85~100为优  
我们如何了通过我们的条件语句来实现呢？

```python
arg = int(input("请输入分数"))
if 0 <= arg <= 59:
    print("差")
elif 60 <= arg <= 84:
    print("良")
else:
    print("优")
```

<h3 id="5.2">5.2 match case</h3>

```
def http_error(status):
    match status:
        case 200:
            return "successful"
        case 400:
            return "Bad request"
        case 404:
            return "Not Found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

这里如果使用if else elif来书写

```python
def http_error(status):
    if status == 200:
        return "successful"
    elif status == 400:
        return "Bad request"
    elif status == 404:
        return "Not Found"
    elif status == 418:
        return "I'm a teapot"
    else:
        return "Something's wrong with the internet"
```

<h3 id="6">6 循环语句</h3>
<h3 id="6.1">6.1 for循环</h3>
上文出现的对于女生挑选符合条件的男生有了一个条件判断语句，  
但是如果多个男生，可能就需要用这个条件去筛选满足女生要求的男生，  
如果在代码里实现一个一个去写，频繁、冗余、而且很不美观，  
机智的我们就把众多的男生放入一个容器里，把他们一个一个拿出来做筛选，就跟排队一样  
我们通过Python语言去实现：

```
list_name = ["张三", "李四", "王五", "赵六"]
for man in list_name:
    if man have car and man have house:
        print('it is ok')
    elif man is "Handsome":
        print('it is ok')
    elif man is "王思聪":
        print('it is ok')
    else:
        print('i will be alone')
```

那这里就产生了通式：

```
for 元素名（一般随便取，除非写清楚是什么） in 范围:
    执行的操作项
```

不难看出，既然存在范围，就意味着for循环拥有边界  
如果范围为固定的，或知道范围上限，我们多采用for循环对语句进行循环语句的构建
<h3 id="6.2">6.2 while循环</h3>
因为for循环的边界性，导致当有一些功能我不确定范围、或者范围很模糊的时候，for循环无法满足，于是就有了我们的while循环  
首先while循环的通式：

```
while 条件:
    功能块
```

当你想用有一个死循环的时候：

```
while True:
    功能块
    
while 1:
    功能块
```

假设，前文说到的女生，只是想相亲的时候，蹭一顿饭吃，这里我们可以引入一个while循环了：

```
man = 0
while True:
    if man have car and man have house:
        print('it is ok')
    elif man is "Handsome":
        print('it is ok')
    elif man is "王思聪":
        print('it is ok')
    else:
        print('i will be alone')
    man += 1
```

<h3 id="6.3">6.3 continue</h3>
在广泛的遍历一些范围时，有一些范围内的值，并不是我们要的，我们可以采用从continue的方式，跳过某些数据  
例如：

```python
# 我们不能要1~100的数据中的偶数，我们可以添加条件与continue结合，来跳过偶数
for x in range(1, 101):
    if x % 2 == 0:
        continue
    print(x)
x = 0
while x < 101:
    x += 1
    if x % 2 == 0:
        continue
    print(x)
```

<h3 id="6.4">6.4 break</h3>
我们前面说到while循环使用时，当条件为True时，会陷入死循环之中，在代码运行中会因为进入了死循环，无法自动停止  
因此我们引入条件判断和break来中断循环的构建 例如：

```python
times = 0
while True:
    times += 1
    if times >= 100:
        break
```

<h3 id="6.5">6.5 pass</h3>
Python中还存在一个不做任何操作，而是单纯让代码通过的操作，运用场景不多，下面简单的用一个实例来介绍

```python
# 输入一个成绩，0~59分为差，60~84为良，85~100为优，其他超出范围内的不返回数据
arg = int(input("请输入分数"))
if 0 <= arg <= 59:
    print("差")
elif 60 <= arg <= 84:
    print("良")
elif 85 <= arg <= 100:
    print("优")
else:
    pass
```

<h2 id="7">7 Python异常处理</h2>
<h3 id="7.1">7.1 try/except语句</h3>
在编写功能时，总会有一些情况我们无法得知是否能够正常运行，我们可以通过try/except语句用于将异常捕获，方便分析  
try/except语句语法通式有以下两种

```
第一种
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
else:
<语句>        #如果没有异常发生

第二种
try:
<语句>        #运行别的代码
except <名字>：
<语句>        #如果在try部份引发了'name'异常
except <名字>，<数据>:
<语句>        #如果引发了'name'异常，获得附加的数据
finally:
<语句>        #不管是否有异常发生，都会执行这个语句

```

其中else和finally 非必要，根据应用场景进行编写即可
<h3 id="7.2">7.2 Python的标准异常</h3>
在Python语言中，有一些标准异常，如下：

|||
|-----|-----|
|异常名称|描述|
|BaseException|所有异常的基类|
|SystemExit|解释器请求退出|
|KeyboardInterrupt|用户中断执行(通常是输入^C)|
|Exception|常规错误的基类|
|StopIteration|迭代器没有更多的值|
|GeneratorExit|生成器(generator)发生异常来通知退出|
|StandardError|所有的内建标准异常的基类|
|ArithmeticError|所有数值计算错误的基类|
|FloatingPointError|浮点计算错误|
|OverflowError|数值运算超出最大限制|
|ZeroDivisionError|除(或取模)零 (所有数据类型)|
|AssertionError|断言语句失败|
|AttributeError|对象没有这个属性|
|EOFError|没有内建输入,到达EOF 标记|
|EnvironmentError|操作系统错误的基类|
|IOError|输入/输出操作失败|
|OSError|操作系统错误|
|WindowsError|系统调用失败|
|ImportError|导入模块/对象失败|
|LookupError|无效数据查询的基类|
|IndexError|序列中没有此索引(index)|
|KeyError|映射中没有这个键|
|MemoryError|内存溢出错误(对于Python 解释器不是致命的)|
|NameError|未声明/初始化对象 (没有属性)|
|UnboundLocalError|访问未初始化的本地变量|
|ReferenceError|弱引用(Weak reference)试图访问已经垃圾回收了的对象|
|RuntimeError|一般的运行时错误|
|NotImplementedError|尚未实现的方法|
|SyntaxError|Python 语法错误|
|IndentationError|缩进错误|
|TabError|Tab 和空格混用|
|SystemError|一般的解释器系统错误|
|TypeError|对类型无效的操作|
|ValueError|传入无效的参数|
|UnicodeError|Unicode 相关的错误|
|UnicodeDecodeError|Unicode 解码时的错误|
|UnicodeEncodeError|Unicode 编码时错误|
|UnicodeTranslateError|Unicode 转换时错误|
|Warning|警告的基类|
|DeprecationWarning|关于被弃用的特征的警告|
|FutureWarning|关于构造将来语义会有改变的警告|
|OverflowWarning|旧的关于自动提升为长整型(long)的警告|
|PendingDeprecationWarning|关于特性将会被废弃的警告|
|RuntimeWarning|可疑的运行时行为(runtime behavior)的警告|
|SyntaxWarning|可疑的语法的警告|
|UserWarning|用户代码生成的警告|

<h3 id="7.3">7.3 raise抛出异常</h3>
有一些应用场景内，我们需要对某一情况，主动把异常抛出去，并结束应用程序的时候，可以用到raise语句

```python
try:
    print(1)
except Exception as error:
    raise RuntimeError(error)
```

当然并非一定要在try/except语句内使用才可以  
raise是开发/测试人员主动抛出异常，并自定义异常种类时使用，通常在测试套件、开发自身的单元测试内会经常性用到
<h3 id="7.4">7.4 判定是否抛出异常</h3>
异常并非只有通过主动抛出、try/except语句进行定位  
还可以用python自身携带的assert语句，来让程序判定是否需要抛出异常  
assert语句通式

```
# assert只会在后面的条件满足False时，将程序中止，异常抛出
assert 条件
```

例如：

```python
# 我们定义当输入数字大于0的时候，抛出异常

# 常规写法
value = int(input())
if value > 0:
    raise RuntimeError("您输入的数据已经大于0了")

# assert写法
value = int(input())
assert value <= 0
```
